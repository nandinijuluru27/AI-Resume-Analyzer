from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import shutil

from backend.utils.pdf_parser import extract_text_from_pdf
from backend.utils.resume_parser import extract_resume_details
from backend.utils.ats import calculate_ats_score
app = FastAPI(
    title="Nandini ATS Test",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class JobDescription(BaseModel):
    resume_skills: list[str]
    job_description: str

UPLOAD_FOLDER = "backend/uploads"
@app.post("/ats-score")
def ats_score(data: JobDescription):

    result = calculate_ats_score(
        data.resume_skills,
        data.job_description
    )

    return result

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "project": "AI Resume Analyzer",
        "developer": "Nandini Juluru",
        "status": "Backend is running successfully!"
    }


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    resume_data = extract_resume_details(extracted_text)

    return {
        "filename": file.filename,
        "resume": resume_data
    }