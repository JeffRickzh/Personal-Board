import os
from datetime import datetime
import yaml
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI, AsyncOpenAI
import re
from persona_engine import PersonaEngine
import json

app = FastAPI(title="Personal Board API")

# Setup CORS to allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MIMO_API_KEY = "sk-cqwylmqq1varypuqxu5q8xr8keffipl8ivsn71ojyk91btgp"
MIMO_BASE_URL = "https://api.xiaomimimo.com/v1" 
MODEL_NAME = "mimo-v2.5" 

def load_persona(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Global dictionary to store instantiated Persona Engines and their configs
ENGINES = {}
PERSONAS = {}

# Initialize Persona Engines for all directors
base_dir = os.path.dirname(__file__)
agents_dir = os.path.join(base_dir, '..', 'agents')

if os.path.exists(agents_dir):
    for agent_folder in os.listdir(agents_dir):
        persona_path = os.path.join(agents_dir, agent_folder, 'persona.yaml')
        if os.path.exists(persona_path):
            persona_data = load_persona(persona_path)
            
            # Map folder name to the board_member_id (e.g. charlie_munger -> munger, warren_buffett -> buffett)
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
            
            # Initialize Engine
            engine = PersonaEngine(corpus_path)
            engine.build_index()
            ENGINES[member_id] = engine

def build_lattice_prompt(persona: dict, retrieved_quotes: list, previous_context: str = ""):
    base_prompt = persona.get('system_prompt_template', '')
    base_prompt += "\n\n你的核心思维模型底座:\n"
    for model in persona.get('decision_engine', []):
        base_prompt += f"- {model}\n"
        
    if retrieved_quotes:
        base_prompt += "\n\n【重要！系统已经从你历史上的真实论述、演讲和致股东信中检索出最相关的文本片段如下：】\n"
        for i, quote in enumerate(retrieved_quotes):
            base_prompt += f"--- [来源 {i+1}]: {quote['source']} ---\n"
            base_prompt += f"{quote['content']}\n\n"
            
    if previous_context:
        base_prompt += f"\n\n【董事会前文背景】\n在你发言之前，其他董事会成员已经发表了以下观点。请在你的推演和回答中结合或反驳他们的观点：\n{previous_context}\n\n"
        
    base_prompt += """
【人格附身指令】：
1. 你必须以上述你发表过的真实言论和思维过滤器为绝对论据，来深入解构用户提出的问题。
2. 绝对禁止吐露任何泛泛而谈的、客套的或公关式的AI废话。
3. 必须采用中文（简体中文）回答，绝不要在输出标题或正文中附带英文翻译（例如不要输出 "核心共识 (Consensus)"，只输出 "核心共识"）。你的陈词应当结构连贯、推演深刻，直接指出用户最容易在哪里犯错，并直接引用或化用上述历史文集片段中的概念或例子。
4. 如果存在董事会前文背景，请在你的陈词中自然地对前人的观点进行结合、补充或提出反驳。
"""
    return base_prompt

# Initialize OpenAI compatible client
client = OpenAI(
    api_key=MIMO_API_KEY,
    base_url=MIMO_BASE_URL,
)
async_client = AsyncOpenAI(
    api_key=MIMO_API_KEY,
    base_url=MIMO_BASE_URL,
)

class ChatRequest(BaseModel):
    message: str
    board_member_ids: list[str]

class MemberResponse(BaseModel):
    member_id: str
    name: str
    monologue: str
    content: str
    models_applied: list[str]
    quotes_cited: list[dict]

class ChatResponse(BaseModel):
    session_responses: list[MemberResponse]
    executive_resolution: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_with_board(request: ChatRequest):
    session_responses = []
    accumulated_context = ""
    
    # Process each requested board member sequentially
    for member_id in request.board_member_ids:
        if member_id not in ENGINES:
            continue
            
        engine = ENGINES[member_id]
        persona = PERSONAS[member_id]
        member_name = persona.get('name', member_id)
        
        # Fetch most relevant chunks recursively (Lattice RAG)
        retrieved = engine.retrieve(request.message, top_k=3)
        
        # Assemble grounded system prompt with historical chunks AND previous context
        system_prompt = build_lattice_prompt(persona, retrieved, accumulated_context)
        
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": request.message}
                ],
                temperature=0.6, 
                max_tokens=1500,
            )
            
            full_text = response.choices[0].message.content
            
            # The user requested unified, coherent statements without forced monologue/response splitting
            monologue = ""
            content = full_text.strip()
                
            models_zh = {
                "逆向思维": "Inversion", "安全边际": "Margin of Safety", "能力圈": "Circle of Competence",
                "机会成本": "Opportunity Cost", "人类误判心理学": "Psychology of Human Misjudgment",
                "极度求真": "Extreme Truth", "社会认同倾向": "Social Proof Bias",
                "激励机制引起的偏见": "Reward Super-Response Bias", "护城河": "Economic Moat",
                "市场先生": "Mr. Market", "买入并持有": "Buy and Hold", "内在价值": "Intrinsic Value",
                "长期主义": "Long-termism", "诚实管理层": "Management"
            }
            
            models_applied = []
            for zh_name, en_name in models_zh.items():
                if zh_name in monologue or en_name in monologue or zh_name in content:
                    models_applied.append(zh_name)
            if not models_applied:
                models_applied = ["独立思考框架"]
                
            # Append to session responses
            session_responses.append(MemberResponse(
                member_id=member_id,
                name=member_name,
                monologue=monologue,
                content=content,
                models_applied=models_applied[:4],
                quotes_cited=retrieved
            ))
            
            # Build accumulated context for the next member
            accumulated_context += f"【{member_name} 的核心观点】: {content}\n\n"
            
        except Exception as e:
            session_responses.append(MemberResponse(
                member_id=member_id,
                name=member_name,
                monologue=f"API 推理失败: {str(e)}",
                content="我无法连接到思维引擎。",
                models_applied=[],
                quotes_cited=[]
            ))
            
    # Final Synthesis (Executive Resolution)
    if accumulated_context:
        synthesis_prompt = f"""
        你现在是个人董事会的首席书记员 (Chief Board Secretary) 兼执行官。
        用户提出了一个战略问题："{request.message}"
        
        以下是各位顶级董事的发言总结与交锋记录：
        {accumulated_context}
        
        请你综合以上所有董事的意见，给出一份详尽的、极具专业深度的《首席书记员会议纪要》(Chief Secretary's Board Report)。
        
        你的回答应包含：
        1. 核心共识：董事们在哪里达成了一致？
        2. 视角碰撞：不同董事的视角有什么区别或补充？
        3. 最终战略决议：基于上述智慧，给用户一份具体、可执行、带有红线护栏的操作指南。
        
        请畅所欲言，完全保留董事们讨论的精华内容，字数不限，排版要清晰、犀利、客观，绝对不要在输出标题中包含英文翻译，不要讲公关废话。
        """
        try:
            synth_res = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": synthesis_prompt}],
                temperature=0.3,
                max_tokens=4000,
            )
            executive_resolution = synth_res.choices[0].message.content.strip()
        except Exception as e:
            executive_resolution = "生成最终决议失败。"
    else:
        executive_resolution = "由于所有节点均未提供有效输出，无法生成决议。"

    return ChatResponse(
        session_responses=session_responses,
        executive_resolution=executive_resolution
    )

@app.post("/api/chat_stream")
async def chat_with_board_stream(request: ChatRequest):
    async def event_generator():
        accumulated_context = ""
        
        # Process each requested board member sequentially
        for member_id in request.board_member_ids:
            if member_id not in ENGINES:
                continue
                
            engine = ENGINES[member_id]
            persona = PERSONAS[member_id]
            member_name = persona.get('name', member_id)
            
            # Yield thinking status
            yield f"data: {json.dumps({'event': 'status', 'member_id': member_id, 'name': member_name, 'state': 'retrieving', 'message': 'Retrieving context...'}, ensure_ascii=False)}\n\n"
            
            # Fetch most relevant chunks recursively
            retrieved = engine.retrieve(request.message, top_k=3)
            
            yield f"data: {json.dumps({'event': 'quotes', 'member_id': member_id, 'quotes': retrieved}, ensure_ascii=False)}\n\n"
            
            # Assemble grounded system prompt
            system_prompt = build_lattice_prompt(persona, retrieved, accumulated_context)
            
            yield f"data: {json.dumps({'event': 'status', 'member_id': member_id, 'state': 'speaking', 'message': 'Speaking...'}, ensure_ascii=False)}\n\n"
            
            content = ""
            try:
                response = await async_client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": request.message}
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
            accumulated_context += f"【{member_name} 的核心观点】: {content}\n\n"
            
        # Final Synthesis
        if accumulated_context:
            yield f"data: {json.dumps({'event': 'status', 'member_id': 'secretary', 'name': 'Chief Board Secretary', 'state': 'synthesizing', 'message': 'Drafting Executive Resolution...'}, ensure_ascii=False)}\n\n"
            
            synthesis_prompt = f"""
            你现在是个人董事会的首席书记员 (Chief Board Secretary) 兼执行官。
            用户提出了一个战略问题："{request.message}"
            
            以下是各位顶级董事的发言总结与交锋记录：
            {accumulated_context}
            
            请你综合以上所有董事的意见，给出一份详尽的、极具专业深度的《首席书记员会议纪要》。
            
            你的回答应包含：
            1. 核心共识：董事们在哪里达成了一致？
            2. 视角碰撞：不同董事的视角有什么区别或补充？
            3. 最终战略决议：基于上述智慧，给用户一份具体、可执行、带有红线护栏的操作指南。
            
            请畅所欲言，完全保留董事们讨论的精华内容，字数不限，排版要清晰、犀利、客观，绝不要在输出的标题中包含英文翻译，不要讲公关废话。
            """
            
            try:
                synth_res = await async_client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[{"role": "user", "content": synthesis_prompt}],
                    temperature=0.3,
                    max_tokens=4000,
                    stream=True,
                )
                
                full_resolution = ""
                async for chunk in synth_res:
                    if chunk.choices and len(chunk.choices) > 0 and chunk.choices[0].delta.content:
                        delta = chunk.choices[0].delta.content
                        full_resolution += delta
                        yield f"data: {json.dumps({'event': 'secretary_token', 'text': delta}, ensure_ascii=False)}\n\n"
                        
            except Exception as e:
                yield f"data: {json.dumps({'event': 'error', 'member_id': 'secretary', 'message': str(e)}, ensure_ascii=False)}\n\n"
                
        yield f"data: {json.dumps({'event': 'board_end'}, ensure_ascii=False)}\n\n"
        
        # --- Save to Markdown History ---
        history_dir = os.path.join(base_dir, '..', 'chathistory')
        os.makedirs(history_dir, exist_ok=True)
        now = datetime.now()
        timestamp_str = now.strftime("%Y%m%d_%H%M%S")
        # create a safe filename
        safe_query = re.sub(r'[\\/*?:"<>|]', "", request.message)
        safe_query = safe_query.replace('\n', ' ').strip()
        safe_query = safe_query[:20] if safe_query else "empty_query"
        filename = f"{timestamp_str}_{safe_query}.md"
        filepath = os.path.join(history_dir, filename)
        
        md_content = f"# Topic: {request.message}\n"
        md_content += f"**Date:** {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        md_content += f"## 智囊推演 (Board Analysis)\n{accumulated_context}\n"
        if 'full_resolution' in locals():
            md_content += f"## 最终决议 (Executive Resolution)\n{full_resolution}\n"
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.get("/api/history")
async def get_history_list():
    history_dir = os.path.join(base_dir, '..', 'chathistory')
    if not os.path.exists(history_dir):
        return []
    
    files = []
    for filename in os.listdir(history_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(history_dir, filename)
            files.append({
                "filename": filename,
                "timestamp": os.path.getmtime(filepath)
            })
    files.sort(key=lambda x: x["timestamp"], reverse=True)
    return files

@app.get("/api/history/{filename}")
async def get_history_file(filename: str):
    history_dir = os.path.join(base_dir, '..', 'chathistory')
    filepath = os.path.join(history_dir, filename)
    if os.path.exists(filepath) and filename.endswith(".md"):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            return {"filename": filename, "content": content}
    return {"error": "File not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
