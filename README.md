# AI Resume Analyzer

A Python-based web application that analyzes resumes and compares a candidate's skills with a job description to help identify skill gaps.

## Features

- Upload resumes in PDF format.
- Extract resume text and skills.
- Compare resume skills with job requirements.
- Generate an estimated ATS-style score.
- Display matched skills, missing skills, and improvement suggestions.

## Technologies Used

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **PDF Processing:** Python PDF parsing libraries
- **API Communication:** REST API

## Project Structure

```text
AI-Resume-Analyzer/
├── backend/
│   ├── main.py
│   └── utils/
│       ├── ats.py
│       ├── pdf_parser.py
│       └── resume_parser.py
├── frontend/
│   └── index.html
└── .gitignore
```

## How to Run

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the required Python packages.
4. Start the FastAPI backend:

   `uvicorn backend.main:app --reload`

5. Open the API documentation at `http://127.0.0.1:8000/docs`.
6. Open `frontend/index.html` in a browser to use the interface.

## Note

The ATS-style score is an estimate based on skill matching. It does not guarantee how a real applicant tracking system will evaluate a resume.

## Future Improvements

- Improve resume parsing accuracy.
- Add downloadable analysis reports.
- Expand skill extraction and job-role support.
