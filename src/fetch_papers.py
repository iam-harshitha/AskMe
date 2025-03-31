import requests
import xml.etree.ElementTree as ET

def fetch_arxiv_papers(query, max_results=5):
    """Fetch related research papers from ArXiv based on a search query."""
    base_url = "http://export.arxiv.org/api/query?"
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending"
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return []

    # Parse XML response
    root = ET.fromstring(response.text)
    papers = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        link = entry.find("{http://www.w3.org/2005/Atom}id").text
        papers.append({"title": title, "url": link})

    return papers
