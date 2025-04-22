import openai

openai.api_key = "sk-..."

def generate_suggestions(resume_text, job_description, missing_keywords):
    prompt = f"Here is the job description:\n{job_description}\n\nHere is the current resume:\n{resume_text}\n\nUpdate the resume to better match the job. Highlight missing keywords: {', '.join(missing_keywords)}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )
    return response.choices[0].message["content"]