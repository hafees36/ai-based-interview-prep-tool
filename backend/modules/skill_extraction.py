import spacy    
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

SKILL_DB = [

    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "go", "rust", "r", "matlab", "kotlin", "swift", "php", "dart",

    # Web Technologies
    "html", "css", "bootstrap", "tailwind", "react", "angular",
    "vue", "nextjs", "jquery",

    # Backend Frameworks
    "nodejs", "express", "django", "flask", "fastapi",
    "spring boot", "asp.net", "laravel",

    # Databases
    "sql", "mysql", "postgresql", "mongodb", "oracle",
    "sqlite", "redis", "firebase", "cassandra", "dynamodb",

    # Data Science / AI / ML
    "machine learning", "deep learning", "ml", "ai",
    "data science", "data analysis", "statistics",
    "probability", "linear algebra", "predictive modeling",
    "feature engineering", "model deployment",

    # ML Libraries
    "tensorflow", "pytorch", "keras", "scikit-learn",
    "xgboost", "lightgbm", "catboost", "opencv",

    # Data Libraries
    "pandas", "numpy", "matplotlib", "seaborn",
    "plotly", "scipy",

    # NLP / LLM
    "nlp", "spacy", "nltk", "transformers",
    "bert", "gpt", "llm", "langchain",
    "hugging face", "tokenization", "prompt engineering",

    # Computer Vision
    "computer vision", "image processing", "object detection",

    # Big Data
    "hadoop", "spark", "hive", "kafka", "airflow",

    # DevOps
    "git", "github", "docker", "kubernetes",
    "ci/cd", "jenkins", "linux", "terraform",
    "ansible", "prometheus", "grafana",

    # Cloud
    "aws", "azure", "gcp", "ec2", "s3", "lambda",

    # APIs / Architecture
    "rest api", "graphql", "microservices",
    "system design", "api development",

    # Testing / QA
    "unit testing", "pytest", "selenium",
    "automation testing", "manual testing",
    "junit", "postman",

    # Mobile
    "android", "ios", "flutter",
    "react native", "swift", "kotlin",
    "mobile development",

    # Frontend
    "frontend development", "responsive design",
    "ui development", "redux",

    # Cybersecurity
    "cybersecurity", "network security",
    "penetration testing", "ethical hacking",
    "vulnerability assessment", "firewall",
    "siem", "incident response",

    # Networking
    "networking", "tcp/ip", "dns", "routing",
    "switching", "network troubleshooting",

    # Database Roles
    "database administration", "database design",
    "query optimization", "sql tuning",
    "backup recovery",

    # UI/UX
    "ui design", "ux design", "figma",
    "adobe xd", "wireframing", "prototyping",
    "user research",

    # Product / Project Management
    "product management", "project management",
    "scrum", "agile", "jira", "kanban",
    "stakeholder management", "roadmap planning",

    # Business Analysis
    "business analysis", "requirement gathering",
    "process improvement", "strategic planning",
    "documentation", "workflow analysis",

    # Finance
    "financial analysis", "accounting",
    "bookkeeping", "budgeting",
    "financial reporting", "financial modeling",
    "taxation", "auditing", "cost analysis",
    "tally", "quickbooks", "excel",

    # Marketing
    "digital marketing", "seo", "sem",
    "content marketing", "social media marketing",
    "branding", "market research",
    "google analytics", "email marketing",

    # HR
    "recruitment", "talent acquisition",
    "employee engagement", "performance management",
    "conflict resolution", "hr policies",
    "payroll management", "employee relations",

    # Mechanical Engineering
    "autocad", "solidworks", "catia",
    "thermodynamics", "fluid mechanics",
    "mechanical design", "manufacturing processes",
    "cad modeling", "quality assurance",

    # Civil Engineering
    "structural analysis", "construction management",
    "site supervision", "project planning",
    "quantity surveying", "surveying",
    "building materials", "autocad civil 3d",

    # Electrical Engineering
    "circuit design", "power systems",
    "electrical machines", "control systems",
    "troubleshooting", "plc", "embedded systems",
    "electronics", "vlsi", "pcb design",

    # Embedded / Robotics
    "arduino", "raspberry pi", "iot",
    "embedded c", "robotics", "microcontrollers",

    # Soft Skills
    "communication", "teamwork", "problem solving",
    "leadership", "time management",
    "critical thinking", "presentation skills"
]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILL_DB]
matcher.add("SKILLS", patterns)


def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)

    found_skills = []

    for match_id, start, end in matches:
        skill = doc[start:end].text.lower()
        found_skills.append(skill)

    return list(set(found_skills))


if __name__ == "__main__":
    from resume_parser import extract_text_from_pdf

    resume_text = extract_text_from_pdf("sample_resume.pdf")
    skills = extract_skills(resume_text)

    print("===== Extracted Skills =====\n")
    print(skills)