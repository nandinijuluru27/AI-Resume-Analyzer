import re

SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "FastAPI",
    "Flask",
    "Power BI",
    "Excel",
    "Git",
    "GitHub",
    "Machine Learning",
    "AI",
    "Data Analysis"
]


def extract_resume_details(text):

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    phone = re.findall(
        r"(?:\+91[-\s]?)?[6-9]\d{9}",
        text
    )

    skills = []

    lower_text = text.lower()

    for skill in SKILLS:
        if skill.lower() in lower_text:
            skills.append(skill)

    lines = text.split("\n")

    name = ""

    education = []
    experience = []
    certifications = []

    for line in lines[:5]:
        line = line.strip()

        if len(line.split()) >= 2 and len(line) < 40:
            name = line
            break

    return {
        "name": name,
        "email": email[0] if email else "",
        "phone": phone[0] if phone else "",
        "skills": skills,
        "education":education,
        "experience": experience,
        "certifications": certifications
    }