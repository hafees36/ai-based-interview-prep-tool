import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.1-8b-instant"


def call_followup_llm(prompt, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature
    }

    response = requests.post(GROQ_URL, headers=headers, json=data)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

def generate_follow_up(question, answer):

    prompt = f"""
You are a strict technical interviewer.

Original Question:
{question}

Candidate Answer:
{answer}

Your task:
Ask ONE intelligent follow-up question to test deeper understanding.

Rules:
- Only ask the question.
- Do not explain.
- Keep it technical.
- Do not repeat the original question.
- Ask only one follow-up question.
"""

    return call_followup_llm(prompt)