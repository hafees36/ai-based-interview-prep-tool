from modules.resume_parser import extract_text_from_pdf
from modules.skill_extraction import extract_skills
from modules.role_extraction import extract_role
from modules.skill_gap import analyze_skill_gap
from modules.llm_module import generate_questions, evaluate_answer

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("sample_resume.pdf")
    skills = extract_skills(resume_text)
    
    print("\n===== EXTRACTED RESUME TEXT =====")
    print(resume_text)

    print("\n===== EXTRACTED RESUME SKILLS =====")
    print(skills)

    print("\n===== IDENTIFIED ROLE =====\n")
    print(extract_role(resume_text))
    

    role = extract_role(resume_text)
    gap_result = analyze_skill_gap(role, skills)
    print("\n===== SKILL GAP ANALYSIS =====")
    print("Matched Skills:", gap_result["matched_skills"])
    print("Missing Skills:", gap_result["missing_skills"])
    print("Coverage %:", gap_result["coverage_percentage"])

    print("\n===== GENERATED INTERVIEW QUESTIONS =====\n")
    questions = generate_questions(
        role,
        gap_result["matched_skills"],
        gap_result["missing_skills"]
    )
    print(questions)

    print("\n===== TYPE YOUR ANSWER =====\n")
    user_answer = input("Type your answer here:\n")
    feedback = evaluate_answer(questions, user_answer)

    print("\n===== ANSWER EVALUATION & AI FEEDBACK =====\n")
    first_question = questions.split("\n")[0]
    feedback = evaluate_answer(first_question, user_answer)
    print(feedback)