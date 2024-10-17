import requests
from bs4 import BeautifulSoup
from flask import jsonify

def get_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        return jsonify({"title": title})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrair cabeçalhos
        headers = []
        for header_tag in ['h1', 'h2', 'h3']:
            for header in soup.find_all(header_tag):
                headers.append(header.get_text(strip=True))

        # Extrair parágrafos
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

        return jsonify({
            "headers": headers,
            "paragraphs": paragraphs
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
