from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_text, job_description):
    texts = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)

    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    fit_score = round(cosine_sim[0][0] * 100, 2)

    resume_lines = resume_text.split("\n")
    top_matches = [line for line in resume_lines if len(line.strip()) > 0 and cosine_similarity(vectorizer.transform([line]), tfidf_matrix[1:2])[0][0] > 0.2]

    job_keywords = set(job_description.split())
    resume_keywords = set(resume_text.split())
    missing_keywords = job_keywords - resume_keywords

    return top_matches, missing_keywords, fit_score