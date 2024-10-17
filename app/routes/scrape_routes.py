from flask import request, jsonify
from app import app, auth
from app.services.scraping_service import get_title, get_content

@app.route('/scrape/title', methods=['GET'])
@auth.login_required
def scrape_title():
    """
    Extrai o título de uma página web fornecida pela URL.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: url
        in: query
        type: string
        required: true
        description: URL da página web para extrair o título.
    responses:
      200:
        description: Título da página web.
        schema:
          type: object
          properties:
            title:
              type: string
              description: O título da página.
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    return get_title(url)

@app.route('/scrape/content', methods=['GET'])
@auth.login_required
def scrape_content():
    """
    Extrai cabeçalhos e parágrafos de uma página web fornecida pela URL.
    ---
    security:
      - BasicAuth: []
    parameters:
      - name: url
        in: query
        type: string
        required: true
        description: URL da página web para extrair o conteúdo.
    responses:
      200:
        description: Conteúdo da página web.
        schema:
          type: object
          properties:
            headers:
              type: array
              items:
                type: string
              description: Lista de cabeçalhos (h1, h2, h3).
            paragraphs:
              type: array
              items:
                type: string
              description: Lista de parágrafos.
      400:
        description: Erro de requisição.
      401:
        description: Não autorizado.
    """
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL é obrigatória"}), 400
    return get_content(url)
