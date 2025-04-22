import requests
from bs4 import BeautifulSoup

def scrape_linkedin_profile(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        experiences = []
        for section in soup.find_all("section"):
            if "experience" in section.get("class", []):
                items = section.find_all("li")
                for item in items:
                    experiences.append(item.get_text(strip=True))
        return "\n".join(experiences) if experiences else "No relevant job experience found."
    except Exception as e:
        return f"Error: {str(e)}"