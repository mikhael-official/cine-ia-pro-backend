# Usa uma imagem oficial do Python
FROM python:3.10

# Cria uma pasta para o app
WORKDIR /code

# Copia os requisitos e instala
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia o código do main.py
COPY . .

# Comando para rodar a API na porta 7860 (padrão do Hugging Face)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
