import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.1-8b-instant"

ALLOWED_ROLES = [
    "Data Scientist",
    "Data Analyst",
    "Business Analyst",
    "AI Engineer",
    "AI/ML Engineer",
    "Machine Learning Engineer",
    "Deep Learning Engineer",
    "NLP Engineer",
    "Computer Vision Engineer",

    "Software Engineer",
    "Software Development Engineer",  
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "Web Developer",
    "Mobile Developer",
    "Android Developer",
    "iOS Developer",

    "DevOps Engineer",
    "Cloud Engineer",
    "Site Reliability Engineer",
    "Cybersecurity Analyst",
    "Network Engineer",
    "System Administrator",

    "Database Administrator",
    "Database Developer",

    "QA Engineer",
    "Test Engineer",
    "Automation Test Engineer",

    "UI/UX Designer",
    "Product Designer",

    "Product Manager",
    "Project Manager",
    "Scrum Master",

    "HR Manager",
    "Recruiter",
    "Digital Marketing Specialist",
    "SEO Specialist",
    "Content Strategist",
    "Sales Manager",

    "Mechanical Engineer",
    "Civil Engineer",
    "Electrical Engineer",
    "Electronics Engineer",
    "Embedded Systems Engineer",
    "Robotics Engineer",

    "Accountant",
    "Financial Analyst",

    "Research Scientist",
    "Technical Support Engineer"
]


def extract_role(resume_text):

    prompt = f"""
Analyze the following resume text and identify the most suitable job role.

Choose ONLY ONE role from this list:
{", ".join(ALLOWED_ROLES)}

Rules:
- Return ONLY the exact role name.
- No explanation.
- No extra text.

Resume:
{resume_text}
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0
    }

    try:
        response = requests.post(
            GROQ_URL,
            headers=headers,
            json=payload
        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print("LLM Error:", e)
        return "Role Not Identified"


if __name__ == "__main__":

    sample_resume = """
    Experienced Machine Learning Engineer with Python,
    TensorFlow, SQL, NLP, Deep Learning and FastAPI.
    """

    detected_role = extract_role(sample_resume)
    print("Detected Role:", detected_role)