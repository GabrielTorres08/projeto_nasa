from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

def dados_API():
  apod_url = "https://api.nasa.gov/planetary/apod"
  response = requests.get(apod_url, params={"api_key": "1bwitvx0d1gqegHP2DeORpKbGRSaacChbEL6WeDy"})
  data = response.json()
  return data


@app.route("/")
def home():
  dados = dados_API()
  img_url = dados.get("url")
  titulo = dados.get('title')
  descricao = dados.get('explanation')
  return render_template("index.html", img_url=img_url, titulo=titulo, descricao=descricao)


if __name__ == "__main__":
  app.run(debug=True)
