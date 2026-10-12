import re

TECHNICAL_SKILLS = {
    # Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "go", "ruby", "php", "kotlin", "swift",

    # Web Development
    "html", "css", "react", "angular", "vue", "node.js",
    "express", "bootstrap", "tailwind",

    # Databases
    "sql", "mysql", "postgresql", "mongodb", "oracle",
    "sqlite", "redis",

    # Python / Backend
    "fastapi", "django", "flask",

    # Data / AI / ML
    "machine learning", "deep learning",
    "artificial intelligence", "ai",
    "tensorflow", "pytorch", "pandas", "numpy",
    "scikit-learn", "opencv",

    # Cloud / DevOps
    "aws", "azure", "gcp",
    "docker", "kubernetes",
    "jenkins", "terraform",

    # Tools
    "git", "github", "gitlab",
    "power bi", "excel",
    "tableau",

    # APIs
    "api", "rest api", "graphql"
}

def generate_suggestions(missing_skills):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(
            f"Consider adding {skill} to your resume if you have relevant experience."
        )

    return suggestions

def calculate_ats_score(resume_skills, job_description):

    job_description = job_description.lower()

    job_skills = set()

    for skill in TECHNICAL_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, job_description):
            job_skills.add(skill)
        
        
    matched = []

    missing = []

    for skill in resume_skills:

        if skill.lower() in job_description:
            matched.append(skill)

    resume_skills_lower = [skill.lower() for skill in resume_skills]

    for skill in job_skills:

        if skill.lower() not in resume_skills_lower:
            missing.append(skill.title())
    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched) / len(job_skills)) * 100)
    return {
    "ats_score": score,
    "matched_skills": matched,
    "missing_skills": sorted(list(set(missing)))[:20],
    "suggestions": generate_suggestions(
        sorted(list(set(missing)))[:20]
    )
}