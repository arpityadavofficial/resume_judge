Resume Judge using Gemini API

This project is designed to assist recruiters in automating resume shortlisting by intelligently comparing candidate resumes with job descriptions using Google’s Gemini LLM.

Project Overview:

Recruiters often have to manually review hundreds of resumes to find suitable candidates for a given job posting. This script simplifies and speeds up the process by:
- Extracting text from both the resume and the job description (PDF format)
- Sending both texts to a Gemini LLM
- Getting back a **match score (0–100)** and **detailed justifications**
- Providing a verdict: **Shortlisted**, **Under Review**, or **Rejected**


Features

- ✅ PDF-to-text extraction using `pdfplumber`
- ✅ Relevance scoring via Google's `gemini-2.0-flash` model
- ✅ Structured feedback with justifications
- ✅ Console-based output for rapid evaluation


Project Structure

Resume_Judge
├── data/
│ ├── resumes/
│ │ └── example_resume.pdf
│ └── job_descriptions/
│ └── example_jd.pdf
├── main.py
├── requirements.txt
└── README.md


Install Dependencies

pip install -r requirements.txt


Add Your API Key

This project uses Google's Gemini API via the google-generativeai SDK.

Get a free Gemini API key from: https://aistudio.google.com/app/apikey

Open main.py and replace: api_key = "your API key goes here"


Run the Script:

python main.py
