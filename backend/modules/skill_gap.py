def analyze_skill_gap(role, extracted_skills):           
    required_skills = ROLE_SKILLS.get(role, [])

    matched = []
    missing = []

    for skill in required_skills:
        if skill in extracted_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    coverage = 0
    if required_skills:
        coverage = round((len(matched) / len(required_skills)) * 100, 2)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "coverage_percentage": coverage
    }

ROLE_SKILLS = {
    "data scientist": [
        "python", "sql", "machine learning", "deep learning",
        "statistics", "pandas", "numpy", "scikit-learn",
        "tensorflow", "nlp"
    ],

    "data analyst": [
        "sql", "excel", "power bi", "tableau",
        "python", "pandas", "numpy",
        "data visualization", "statistics", "reporting"
    ],

    "business analyst": [
        "business analysis", "requirement gathering",
        "documentation", "stakeholder management",
        "process improvement", "excel", "sql"
    ],

    "ai engineer": [
        "python", "machine learning", "deep learning",
        "tensorflow", "pytorch", "nlp",
        "transformers", "llm"
    ],

    "ai/ml engineer": [
        "python", "machine learning", "deep learning",
        "tensorflow", "pytorch", "scikit-learn"
    ],

    "machine learning engineer": [
        "python", "machine learning", "scikit-learn",
        "tensorflow", "pytorch", "feature engineering"
    ],

    "deep learning engineer": [
        "python", "deep learning",
        "tensorflow", "pytorch",
        "computer vision", "neural networks"
    ],

    "nlp engineer": [
        "python", "nlp", "transformers",
        "bert", "gpt", "spacy", "nltk"
    ],

    "computer vision engineer": [
        "python", "opencv", "computer vision",
        "image processing", "tensorflow", "pytorch"
    ],

    "software engineer": [
        "python", "java", "c++",
        "data structures", "algorithms",
        "oop", "system design"
    ],

    "software development engineer": [
        "python", "java", "c++",
        "data structures", "algorithms",
        "oop", "system design"
    ],

    "backend developer": [
        "python", "django", "flask",
        "fastapi", "sql", "rest api",
        "microservices"
    ],

    "frontend developer": [
        "html", "css", "javascript",
        "react", "angular", "vue",
        "responsive design"
    ],

    "full stack developer": [
        "html", "css", "javascript",
        "react", "nodejs", "express",
        "mongodb", "sql", "rest api"
    ],

    "web developer": [
        "html", "css", "javascript",
        "react", "bootstrap", "nodejs"
    ],

    "mobile developer": [
        "flutter", "react native",
        "android", "ios",
        "swift", "kotlin"
    ],

    "android developer": [
        "android", "java",
        "kotlin", "firebase"
    ],

    "ios developer": [
        "ios", "swift",
        "xcode", "mobile development"
    ],

    "devops engineer": [
        "docker", "kubernetes",
        "jenkins", "terraform",
        "linux", "ci/cd", "aws"
    ],

    "cloud engineer": [
        "aws", "azure", "gcp",
        "docker", "kubernetes",
        "terraform"
    ],

    "site reliability engineer": [
        "linux", "docker",
        "kubernetes", "grafana",
        "prometheus", "monitoring"
    ],

    "cybersecurity analyst": [
        "cybersecurity", "network security",
        "penetration testing",
        "ethical hacking",
        "incident response"
    ],

    "network engineer": [
        "networking", "tcp/ip",
        "dns", "routing",
        "switching"
    ],

    "system administrator": [
        "linux", "windows server",
        "networking",
        "system administration",
        "troubleshooting"
    ],

    "database administrator": [
        "sql", "mysql",
        "postgresql", "oracle",
        "database administration",
        "backup recovery"
    ],

    "database developer": [
        "sql", "mysql",
        "postgresql",
        "database design",
        "query optimization"
    ],

    "qa engineer": [
        "manual testing",
        "automation testing",
        "selenium", "pytest"
    ],

    "test engineer": [
        "manual testing",
        "automation testing",
        "selenium"
    ],

    "automation test engineer": [
        "selenium",
        "pytest",
        "automation testing",
        "test automation"
    ],

    "ui/ux designer": [
        "figma", "wireframing",
        "prototyping", "ui design",
        "ux design"
    ],

    "product designer": [
        "figma", "ui design",
        "ux design", "prototyping"
    ],

    "product manager": [
        "product management",
        "roadmap planning",
        "agile", "scrum",
        "stakeholder management"
    ],

    "project manager": [
        "project management",
        "risk management",
        "agile", "scrum",
        "jira", "leadership"
    ],

    "scrum master": [
        "scrum", "agile",
        "jira", "team management"
    ],

    "hr manager": [
        "recruitment",
        "employee engagement",
        "communication",
        "performance management",
        "leadership"
    ],

    "recruiter": [
        "recruitment",
        "talent acquisition",
        "interviewing",
        "communication"
    ],

    "digital marketing specialist": [
        "seo", "sem",
        "google analytics",
        "social media marketing",
        "email marketing"
    ],

    "seo specialist": [
        "seo", "keyword research",
        "google analytics",
        "content optimization"
    ],

    "content strategist": [
        "content marketing",
        "branding",
        "seo",
        "social media marketing"
    ],

    "sales manager": [
        "sales", "crm",
        "negotiation",
        "leadership",
        "communication"
    ],

    "mechanical engineer": [
        "autocad", "solidworks",
        "thermodynamics",
        "fluid mechanics",
        "mechanical design"
    ],

    "civil engineer": [
        "autocad",
        "structural analysis",
        "construction management",
        "site supervision",
        "quantity surveying"
    ],

    "electrical engineer": [
        "circuit design",
        "power systems",
        "electrical machines",
        "control systems",
        "plc"
    ],

    "electronics engineer": [
        "electronics",
        "pcb design",
        "embedded systems",
        "circuit design"
    ],

    "embedded systems engineer": [
        "embedded systems",
        "embedded c",
        "microcontrollers",
        "arduino",
        "raspberry pi"
    ],

    "robotics engineer": [
        "robotics",
        "python",
        "computer vision",
        "embedded systems",
        "arduino"
    ],

    "accountant": [
        "accounting",
        "bookkeeping",
        "taxation",
        "auditing",
        "tally",
        "quickbooks"
    ],

    "financial analyst": [
        "financial analysis",
        "financial modeling",
        "budgeting",
        "excel",
        "reporting"
    ],

    "research scientist": [
        "research",
        "python",
        "statistics",
        "machine learning",
        "data analysis"
    ],

    "technical support engineer": [
        "technical support",
        "troubleshooting",
        "networking",
        "communication"
    ]
}

