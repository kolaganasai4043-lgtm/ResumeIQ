import fitz
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "java", "javascript", "html", "css", "sql",
    "machine learning", "deep learning", "nlp", "flask",
    "django", "react", "nodejs", "mongodb", "mysql",
    "git", "docker", "aws", "data analysis", "pandas",
    "numpy", "tensorflow", "keras", "scikit-learn", "c++"
]

JOB_REQUIREMENTS = {
    "data scientist": ["python", "machine learning", "pandas",
                       "numpy", "sql", "data analysis", "scikit-learn"],
    "web developer": ["html", "css", "javascript", "react",
                      "nodejs", "mongodb", "git"],
    "python developer": ["python", "flask", "django", "sql", "git"],
    "ml engineer": ["python", "machine learning", "deep learning",
                    "tensorflow", "keras", "docker", "aws"]
}

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

def extract_skills(text):
    found_skills = []
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    return list(set(found_skills))

def match_job(resume_skills, job_role):
    required = JOB_REQUIREMENTS.get(job_role.lower(), [])
    if not required:
        return 0, [], required
    matched = [s for s in resume_skills if s in required]
    missing = [s for s in required if s not in resume_skills]
    percentage = (len(matched) / len(required)) * 100
    return round(percentage, 1), missing, required

def analyze_resume(pdf_path, job_role):
    text = extract_text_from_pdf(pdf_path)
    skills = extract_skills(text)
    match_percent, missing_skills, required = match_job(skills, job_role)
    return {
        "extracted_skills": skills,
        "match_percentage": match_percent,
        "missing_skills": missing_skills,
        "required_skills": required
    }