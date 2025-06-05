import pdfplumber
import google.generativeai as genai

def extract_text_from_pdf(file_path):
    full_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    return full_text.strip()

def prepare_prompt(resume_text, job_desc_text):
    return f"""
You are an expert recruiter. Carefully analyze the following RESUME and JOB DESCRIPTION, considering relevant criteria like required skills, experience, qualifications, and alignment of roles.

1. Give a score between 0 and 100, where above 80 means a perfect match.
2. Provide a brief explanation (in 3–5 bullet points) explaining why this score was given.
3. Highlight any major mismatches or strengths.

JOB DESCRIPTION:
\"\"\"
{job_desc_text}
\"\"\"

RESUME:
\"\"\"
{resume_text}
\"\"\"

Please structure your response like this:

Score: <number>

Explanation:
- Point 1
- Point 2
- ...

Strengths:
- ...

Mismatches:
- ...

Quantification:
- numeric breakdown of your final score and final score

Result:
"Under Review" - if the score is above 75
"Shortlisted" - if the score is above 55
"Rejected" - if the score is below 50
"""


# 3. Send prompt to Gemini API
def get_relevance_score(prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")  # Name of the free model you are using from the API key
    response = model.generate_content(prompt)
    try:
        score = int(response.text.strip())
        return score
    except ValueError:
        print("Unexpected output from Gemini:", response.text)
        return None

# 4. Main logic
if __name__ == "__main__":
    # Replace with your actual file paths
    resume_path = r"path to your resume goes here"  # Path of your resume.pdf file
    job_desc_path = r"path to your job description goes here"  # Path of the jobdescription.pdf file

    # Replace with your Gemini API key
    api_key = "Your API key goes here"  # Your Free API key from google gemini

    resume_text = extract_text_from_pdf(resume_path)
    job_desc_text = extract_text_from_pdf(job_desc_path)

    prompt = prepare_prompt(resume_text, job_desc_text)
    score = get_relevance_score(prompt, api_key)
