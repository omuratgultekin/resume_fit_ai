import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_suggestions(resume_text, job_description, missing_keywords):
    prompt = f"""
Here is the job description:
{job_description}

Here is the current resume:
{resume_text}

Update the resume to better match the job. Focus on including these missing keywords: {', '.join(missing_keywords)}.
Only output the revised resume content (no explanation).
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )
    return response.choices[0].message.content
