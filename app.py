import streamlit as st
from resume_parser import parse_resume
from job_similarity import compute_similarity
from suggestion_engine import generate_suggestions
from resume_editor import export_to_docx
from ats_scraper import scrape_job_description
from linkedin_scraper import scrape_linkedin_profile

st.set_page_config(page_title="Resume Fit AI", layout="wide")
st.title("📄 Resume Fit AI: Tailor Your Resume with Generative AI")

uploaded_file = st.file_uploader("Upload Your Resume (.pdf or .docx)", type=["pdf", "docx"])
job_url = st.text_input("Paste the Job Description URL (optional)")
job_description = st.text_area("Or paste the Job Description manually")

linkedin_url = st.text_input("Enter LinkedIn profile URL (public)")

if linkedin_url:
    with st.spinner("Scraping LinkedIn profile..."):
        linkedin_experience = scrape_linkedin_profile(linkedin_url)
        st.write("LinkedIn Job Experience:")
        st.text_area("Scraped LinkedIn Experience (editable)", value=linkedin_experience, height=300)

if job_url:
    with st.spinner("Scraping job description..."):
        job_description = scrape_job_description(job_url)

if uploaded_file and job_description:
    with st.spinner("Parsing resume..."):
        resume_text = parse_resume(uploaded_file)

    with st.spinner("Computing similarity..."):
        top_matches, missing_keywords, fit_score = compute_similarity(resume_text, job_description)

    st.subheader("🧠 Resume Insights")
    st.write("**Top Relevant Sections from Resume:**")
    for match in top_matches:
        st.markdown(f"- {match}")

    st.write("**Missing Keywords from Job Description:**")
    st.markdown(", ".join(missing_keywords))

    st.write(f"**Fit Score**: {fit_score}%")  # Display Fit Score

    with st.spinner("Generating AI suggestions..."):
        suggestions = generate_suggestions(resume_text, job_description, missing_keywords)

    st.subheader("✍️ Suggested Resume Updates")
    edited_text = st.text_area("AI Suggestions (editable)", value=suggestions, height=250)

    if st.button("Download Updated Resume"):
        export_to_docx(edited_text, "/mnt/data/Updated_Resume.docx")
        with open("/mnt/data/Updated_Resume.docx", "rb") as file:
            st.download_button("Download .docx", file, "Updated_Resume.docx")