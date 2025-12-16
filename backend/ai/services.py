import os
from openai import OpenAI

client = None
api_key = os.getenv('OPENAI_API_KEY', '')
if api_key:
    client = OpenAI(api_key=api_key)

def ensure_client():
    if not client:
        raise RuntimeError('OPENAI_API_KEY missing')

def summarize_text(text):
    ensure_client()
    completion = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role':'system','content':'你是中文笔记助手，输出简短摘要和5-10个关键词。'},{'role':'user','content':text}])
    return completion.choices[0].message.content

def enhance_text(text):
    ensure_client()
    completion = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role':'system','content':'保持原意，提升可读性与简练度，保留术语。'},{'role':'user','content':text}])
    return completion.choices[0].message.content