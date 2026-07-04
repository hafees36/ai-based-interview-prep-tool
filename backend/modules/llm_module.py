import os
import json
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.1-8b-instant"


def call_llm(prompt, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": temperature
    }

    response = requests.post(GROQ_URL, headers=headers, json=data)
    response.raise_for_status()

    result = response.json()
    return result["choices"][0]["message"]["content"]


# -------------------------------
# Generate Interview Questions
# -------------------------------
def generate_questions(role, matched_skills, missing_skills):

    prompt = f"""
Generate exactly 10 interview MCQ questions for the role: {role}

Requirements:
- 5 questions from matched skills: {matched_skills}
- 5 questions from missing skills: {missing_skills}
- Each question must have exactly 4 options
- correct must be option index (0,1,2,3)

STRICT RULES:
- Return ONLY valid JSON
- No markdown
- No explanations
- No text outside JSON

Return format:
[
  {{
    "question": "What is Python?",
    "options": [
      "Programming Language",
      "Database",
      "Operating System",
      "Web Browser"
    ],
    "correct": 0
  }}
]
"""

    content = call_llm(prompt, temperature=0.3)

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return []


# -------------------------------
# Evaluate Answer
# -------------------------------
def evaluate_answer(question, answer):

    prompt = f"""
You are a strict technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Return EXACTLY:

Score: X/10
Correct Answer: (answer)
Result: Correct / Incorrect
Brief Explanation: (1-2 lines)
"""

    return call_llm(prompt)