#!/usr/bin/env python3
"""
Patched runner for the Munger dataset curator that adds retry logic with
exponential backoff to handle 429 rate limit errors from the MIMO API.
"""
import os
import json
import sys
import asyncio
import time
import random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# First, clean up checkpoint: remove empty entries so they get retried
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
checkpoint_file = os.path.join(BASE_DIR, "munger_checkpoint.json")
output_jsonl = os.path.join(BASE_DIR, "munger_qa_dataset.jsonl")

if os.path.exists(checkpoint_file):
    with open(checkpoint_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    empty_keys = [k for k, v in data.items() if not v]
    non_empty_keys = [k for k, v in data.items() if v]

    print(f"Checkpoint has {len(data)} entries: {len(non_empty_keys)} with QA, {len(empty_keys)} empty (failed)")

    for k in empty_keys:
        del data[k]

    with open(checkpoint_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Cleaned checkpoint: removed {len(empty_keys)} empty entries, {len(data)} entries remain.")

    with open(output_jsonl, 'w', encoding='utf-8') as out_f:
        for chunk_id, qa_pairs in data.items():
            for pair in qa_pairs:
                out_f.write(json.dumps(pair, ensure_ascii=False) + "\n")
    print(f"Rebuilt {output_jsonl} from checkpoint.")

from dataset_curator import DatasetCurator
from openai import RateLimitError, APIError, APITimeoutError

MAX_RETRIES = 5
BASE_DELAY = 2.0

async def retry_api_call(coro_func, chunk_id, call_type="API"):
    for attempt in range(MAX_RETRIES):
        try:
            return await coro_func()
        except RateLimitError as e:
            delay = BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
            print(f"  [RateLimit] {call_type} for {chunk_id}: attempt {attempt+1}/{MAX_RETRIES}, waiting {delay:.1f}s...")
            await asyncio.sleep(delay)
        except (APIError, APITimeoutError) as e:
            if attempt < MAX_RETRIES - 1:
                delay = BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
                print(f"  [APIError] {call_type} for {chunk_id}: attempt {attempt+1}/{MAX_RETRIES}, waiting {delay:.1f}s...")
                await asyncio.sleep(delay)
            else:
                print(f"  [FAILED] {call_type} for {chunk_id} after {MAX_RETRIES} attempts: {e}")
                raise
        except Exception as e:
            print(f"  [ERROR] {call_type} for {chunk_id}: {e}")
            raise
    return None

original_generate_questions = DatasetCurator.generate_questions
original_generate_answer = DatasetCurator.generate_answer
original_process_chunk = DatasetCurator.process_chunk

async def patched_generate_questions(self, chunk):
    result = await retry_api_call(
        lambda: original_generate_questions(self, chunk),
        chunk['id'], "Q-Gen"
    )
    return result if result else [f"Regarding {chunk['source']} from {chunk['year']}, can you discuss the business logic?"]

async def patched_generate_answer(self, chunk, question):
    result = await retry_api_call(
        lambda: original_generate_answer(self, chunk, question),
        chunk['id'], "A-Synth"
    )
    return result if result else ""

async def patched_process_chunk(self, chunk, semaphore, dry_run=False):
    async with semaphore:
        chunk_id = chunk["id"]
        if chunk_id in self.processed_chunks and not dry_run:
            return self.processed_chunks[chunk_id]

        print(f"[{self.agent_name}] Generating QA for Chunk: {chunk_id}...")
        await asyncio.sleep(1.5)

        questions = await patched_generate_questions(self, chunk)

        qa_pairs = []
        for q in questions:
            await asyncio.sleep(1.0)
            answer = await patched_generate_answer(self, chunk, q)
            if answer and len(answer) > 30:
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
            if qa_pairs:
                self.processed_chunks[chunk_id] = qa_pairs
                self.save_checkpoint()
                with open(self.output_jsonl, 'a', encoding='utf-8') as out_f:
                    for pair in qa_pairs:
                        out_f.write(json.dumps(pair, ensure_ascii=False) + "\n")
            else:
                print(f"  [WARN] No valid QA pairs for {chunk_id}, skipping checkpoint save.")

        return qa_pairs

DatasetCurator.generate_questions = patched_generate_questions
DatasetCurator.generate_answer = patched_generate_answer
DatasetCurator.process_chunk = patched_process_chunk

CONCURRENCY = 2

print(f"\n=== Starting Munger Dataset Curator (with retry) ===")
print(f"Concurrency: {CONCURRENCY}, Max retries: {MAX_RETRIES}, Base delay: {BASE_DELAY}s\n")

curator = DatasetCurator(member="munger", concurrency=CONCURRENCY)
asyncio.run(curator.run())
