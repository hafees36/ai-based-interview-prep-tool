#  AI Based Interview Preparation Tool

An AI-powered interview preparation platform that helps candidates improve their interview skills through resume analysis, personalized technical questions, mock interviews, and AI-generated feedback.

## 📌 Features

### 📄 Resume Analysis
- Upload your resume (PDF).
- Extracts skills automatically.
- Identifies the most suitable job role using AI.
- Finds missing skills required for the selected role.

### ❓ Personalized Interview Questions
- Generates role-specific MCQ interview questions.
- Questions are based on:
  - Skills already present in the resume.
  - Missing skills to improve.

### 🎤 AI Mock Interview
- Conducts an interactive mock interview.
- Generates intelligent follow-up questions based on candidate responses.
- Simulates a real technical interview experience.

### 📊 AI Answer Evaluation
- Evaluates candidate answers.
- Provides:
  - Score
  - Correct Answer
  - Result (Correct/Incorrect)
  - Brief Explanation

### 🤖 AI-Powered Role Detection
- Identifies the most suitable job role from the uploaded resume using Groq LLM.

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Vite
- JavaScript
- Tailwind CSS
- HTML5
- CSS3

## Backend
- FastAPI
- Python

## AI & Machine Learning
- Groq API (Llama 3.1 8B Instant)
- spaCy
- NLP
- Prompt Engineering

## Other Libraries
- PyPDF2
- Requests
- Uvicorn
- python-dotenv

---

# 📂 Project Structure

```
AI-Interview-Preparation-Tool
│
├── backend
│   ├── modules
│   │   ├── llm_module.py
│   │   ├── followup_llm.py
│   │   ├── role_extraction.py
│   │   ├── resume_parser.py
│   │   ├── skill_extraction.py
│   │   └──skill_gap.py
│   │   └──speech_to_text.py
│   │   └──video_monitor.py
│   │
│   ├── app.py
│   └── requirements.txt
│
├── src
├── public
├── package.json
└── README.md
```

# 🧠 Workflow

1. Upload Resume
2. Resume Parsing
3. Skill Extraction
4. AI Role Detection
5. Skill Gap Analysis
6. Generate Interview Questions
7. Mock Interview
8. AI Answer Evaluation
9. AI Follow-up Questions

---

# 🔮 Future Enhancements

- Voice-based interview
- Video interview support
- Facial expression analysis
- Performance analytics dashboard
- Interview history tracking
- Leaderboard and progress reports

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository and submit a pull request.

---

# 📄 License

This project is developed for educational and learning purposes.

---

# 👨‍💻 Author

**Hafees Muhammed V A**

B.Tech in Artificial Intelligence & Data Science

GitHub: https://github.com/hafees36

LinkedIn: https://www.linkedin.com/in/hafees-muhammed-v-a-95b947297/
