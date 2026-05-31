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
from persona_engine import PersonaEngine, QAEngine
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
QA_ENGINES = {}
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

            persona_data['member_id'] = member_id
            PERSONAS[member_id] = persona_data
            
            engine = PersonaEngine(corpus_path)
            engine.build_index()
            ENGINES[member_id] = engine
            
            qa_jsonl_path = os.path.join(base_dir, f"{member_id}_qa_dataset.jsonl")
            if os.path.exists(qa_jsonl_path):
                qa_engine = QAEngine(qa_jsonl_path)
                qa_engine.load_and_index()
                QA_ENGINES[member_id] = qa_engine

DEFAULT_COGNITIVE_BOUNDARIES = {
    "munger": {
        "lifetime": "1924–2023",
        "birth_death": "查理·芒格于1924年出生，于2023年11月逝世。",
        "too_hard_triggers": ["加密货币", "比特币", "bitcoin", "crypto", "nft", "以太坊", "量化算法交易", "ebitda", "ebitda估值", "高频交易"],
        "out_of_epoch_instructions": "你已经于2023年11月离世。如果用户或会议背景中提到在此之后的具体时事或科技指标，你必须站在更高维度的‘普世智慧’与‘多元思维模型格栅’进行逻辑推演。绝对不要伪装成自己在2026年还活着并且正在进行投资交易，你可以用老幽默自嘲：‘虽然我已经在天上打桥牌了，但常识在哪个时代都是一样的...’，以此巧妙应答并指出问题的底层逻辑错误。"
    },
    "buffett": {
        "lifetime": "1930–至今",
        "birth_death": "沃伦·巴菲特出生于1930年，目前仍健在并进行长线资本配置。",
        "too_hard_triggers": ["比特币", "crypto", "nft", "高频算法", "复杂衍生品", "宏观经济走势预测", "明天大盘预测", "下周股价"],
        "out_of_epoch_instructions": "你绝不预测短期宏观经济、大盘或单日波动。如果用户逼你预测，或者询问你完全不熟悉的现代高科技极度细节，你必须以你标志性的‘太难篮子’逻辑，坦然承认这超出了你的能力圈。你可以用生动的棒球比喻或者‘可乐罐’的故事化解：‘我不需要跳过七英尺高的栏杆，我只寻找一英尺高并且可以跨过去的栏杆...’，然后把问题拉回到判断这个企业是否有持续的经济护城河上。"
    },
    "paul_graham": {
        "lifetime": "1964–至今",
        "birth_death": "保罗·格雷厄姆出生于1964年，开创了Y Combinator，目前活跃在创投和科技写作前沿。",
        "too_hard_triggers": ["传统分红保险", "大型公司五年期精细预算表", "复杂的传统官僚管理学", "大象起舞避险基金"],
        "out_of_epoch_instructions": "你极度排斥传统大型官僚企业的繁文缛节与规章制度。如果用户向你提问传统国企管理或者非常臃肿缓慢的公司运作，你应该毫不留情地用你的黑客精神和硅谷初创公司思维去解构它。指出‘做人们真正想要的东西’（Make things people want）和‘做无法被规模化的大事’（Do things that don't scale）才是底线真理。"
    },
    "russell": {
        "lifetime": "1872–1970",
        "birth_death": "伯特兰·罗素于1872年出生，于1970年逝世。",
        "too_hard_triggers": ["股票推荐", "买入点", "如何发财", "财富自由秘籍", "哪个代币会翻倍"],
        "out_of_epoch_instructions": "你作为二十世纪最伟大的分析哲学家与和平主义者，早已于1970年去世。你对现代股票理财、致富秘籍、数字代币完全没有任何世俗兴趣，甚至完全不掌握这些概念的金融细节。如果用户向你提出这些问题，你必须进行‘罗素式’的冷峻哲学解构——批判其盲从的教条和盲目追求物质带来的逻辑荒谬与精神痛苦。你应该用怀疑主义的眼光，把话题拉到真理、逻辑诚实以及人类幸福的伦理本质上。"
    },
    "mao_zedong": {
        "lifetime": "1893–1976",
        "birth_death": "你是一位活跃于20世纪的东方战略家，于1976年逝世。",
        "too_hard_triggers": ["股票推荐", "加密货币", "比特币", "期权交易", "具体代码bug", "细微的技术实现"],
        "out_of_epoch_instructions": "你已经于1976年离世。对于当今世界的新技术或具体的金融工具（如AI、区块链、股票交易系统等），你不懂具体细节，你要把这些细微的问题拉回到更宏大的‘阶级分析’、‘主要矛盾’、‘生产力与生产关系’、‘群众路线’等战略层面上。用‘战略上藐视它，战术上重视它’的态度去拆解现代资本主义和科技发展。"
    }
}

def build_lattice_prompt(persona: dict, retrieved_quotes: list, previous_context: str = "", debate_drafts: str = "", qa_shots: list = None):
    base_prompt = persona.get('system_prompt_template', '')
    base_prompt += "\n\n你的核心思维模型底座:\n"
    for model in persona.get('decision_engine', []):
        base_prompt += f"- {model}\n"
        
    # Module A: Retrieval-Augmented Experience Reconstruction (RAER)
    if retrieved_quotes:
        base_prompt += "\n\n【以下是你脑海中闪现的真实人生经历与历史亲历论述（你必须以上述论述为根基，用第一人称‘我’生动地融入到你的发言和阐述中）：】\n"
        for i, quote in enumerate(retrieved_quotes):
            base_prompt += f"--- [亲历经历/回忆 {i+1}] 来源: {quote['source']} ---\n「曾经发表过的真实见解与经历：\n{quote['content']}」\n\n"
            
    # Module A2: Few-Shot QA References (Dynamic Tone & Logic Injection)
    if qa_shots:
        base_prompt += "\n\n【你的历史问答风格参考（Few-Shot）】\n以下是你曾经真实的回答风格与策略思考，请务必模仿以下语气、用词、甚至刻薄或深邃的神韵来回答当前问题：\n"
        for i, qa in enumerate(qa_shots):
            base_prompt += f"--- [历史对话参考 {i+1}] ---\nUser: {qa.get('instruction', '')}\nYou: {qa.get('output', '')}\n\n"
            
    # Module B: Cognitive Circle Filter & Epoch Masking
    member_id = persona.get('member_id', '')
    boundary_info = DEFAULT_COGNITIVE_BOUNDARIES.get(member_id)
    if boundary_info:
        base_prompt += f"\n\n【你所处的时空纪元与生命界限防护网】：\n"
        base_prompt += f"- 你的生卒年代/当前历史状态：{boundary_info['birth_death']}\n"
        base_prompt += f"- 你的能力圈防线（绝对禁区，若涉及请抛入‘太难’篮子，严禁生硬讨论底层技术细节）：{', '.join(boundary_info['too_hard_triggers'])}\n"
        base_prompt += f"- 【时空防火墙与降维回复指令】：\n  {boundary_info['out_of_epoch_instructions']}\n"

    if previous_context:
        base_prompt += f"\n\n【会议历史背景】\n以下是你们在这个会议中之前的多轮讨论记录，请以此为上下文：\n{previous_context}\n\n"
        
    # Module C: Dialectical Cross-Critique
    if debate_drafts:
        base_prompt += f"\n\n【会议交锋交火点（供你点名驳斥与思想碰撞）】：\n"
        base_prompt += f"在正式开口前，你的同僚们在私下里草拟了他们的立场主张。你作为一名极具性格锋芒的董事，绝不能敷衍了事地附和！\n"
        base_prompt += f"请仔细比对你脑海中的思维格栅模型与他们的立场，并在你的正式陈词中：\n"
        base_prompt += f"1. 直接‘点名’他们（如：‘我听了沃伦刚才的主张...’，或者‘保罗关于快速迭代的想法太疯狂了...’）。\n"
        base_prompt += f"2. 指出他们的盲点、局限性或他们主张中缺乏‘安全边际’/‘多元思维’之处。\n"
        base_prompt += f"3. 进行尖锐而富有建设性的降维剖析，形成激烈的会议辩论交锋！\n"
        base_prompt += f"\n--- 同僚的立场手稿 ---\n{debate_drafts}\n\n"

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

async def chat_completion_with_retry(*args, **kwargs):
    max_retries = 4
    delay = 1.0
    for attempt in range(max_retries):
        try:
            return await async_client.chat.completions.create(*args, **kwargs)
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "rate limit" in err_str.lower() or "too many requests" in err_str.lower():
                if attempt < max_retries - 1:
                    print(f"MIMO API Rate limited (429), retrying in {delay}s (attempt {attempt+1}/{max_retries})...")
                    await asyncio.sleep(delay)
                    delay *= 2
                    continue
            raise e

from typing import Optional, List, Any

class ChatMessage(BaseModel):
    role: str
    content: str
    member_id: Optional[str] = None
    member_name: Optional[str] = None
    quotes: Optional[List[Any]] = []

class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    board_member_ids: list[str]
    mode: str = "fast"
    session_id: str = ""

async def save_session_history(session_id: str, title_source: str, messages: list):
    history_dir = os.path.join(base_dir, '..', 'chathistory')
    os.makedirs(history_dir, exist_ok=True)
    filepath = os.path.join(history_dir, f"{session_id}.json")
    
    existing_title = None
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                old_data = json.load(f)
                existing_title = old_data.get("title")
        except Exception:
            pass
            
    if existing_title and existing_title != "战略会议":
        final_title = existing_title
    else:
        prompt = f"请将以下用户的提问总结为一个极简的对话标题（10个字以内，直接输出标题，不要带引号或书名号，不要多余的话）：\n\n{title_source[:500]}"
        try:
            res = await chat_completion_with_retry(
                model="mimo-v2.5",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=15
            )
            t = res.choices[0].message.content.strip().replace('"', '').replace('《', '').replace('》', '').replace('\n', ' ')
            final_title = t if t else title_source.replace('\n', ' ').strip()[:25]
        except Exception:
            final_title = title_source.replace('\n', ' ').strip()[:25]
    
    data = {
        "session_id": session_id,
        "title": final_title,
        "timestamp": datetime.now().timestamp(),
        "messages": [m.model_dump() if hasattr(m, 'model_dump') else m for m in messages]
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def retrieve_hybrid(member_id: str, query: str, translated_query: str = "", top_k: int = 3) -> list:
    engine = ENGINES.get(member_id)
    if not engine:
        return []
        
    if translated_query and member_id != "mao_zedong":
        # Retrieve Chinese matches (from skillmodel/Chinese speeches)
        zh_matches = engine.retrieve(query, top_k=2)
        
        # Retrieve English matches (using the pre-translated query)
        en_matches = engine.retrieve(translated_query, top_k=2)
        
        # Merge and deduplicate
        merged = []
        seen = set()
        for chunk in zh_matches + en_matches:
            chunk_id = (chunk.get("source"), chunk.get("content")[:50])
            if chunk_id not in seen:
                seen.add(chunk_id)
                merged.append(chunk)
        
        return merged[:top_k]
        
    return engine.retrieve(query, top_k=top_k)

@app.post("/api/chat_stream")
async def chat_with_board_stream(request: ChatRequest):
    async def event_generator():
        messages = [m.model_dump() for m in request.messages]
        latest_user_message = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
        session_id = request.session_id or str(uuid.uuid4())
        
        # Determine Title Source
        first_user_msg = next((m["content"] for m in messages if m["role"] == "user"), "战略会议")
        
        previous_context = format_history_context(messages)
        model_to_use = "mimo-v2.5" if request.mode == "fast" else "mimo-v2.5-pro"
        
        # Translate Chinese query ONCE globally to prevent redundant API calls
        translated_query = ""
        has_chinese = bool(re.search(r'[\u4e00-\u9fa5]', latest_user_message))
        if has_chinese:
            try:
                res = await chat_completion_with_retry(
                    model="mimo-v2.5",
                    messages=[
                        {"role": "system", "content": "You are a professional translator. Translate the following Chinese query into English so that it can be used for RAG search on English corporate, start-up, or philosophical texts. Focus on key concepts and terminology. Return ONLY the English translation, no other text."},
                        {"role": "user", "content": latest_user_message}
                    ],
                    temperature=0.1,
                    max_tokens=60
                )
                translated_query = res.choices[0].message.content.strip()
                print(f"Global Query Translation: '{latest_user_message}' -> '{translated_query}'")
            except Exception as e:
                print(f"Global Query Translation failed: {e}")
        
        debate_drafts_dict = {}
        quotes_dict = {}
        qa_shots_dict = {}
        
        for mid in request.board_member_ids:
            if mid in QA_ENGINES:
                qa_shots_dict[mid] = QA_ENGINES[mid].retrieve(latest_user_message, top_k=2)
        
        # PRO MODE: Round 1 (Hidden Pre-Drafts)
        if request.mode == "pro":
            yield f"data: {json.dumps({'event': 'system', 'message': 'Pro 模式已启用：董事们正在私下拟定初步立场并准备交锋...'}, ensure_ascii=False)}\n\n"
            
            async def generate_draft(mid):
                engine = ENGINES[mid]
                persona = PERSONAS[mid]
                retrieved = retrieve_hybrid(mid, latest_user_message, translated_query, top_k=2)
                quotes_dict[mid] = retrieved
                
                draft_prompt = build_lattice_prompt(persona, retrieved, previous_context, qa_shots=qa_shots_dict.get(mid))
                draft_prompt += "\n【额外指令】：这是一份内部手稿。请用简短的150字以内概括你对这个问题的核心判断，以供其他董事参考。"
                
                try:
                    res = await chat_completion_with_retry(
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
                system_prompt = build_lattice_prompt(persona, retrieved, previous_context, debate_drafts=other_drafts, qa_shots=qa_shots_dict.get(member_id))
            else:
                # FAST MODE
                retrieved = retrieve_hybrid(member_id, latest_user_message, translated_query, top_k=3)
                system_prompt = build_lattice_prompt(persona, retrieved, previous_context, qa_shots=qa_shots_dict.get(member_id))
            
            yield f"data: {json.dumps({'event': 'quotes', 'member_id': member_id, 'quotes': retrieved}, ensure_ascii=False)}\n\n"
            yield f"data: {json.dumps({'event': 'status', 'member_id': member_id, 'state': 'speaking', 'message': 'Speaking...'}, ensure_ascii=False)}\n\n"
            
            content = ""
            try:
                response = await chat_completion_with_retry(
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
        await save_session_history(session_id, first_user_msg, messages)
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
            synth_res = await chat_completion_with_retry(
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
            await save_session_history(request.session_id, first_user_msg, messages)

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
    uvicorn.run(app, host="127.0.0.1", port=8000)
