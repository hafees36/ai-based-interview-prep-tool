from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os

from modules.resume_parser import extract_text_from_pdf
from modules.role_extraction import extract_role
from modules.skill_extraction import extract_skills
from modules.skill_gap import analyze_skill_gap
from modules.llm_module import generate_questions, evaluate_answer
from modules.followup_llm import generate_follow_up
from modules.speech_to_text import listen_from_mic

app = FastAPI(title="AI Interview Preparation System")
# Enable CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -----------------------------
# Job Role Skill Database
# -----------------------------
job_roles = {
    "Software Developer": ["DSA", "Java", "System Design"],
    "Data Scientist": ["Python", "Machine Learning", "Statistics"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React"],
    "Backend Developer": ["Node.js", "Java", "SQL"],
    "AI / ML Engineer": ["Deep Learning", "TensorFlow", "NLP"]
}


# Request model
class RoleRequest(BaseModel):
    role: str


# -----------------------------
# Resume Analysis API
# -----------------------------
@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    if not resume_text:
        return {"error": "Could not extract resume text"}

    role = extract_role(resume_text)
    skills = extract_skills(resume_text)

    gap_result = analyze_skill_gap(role.lower(), skills)

    return {
        "role": role,
        "skills": skills,
        "matched_skills": gap_result["matched_skills"],
        "missing_skills": gap_result["missing_skills"],
        "coverage_percentage": gap_result["coverage_percentage"]
    }

@app.get("/voice-input")
async def voice_input():

    text = listen_from_mic()

    return {"text": text}

@app.post("/follow-up-question")
async def follow_up_question_api(data: dict):

    question = data.get("question")
    answer = data.get("answer")

    follow_up = generate_follow_up(question, answer)

    return {"follow_up": follow_up}
# -----------------------------
# Job Role Selection API
# -----------------------------
@app.post("/select-role")
async def select_role(data: RoleRequest):

    role = data.role

    skills = job_roles.get(role, [])

    return {
        "role": role,
        "skills": skills,
        "matched_skills": [],
        "missing_skills": skills,
        "coverage_percentage": 0
    }


# -----------------------------
# Generate Interview Questions
# -----------------------------
@app.post("/generate-questions")
async def generate_questions_api(data: dict):

    role = data.get("role")
    matched_skills = data.get("matched_skills")
    missing_skills = data.get("missing_skills")

    questions = generate_questions(role, matched_skills, missing_skills)

    return {"questions": questions}


# -----------------------------
# Evaluate Answer
# -----------------------------
@app.post("/evaluate-answer")
async def evaluate_answer_api(data: dict):

    question = data.get("question")
    answer = data.get("answer")

    if not question or not answer:
        return {"error": "Question and Answer required"}

    feedback = evaluate_answer(question, answer)

    return {"feedback": feedback}