# Use uma imagem base oficial do Python, leve e otimizada
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos da aplicação para o diretório de trabalho
COPY . .

# Expõe a porta 5000 para a aplicação Flask
EXPOSE 5000

# Define a variável de ambiente para o Flask
ENV FLASK_APP=run.py

# Executa o comando para iniciar o servidor Flask
CMD ["flask", "run", "--host=0.0.0.0"]
