import requests
from bs4 import BeautifulSoup

def scrape_job_description(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return "\n".join(p.get_text() for p in paragraphs)