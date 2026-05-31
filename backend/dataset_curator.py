import os
import json
import re
import sys
import asyncio
import argparse
import yaml
from typing import List, Dict
from dotenv import load_dotenv
from openai import AsyncOpenAI
import random

# Force UTF-8 encoding on Windows console outputs to prevent Mojibake
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Load env variables from backend/.env
load_dotenv()

MIMO_API_KEY = os.getenv("MIMO_API_KEY", "")
MIMO_BASE_URL = os.getenv("MIMO_BASE_URL", "https://token-plan-cn.xiaomimimo.com/v1")
DEFAULT_MODEL = "mimo-v2.5"  # Highly efficient model for data generation

if not MIMO_API_KEY:
    print("WARNING: MIMO_API_KEY is not set. Please set it in backend/.env or your system environment variables.")

async def retry_with_backoff(func, max_retries=10, base_delay=3.0, max_delay=120.0):
    """Retry an async function with exponential backoff on 429/rate-limit errors."""
    for attempt in range(max_retries):
        try:
            result = await func()
            # Post-success delay to smooth out request bursts
            await asyncio.sleep(0.3)
            return result
        except Exception as e:
            error_str = str(e)
            is_rate_limit = "429" in error_str or "rate" in error_str.lower() or "limit" in error_str.lower()
            is_transient = "500" in error_str or "502" in error_str or "503" in error_str or "timeout" in error_str.lower()

            if (is_rate_limit or is_transient) and attempt < max_retries - 1:
                delay = min(base_delay * (2 ** attempt) + random.uniform(0, 3), max_delay)
                print(f"  [Retry {attempt+1}/{max_retries}] Rate limited or transient error, waiting {delay:.1f}s...")
                await asyncio.sleep(delay)
            else:
                raise
    return None

# Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = os.path.join(BASE_DIR, '..', 'agents')
CORPUS_BASE_DIR = os.path.join(BASE_DIR, '..', 'board of directors')

# Mapping for members
MEMBER_CONFIGS = {
    "munger": {
        "folder": "CharlieMungerTalk-master",
        "agent_name": "Charlie Munger",
        "persona_file": "munger/persona.yaml"
    },
    "buffett": {
        "folder": "Warren Buffett",
        "agent_name": "Warren Buffett",
        "persona_file": "buffett/persona.yaml"
    },
    "paul_graham": {
        "folder": "Paul Graham",
        "agent_name": "Paul Graham",
        "persona_file": "paul_graham/persona.yaml"
    },
    "russell": {
        "folder": "russiu",
        "agent_name": "Bertrand Russell",
        "persona_file": "russell/persona.yaml"
    },
    "mao_zedong": {
        "folder": "Mao Zedong",
        "agent_name": "Mao Zedong",
        "persona_file": "mao_zedong/persona.yaml"
    }
}

class DatasetCurator:
    def __init__(self, member: str, concurrency: int = 3, model: str = DEFAULT_MODEL):
        self.member = member
        self.concurrency = concurrency
        self.model = model
        
        config = MEMBER_CONFIGS.get(member)
        if not config:
            raise ValueError(f"Unknown member '{member}'. Choose from: {list(MEMBER_CONFIGS.keys())}")
            
        self.agent_name = config["agent_name"]
        self.corpus_path = os.path.join(CORPUS_BASE_DIR, config["folder"])
        self.persona_path = os.path.join(AGENTS_DIR, config["persona_file"])
        
        # Load persona rules
        self.persona = self.load_persona()
        self.client = AsyncOpenAI(api_key=MIMO_API_KEY, base_url=MIMO_BASE_URL)
        
        # Files for saving progress
        self.checkpoint_file = os.path.join(BASE_DIR, f"{member}_checkpoint.json")
        self.output_jsonl = os.path.join(BASE_DIR, f"{member}_qa_dataset.jsonl")
        
        # Per-process rate limiter: max 1 concurrent API call
        self.api_semaphore = asyncio.Semaphore(1)
        # Minimum delay between API calls (seconds) to avoid burst rate limits
        self.api_delay = 3.0

        self.processed_chunks = {}
        self.load_checkpoint()

    def load_persona(self) -> Dict:
        if os.path.exists(self.persona_path):
            with open(self.persona_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return {"name": self.agent_name, "system_prompt_template": "", "decision_engine": []}

    def load_checkpoint(self):
        if os.path.exists(self.checkpoint_file):
            try:
                with open(self.checkpoint_file, 'r', encoding='utf-8') as f:
                    self.processed_chunks = json.load(f)
                print(f"Loaded checkpoint file. {len(self.processed_chunks)} chunks already processed.")
            except Exception as e:
                print(f"Error loading checkpoint, starting fresh: {e}")

    def save_checkpoint(self):
        with open(self.checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(self.processed_chunks, f, ensure_ascii=False, indent=2)

    def extract_year(self, filepath: str, filename: str) -> str:
        """
        Extract the year from file path or file name.
        """
        # Search for 4 consecutive digits in filename first
        match = re.search(r'\d{4}', filename)
        if match:
            return match.group(0)
        # Search in relative path from corpus directory to avoid absolute path username matching
        try:
            rel_path = os.path.relpath(filepath, self.corpus_path)
            match = re.search(r'\d{4}', rel_path)
            if match:
                return match.group(0)
        except Exception:
            pass
        return "Unknown Year"

    def clean_text(self, text: str) -> str:
        # Strip frontmatter
        text = re.sub(r'^---.*?---', '', text, flags=re.DOTALL)
        # Remove markdown image tags or links
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
        return text.strip()

    def chunk_file(self, filepath: str, filename: str) -> List[Dict]:
        """
        Read file and split into logical chunks of 500-1000 characters.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='gbk') as f:
                    content = f.read()
            except Exception:
                return []

        content = self.clean_text(content)
        paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
        
        chunks = []
        current_chunk = []
        current_len = 0
        year = self.extract_year(filepath, filename)
        source = filename.replace(".md", "").replace(".txt", "").replace("-", " ")
        
        for para in paragraphs:
            # Skip very short lines or markdown placeholders
            if len(para) < 20 and ("layout:" in para or "categories:" in para or "---" in para):
                continue
                
            para_len = len(para)
            if current_len + para_len > 2000 and current_chunk:
                chunks.append({
                    "content": "\n".join(current_chunk),
                    "source": source,
                    "year": year,
                    "id": f"{source}_{len(chunks)}"
                })
                current_chunk = [para]
                current_len = para_len
            else:
                current_chunk.append(para)
                current_len += para_len
                
        if current_chunk:
            chunks.append({
                "content": "\n".join(current_chunk),
                "source": source,
                "year": year,
                "id": f"{source}_{len(chunks)}"
            })
            
        return chunks

    def scan_corpus(self) -> List[Dict]:
        """
        Scan all subdirectories recursively for markdown and text files.
        """
        if not os.path.exists(self.corpus_path):
            print(f"Error: Corpus path '{self.corpus_path}' not found.")
            return []

        all_chunks = []
        for root, _, files in os.walk(self.corpus_path):
            for file in files:
                # Skip giant compiled files to prevent massive 2x duplication of the entire corpus
                if file.lower() in ["graham.md", "charlie_munger_talks.md", "mungertalks.md"]:
                    continue
                if file.endswith(".md") or file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    file_chunks = self.chunk_file(file_path, file)
                    all_chunks.extend(file_chunks)
                    
        print(f"Scanned corpus. Total files processed: {len(all_chunks)} chunks generated.")
        return all_chunks

    def filter_response(self, text: str) -> str:
        """
        Strict filter to remove bracketed action words and formatting.
        - Removes: (笑), (缓缓坐下), (沉默片刻), *sigh*, (身体前倾)
        - Translates third person references to first person if needed (done by prompt, backup here)
        """
        # Remove parenthesized action indicators
        text = re.sub(r'[\(\*（【][^\)\*）】]+[\)\*）】]', '', text)
        # Remove leading/trailing quotes and spacing
        text = text.strip().strip('"').strip('「').strip('」')
        return text.strip()

    def parse_json_list(self, text: str) -> List[str]:
        # Try direct load first
        try:
            content = text.strip()
            content = re.sub(r'^```json\s*', '', content)
            content = re.sub(r'^```\s*', '', content)
            content = re.sub(r'\s*```$', '', content)
            return json.loads(content)
        except Exception:
            pass
            
        # Try to find a JSON list pattern [...]
        match = re.search(r'\[\s*".*?"\s*\]', text, re.DOTALL)
        if not match:
            match = re.search(r'\[.*\]', text, re.DOTALL)
            
        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                pass
                
        # If all JSON parsing fails, extract everything in double quotes
        lines = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', text)
        if lines:
            return [l.strip() for l in lines if len(l.strip()) > 5]
            
        # Fallback split by numbering (e.g. 1. 2. 3.)
        questions = []
        for line in text.split("\n"):
            line = line.strip()
            line_match = re.match(r'^(?:\d+[\.、\s]|-|\*)\s*(.+)$', line)
            if line_match:
                questions.append(line_match.group(1).strip())
                
        if questions:
            return questions
            
        return []

    async def generate_questions(self, chunk: Dict) -> List[str]:
        """
        Stage 1: Q-Gen
        Read the chunk and generate 3 realistic, contextually relevant questions.
        """
        prompt = f"""【角色设定】
你现在是世界上最顶尖、最敏锐的财经记者和风险投资家。你正在现场参加【{self.agent_name}】的私人战略闭门会。

【任务】
请仔细阅读以下提供的【历史真实文献片段】（时间定位为 {chunk['year']} 年）。基于这段文献所蕴含的商业本质、投资逻辑或思考模型，设计出3个极其自然、深刻且有挑战性的用户提问。

【提问设计规范】
1. 提问口吻必须像一个真正的创业者、CEO或董事会同僚在向【{self.agent_name}】请教现实决策。
2. 避免直接出现“根据这段文字中说的...”这种机械词汇。提问应当是情境化的、面向现实商业问题的。
3. 3个问题应具备多样性：
   - 问题1：直接请教该文献中提到的核心概念（例如：如何判断护城河是否变宽？）。
   - 问题2：将该逻辑应用到一个假想的现代商业冲突情境中进行提问。
   - 问题3：带有挑战或质疑意味的提问，逼迫【{self.agent_name}】阐述其底层原则。

【历史真实文献片段】
{chunk['content']}

【输出格式】
只输出一个标准的 JSON List 格式，严禁包含任何 Markdown 格式包裹（不要用 ```json）：
[
  "问题1的具体内容...",
  "问题2的具体内容...",
  "问题3的具体内容..."
]"""

        try:
            async def _call():
                async with self.api_semaphore:
                    res = await self.client.chat.completions.create(
                        model=self.model,
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.6,
                        max_tokens=500
                    )
                    return res.choices[0].message.content.strip()

            content = await retry_with_backoff(_call)

            questions = self.parse_json_list(content)
            if isinstance(questions, list) and len(questions) > 0:
                return [q.strip() for q in questions[:3]]
        except Exception as e:
            print(f"Error generating questions for chunk {chunk['id']}: {e}")

        # Fallback question if generation fails
        return [f"关于您在 {chunk['year']} 年提到的《{chunk['source']}》，您能具体谈谈其中的商业逻辑吗？"]

    async def generate_answer(self, chunk: Dict, question: str) -> str:
        """
        Stage 2: A-Synth
        Generate a first-person answer that strictly represents the persona.
        """
        base_prompt = self.persona.get('system_prompt_template', '')
        base_prompt += "\n\n你的核心思维模型底座:\n"
        for model in self.persona.get('decision_engine', []):
            base_prompt += f"- {model}\n"

        prompt = f"""{base_prompt}

【人格附身与本源事实】：
- 你的历史真实文献参考（时间定位：{chunk['year']} 年，出自《{chunk['source']}》）：
「
{chunk['content']}
」

【用户向你提出的问题】：
{question}

【任务】
请基于【历史真实文献参考】所表达的真实观点，针对【用户提出的问题】给出一份精彩的第一人称回答。

【极其严苛的输出约束（违反任何一条则数据作废）】
1. 必须使用第一人称「我」。严禁出现“根据这段论述”或“芒格/巴菲特认为”等出戏的第三人称字眼。你的身体已经和灵魂融为一体！
2. 语言必须高度口语化、犀利、老派。多用你特有的标志性词汇和讲故事节奏。
3. 绝对禁止输出任何肢体动作、舞台旁白、情绪或动作场景描写（严禁包含任何括号或星号内的词汇，如：(喝了一口可乐)、*缓缓放下手中的笔*、(笑) 等）。你必须直接陈述核心见解。
4. 表达结构：先给出一个辛辣直白的结论或故事引入，然后用你的心智模型进行降维解释。
5. 答案必须紧密围绕【历史真实文献参考】的本质逻辑，不允许产生违背事实的胡编乱造。

【你的回答】："""

        try:
            async def _call():
                async with self.api_semaphore:
                    res = await self.client.chat.completions.create(
                        model=self.model,
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7,
                        max_tokens=1000
                    )
                    return res.choices[0].message.content.strip()

            raw_answer = await retry_with_backoff(_call)
            return self.filter_response(raw_answer)
        except Exception as e:
            print(f"Error generating answer for chunk {chunk['id']}: {e}")
            return ""

    async def process_chunk(self, chunk: Dict, semaphore: asyncio.Semaphore, dry_run: bool = False) -> List[Dict]:
        async with semaphore:
            # Delay between chunks to avoid API rate limits
            await asyncio.sleep(0.3)
            chunk_id = chunk["id"]
            if chunk_id in self.processed_chunks and not dry_run:
                # Retrieve from checkpoint
                return self.processed_chunks[chunk_id]

            print(f"[{self.agent_name}] Generating QA for Chunk: {chunk_id}...")
            
            # Step 1: Q-Gen
            questions = await self.generate_questions(chunk)
            
            qa_pairs = []
            # Step 2: A-Synth for each question
            for q in questions:
                answer = await self.generate_answer(chunk, q)
                if answer and len(answer) > 30:
                    # Construct instruction data (Alpaca format)
                    qa_pairs.append({
                        "instruction": q,
                        "input": "",
                        "output": answer,
                        "meta": {
                            "source": chunk["source"],
                            "year": chunk["year"],
                            "character": self.agent_name
                        }
                    })
                    
            if not dry_run:
                self.processed_chunks[chunk_id] = qa_pairs
                self.save_checkpoint()
                
                # Write directly to output_jsonl file line by line
                with open(self.output_jsonl, 'a', encoding='utf-8') as out_f:
                    for pair in qa_pairs:
                        out_f.write(json.dumps(pair, ensure_ascii=False) + "\n")
                        
            return qa_pairs

    async def run(self, limit: int = None, dry_run: bool = False):
        chunks = self.scan_corpus()
        if not chunks:
            print("No chunks found. Exiting.")
            return

        if limit:
            chunks = chunks[:limit]
            print(f"Limiting execution to {limit} chunks.")

        if dry_run:
            print("\n=== DRY RUN MODE ENABLED ===")
            print("QA pairs will be displayed in console but not saved to disk.\n")

        semaphore = asyncio.Semaphore(self.concurrency)
        tasks = [self.process_chunk(chunk, semaphore, dry_run) for chunk in chunks]
        
        results = await asyncio.gather(*tasks)
        total_qa_count = sum(len(r) for r in results)
        
        print("\n==============================================")
        print(f"Finished processing! Generated {total_qa_count} total QA pairs.")
        
        if dry_run:
            print("\n=== SAMPLE GENERATIONS ===")
            sample_count = 0
            for r in results:
                for qa in r:
                    print(f"\n[Q]: {qa['instruction']}")
                    print(f"[A]: {qa['output']}")
                    print(f"[Metadata]: {qa['meta']}")
                    print("-" * 50)
                    sample_count += 1
                    if sample_count >= 3:
                        break
                if sample_count >= 3:
                    break
        else:
            print(f"Saved dataset file to: {self.output_jsonl}")
            print(f"Saved progress checkpoint to: {self.checkpoint_file}")
        print("==============================================")


def main():
    parser = argparse.ArgumentParser(description="Automatical Curation & Personality Synthesis Pipeline")
    parser.add_argument("--member", type=str, required=True, choices=list(MEMBER_CONFIGS.keys()), 
                        help="Member ID: 'munger', 'buffett', 'paul_graham', 'russell', 'mao_zedong'")
    parser.add_argument("--limit", type=int, default=None, 
                        help="Limit total chunks to process (useful for short runs or dry-runs)")
    parser.add_argument("--concurrency", type=int, default=3, 
                        help="Concurrency limit for API requests (default 3)")
    parser.add_argument("--dry-run", action="store_true", 
                        help="Preview generation results without saving checkpoints or files")
    
    args = parser.parse_args()
    
    curator = DatasetCurator(member=args.member, concurrency=args.concurrency)
    asyncio.run(curator.run(limit=args.limit, dry_run=args.dry_run))

if __name__ == "__main__":
    main()
