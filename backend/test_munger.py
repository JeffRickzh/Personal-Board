import os
import yaml
from openai import OpenAI

# 配置小米 MiMo 模型的 API (兼容 OpenAI SDK)
# Note: The exact base_url for Xiaomi MiMo API might vary. Adjust if necessary.
MIMO_API_KEY = "sk-cqwylmqq1varypuqxu5q8xr8keffipl8ivsn71ojyk91btgp"
MIMO_BASE_URL = "https://api.xiaomimimo.com/v1" # Please replace with actual URL if different
MODEL_NAME = "mimo-v2.5" # 假设使用最新的 mimo 模型

def load_persona(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def build_system_prompt(persona):
    prompt = persona['system_prompt_template']
    prompt += "\n\nYour Mental Models:\n"
    for model in persona['decision_engine']:
        prompt += f"- {model}\n"
    return prompt

def test_munger_agent():
    # Load Persona
    persona_path = os.path.join(os.path.dirname(__file__), '..', 'agents', 'charlie_munger', 'persona.yaml')
    persona = load_persona(persona_path)
    system_prompt = build_system_prompt(persona)
    
    print(f"--- Loaded Persona: {persona['name']} ---")
    
    # Init Client
    client = OpenAI(
        api_key=MIMO_API_KEY,
        base_url=MIMO_BASE_URL,
    )
    
    user_query = "我想辞职去创业做一个全新的AI社交APP，但我没有任何经验，你觉得这个想法怎么样？"
    print(f"\nUser Query: {user_query}")
    print("\n--- Charlie Munger is thinking... ---")
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0.7,
            max_tokens=1000,
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"\nAPI Error: {e}")
        print("提示: 可能是 MIMO_BASE_URL 或 MODEL_NAME 不正确，请参考小米开发者文档进行替换。")

if __name__ == "__main__":
    test_munger_agent()
