import os
import json
import uuid
from datetime import datetime
import yaml
import asyncio
import re
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI, AsyncOpenAI
from persona_engine import PersonaEngine
from dotenv import load_dotenv

# Load local environment variables from .env file
load_dotenv()

app = FastAPI(title="Personal Board API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MIMO_API_KEY = os.getenv("MIMO_API_KEY", "")
MIMO_BASE_URL = os.getenv("MIMO_BASE_URL", "https://token-plan-cn.xiaomimimo.com/v1")

if not MIMO_API_KEY:
    print("WARNING: MIMO_API_KEY is not set. Please set it in backend/.env or your system environment variables.") 

def load_persona(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

ENGINES = {}
PERSONAS = {}

base_dir = os.path.dirname(__file__)
agents_dir = os.path.join(base_dir, '..', 'agents')

if os.path.exists(agents_dir):
    for agent_folder in os.listdir(agents_dir):
        persona_path = os.path.join(agents_dir, agent_folder, 'persona.yaml')
        if os.path.exists(persona_path):
            persona_data = load_persona(persona_path)
            
            if "munger" in agent_folder.lower():
                member_id = "munger"
            elif "buffett" in agent_folder.lower():
                member_id = "buffett"
            else:
                member_id = agent_folder

            folder_name = persona_data.get('corpus_folder_name')
            if folder_name:
                corpus_path = os.path.join(base_dir, '..', 'board of directors', folder_name)
            else:
                if "munger" in agent_folder.lower():
                    corpus_path = os.path.join(base_dir, '..', 'board of directors', 'CharlieMungerTalk-master')
                elif "buffett" in agent_folder.lower():
                    corpus_path = os.path.join(base_dir, '..', 'board of directors', 'Warren Buffett')
                else:
                    corpus_path = os.path.join(base_dir, '..', 'board of directors', agent_folder)

            PERSONAS[member_id] = persona_data
            
            engine = PersonaEngine(corpus_path)
            engine.build_index()
            ENGINES[member_id] = engine

def build_lattice_prompt(persona: dict, retrieved_quotes: list, previous_context: str = "", debate_drafts: str = ""):
    base_prompt = persona.get('system_prompt_template', '')
    base_prompt += "\n\n你的核心思维模型底座:\n"
    for model in persona.get('decision_engine', []):
        base_prompt += f"- {model}\n"
        
    if retrieved_quotes:
        base_prompt += "\n\n【系统检索出的你的历史真实论述片段】：\n"
        for i, quote in enumerate(retrieved_quotes):
            base_prompt += f"--- [来源 {i+1}]: {quote['source']} ---\n{quote['content']}\n\n"
            
    if previous_context:
        base_prompt += f"\n\n【会议历史背景】\n以下是你们在这个会议中之前的多轮讨论记录，请以此为上下文：\n{previous_context}\n\n"
        
    if debate_drafts:
        base_prompt += f"\n\n【其它董事的初步立场（供你反驳与交锋）】\n在正式发言前，其他董事私下提出的初步核心立场如下。在你的发言中，你必须点名引用、批评或赞同他们的立场，形成激烈的辩论交锋！\n{debate_drafts}\n\n"

    base_prompt += """
【人格附身指令】：
1. 你必须以上述你发表过的真实言论和思维过滤器为绝对论据，来深入解构用户提出的问题。
2. 绝对禁止吐露任何泛泛而谈的、客套的或公关式的AI废话。
3. 必须采用中文（简体中文）回答，不要输出多余的英文翻译。你的陈词应当结构连贯、推演深刻。
4. 结合历史会议背景，如果你看到了其他董事的立场，务必在陈词中直接点名进行交锋（如“巴菲特刚才提到的安全边际是对的，但是...”或“我不同意格雷厄姆的看法，因为...”）。
5. 绝对禁止在括号内、星号内或正文任何位置输出任何肢体动作、舞台旁白、环境背景或动作场景描写（例如：(缓缓放下手中的可乐罐)、(身体微微前倾)、(沉默片刻)、*叹了口气* 或 (喝了一口水) 等）。你必须直接陈述你的核心逻辑和论据，坚决不进行任何戏剧表演，禁止包含任何括号或星号内的表演性、描述性词汇。
6. 严禁使用“如果他在这里，他会说...”或“我想象他会说...”这类虚拟或假设性剧本台词。其他董事（巴菲特、芒格、格雷厄姆、罗素）此时就在会议现场与你一同开会，你应当自然地进行会场对话和交锋。
"""
    return base_prompt

def format_history_context(messages: list) -> str:
    context = ""
    for msg in messages[:-1]: # exclude the current latest user message
        role = "用户 (User)" if msg["role"] == "user" else "董事会成员 (Board) / 书记员"
        name = msg.get("member_name", "")
        speaker = f"{role} {name}".strip()
        context += f"【{speaker}】:\n{msg['content']}\n\n"
    return context

client = OpenAI(api_key=MIMO_API_KEY, base_url=MIMO_BASE_URL)
async_client = AsyncOpenAI(api_key=MIMO_API_KEY, base_url=MIMO_BASE_URL)

class ChatMessage(BaseModel):
    role: str
    content: str
    member_id: str = None
    member_name: str = None
    quotes: list = []

class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    board_member_ids: list[str]
    mode: str = "fast"
    session_id: str = ""

def save_session_history(session_id: str, title: str, messages: list):
    history_dir = os.path.join(base_dir, '..', 'chathistory')
    os.makedirs(history_dir, exist_ok=True)
    filepath = os.path.join(history_dir, f"{session_id}.json")
    
    data = {
        "session_id": session_id,
        "title": title,
        "timestamp": datetime.now().timestamp(),
        "messages": [m.model_dump() if hasattr(m, 'model_dump') else m for m in messages]
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.post("/api/chat_stream")
async def chat_with_board_stream(request: ChatRequest):
    async def event_generator():
        messages = [m.model_dump() for m in request.messages]
        latest_user_message = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
        session_id = request.session_id or str(uuid.uuid4())
        
        # Determine Title
        first_user_msg = next((m["content"] for m in messages if m["role"] == "user"), "战略会议")
        title = first_user_msg.replace('\n', ' ').strip()[:25]
        
        previous_context = format_history_context(messages)
        model_to_use = "mimo-v2.5" if request.mode == "fast" else "mimo-v2.5-pro"
        
        debate_drafts_dict = {}
        quotes_dict = {}
        
        # PRO MODE: Round 1 (Hidden Pre-Drafts)
        if request.mode == "pro":
            yield f"data: {json.dumps({'event': 'system', 'message': 'Pro 模式已启用：董事们正在私下拟定初步立场并准备交锋...'}, ensure_ascii=False)}\n\n"
            
            async def generate_draft(mid):
                engine = ENGINES[mid]
                persona = PERSONAS[mid]
                retrieved = engine.retrieve(latest_user_message, top_k=2)
                quotes_dict[mid] = retrieved
                
                draft_prompt = build_lattice_prompt(persona, retrieved, previous_context)
                draft_prompt += "\n【额外指令】：这是一份内部手稿。请用简短的150字以内概括你对这个问题的核心判断，以供其他董事参考。"
                
                try:
                    res = await async_client.chat.completions.create(
                        model=model_to_use,
                        messages=[{"role": "system", "content": draft_prompt}, {"role": "user", "content": latest_user_message}],
                        temperature=0.6,
                        max_tokens=300
                    )
                    return mid, persona.get('name', mid), res.choices[0].message.content
                except Exception:
                    return mid, persona.get('name', mid), "系统故障，未提供初步立场。"

            tasks = [generate_draft(mid) for mid in request.board_member_ids if mid in ENGINES]
            results = await asyncio.gather(*tasks)
            
            debate_drafts_str = ""
            for mid, mname, draft in results:
                debate_drafts_dict[mid] = draft
                debate_drafts_str += f"【{mname} 的初步立场】: {draft}\n\n"
                
            yield f"data: {json.dumps({'event': 'system', 'message': '初步立场已确立。正式会议交锋开始！'}, ensure_ascii=False)}\n\n"
        
        # Round 2: Formal Stream Output
        turn_responses = []
        for member_id in request.board_member_ids:
            if member_id not in ENGINES: continue
            
            engine = ENGINES[member_id]
            persona = PERSONAS[member_id]
            member_name = persona.get('name', member_id)
            
            yield f"data: {json.dumps({'event': 'status', 'member_id': member_id, 'name': member_name, 'state': 'retrieving', 'message': 'Retrieving context...'}, ensure_ascii=False)}\n\n"
            
            if request.mode == "pro":
                retrieved = quotes_dict.get(member_id, [])
                # Construct draft string EXCEPT self
                other_drafts = ""
                for mid, draft in debate_drafts_dict.items():
                    if mid != member_id:
                        other_drafts += f"【{PERSONAS[mid].get('name', mid)}】: {draft}\n\n"
                system_prompt = build_lattice_prompt(persona, retrieved, previous_context, debate_drafts=other_drafts)
            else:
                # FAST MODE
                retrieved = engine.retrieve(latest_user_message, top_k=3)
                system_prompt = build_lattice_prompt(persona, retrieved, previous_context)
            
            yield f"data: {json.dumps({'event': 'quotes', 'member_id': member_id, 'quotes': retrieved}, ensure_ascii=False)}\n\n"
            yield f"data: {json.dumps({'event': 'status', 'member_id': member_id, 'state': 'speaking', 'message': 'Speaking...'}, ensure_ascii=False)}\n\n"
            
            content = ""
            try:
                response = await async_client.chat.completions.create(
                    model=model_to_use,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": latest_user_message}
                    ],
                    temperature=0.6, 
                    max_tokens=4000,
                    stream=True,
                )
                
                async for chunk in response:
                    if chunk.choices and len(chunk.choices) > 0 and chunk.choices[0].delta.content:
                        delta = chunk.choices[0].delta.content
                        content += delta
                        yield f"data: {json.dumps({'event': 'token', 'member_id': member_id, 'text': delta}, ensure_ascii=False)}\n\n"
                        
            except Exception as e:
                yield f"data: {json.dumps({'event': 'error', 'member_id': member_id, 'message': str(e)}, ensure_ascii=False)}\n\n"
                
            yield f"data: {json.dumps({'event': 'turn_end', 'member_id': member_id, 'name': member_name}, ensure_ascii=False)}\n\n"
            
            turn_message = {
                "role": "assistant",
                "member_id": member_id,
                "member_name": member_name,
                "content": content,
                "quotes": retrieved
            }
            turn_responses.append(turn_message)
            messages.append(turn_message)
            
            # Fast mode updates the previous_context progressively
            if request.mode == "fast":
                previous_context += f"【{member_name} 的核心观点】: {content}\n\n"
        
        # Save history after round completes
        save_session_history(session_id, title, messages)
        yield f"data: {json.dumps({'event': 'board_end', 'session_id': session_id}, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

class SynthesizeRequest(BaseModel):
    messages: list[ChatMessage]
    session_id: str
    
@app.post("/api/synthesize")
async def synthesize_resolution(request: SynthesizeRequest):
    async def event_generator():
        messages = [m.model_dump() for m in request.messages]
        context = format_history_context(messages) + "\n\n"
        
        # Append the very last few messages if not in context
        for msg in messages[-4:]:
            role = "用户 (User)" if msg["role"] == "user" else "董事会成员 (Board)"
            name = msg.get("member_name", "")
            context += f"【{role} {name}】:\n{msg['content']}\n\n"
        
        yield f"data: {json.dumps({'event': 'status', 'member_id': 'secretary', 'state': 'synthesizing', 'message': 'Drafting Executive Resolution...'}, ensure_ascii=False)}\n\n"
        
        synthesis_prompt = f"""
        你现在是个人董事会的首席书记员 (Chief Board Secretary) 兼执行官。
        请根据本次会议的完整交锋记录，给出一份最终的《首席书记员会议纪要》(Executive Resolution)。
        
        记录如下：
        {context}
        
        你的回答应包含：
        1. 核心共识：董事们在哪里达成了一致？
        2. 视角碰撞：不同董事的视角有什么区别或补充？
        3. 最终战略决议：基于上述智慧，给用户一份具体、可执行、带有红线护栏的操作指南。
        
        【纪要风格约束】：
        1. 会议纪要必须保持极度正式、严谨、专业的商业报告格调，完全剔除任何戏剧性的描述、动作细节、舞台旁白或场景渲染。
        2. 严禁在回答中加入类似“（沉思片刻）”、“（面带微笑）”等情绪性或动作性括号/星号描写。
        3. 将董事们发言中的核心逻辑、多学科格栅和安全边际思想客观、精准地凝练，使其读起来像一份高水平的公司决策性文件。
        
        字数不限，解除一切Token约束。排版要清晰、犀利、客观，绝不要在输出的标题中包含英文翻译。
        """
        
        full_resolution = ""
        try:
            synth_res = await async_client.chat.completions.create(
                model="mimo-v2.5-pro", # Always use pro for synthesis
                messages=[{"role": "user", "content": synthesis_prompt}],
                temperature=0.3,
                max_tokens=8000,
                stream=True,
            )
            
            async for chunk in synth_res:
                if chunk.choices and len(chunk.choices) > 0 and chunk.choices[0].delta.content:
                    delta = chunk.choices[0].delta.content
                    full_resolution += delta
                    yield f"data: {json.dumps({'event': 'secretary_token', 'text': delta}, ensure_ascii=False)}\n\n"
                    
        except Exception as e:
            yield f"data: {json.dumps({'event': 'error', 'member_id': 'secretary', 'message': str(e)}, ensure_ascii=False)}\n\n"
            
        yield f"data: {json.dumps({'event': 'synthesis_end'}, ensure_ascii=False)}\n\n"
        
        # Save to history
        if request.session_id:
            messages.append({
                "role": "secretary",
                "member_id": "secretary",
                "member_name": "Chief Board Secretary",
                "content": full_resolution,
                "quotes": []
            })
            first_user_msg = next((m["content"] for m in messages if m["role"] == "user"), "战略会议")
            title = first_user_msg.replace('\n', ' ').strip()[:25]
            save_session_history(request.session_id, title, messages)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.get("/api/history")
async def get_history_list():
    history_dir = os.path.join(base_dir, '..', 'chathistory')
    if not os.path.exists(history_dir):
        return []
    
    files = []
    for filename in os.listdir(history_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(history_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    files.append({
                        "filename": filename,
                        "title": data.get("title", "未命名会议"),
                        "timestamp": data.get("timestamp", os.path.getmtime(filepath)),
                        "session_id": data.get("session_id", "")
                    })
            except Exception:
                pass
    files.sort(key=lambda x: x["timestamp"], reverse=True)
    return files

@app.get("/api/history/{filename}")
async def get_history_file(filename: str):
    history_dir = os.path.join(base_dir, '..', 'chathistory')
    filepath = os.path.join(history_dir, filename)
    if os.path.exists(filepath) and filename.endswith(".json"):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    return {"error": "File not found"}

@app.delete("/api/history/{filename}")
async def delete_history_file(filename: str):
    history_dir = os.path.join(base_dir, '..', 'chathistory')
    filepath = os.path.join(history_dir, filename)
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            return {"status": "success"}
        except Exception as e:
            return {"error": str(e)}
    return {"error": "File not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
