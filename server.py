from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


def dados_API():
    apod_url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(
        apod_url,
        params={
            "api_key": os.getenv("API_KEY")
        }
    )

    response.raise_for_status()

    return response.json()


def transformar_video_url(url):
    if "youtube.com/watch?v=" in url:
        video_id = url.split("v=")[1].split("&")[0]

        return f"https://www.youtube.com/embed/{video_id}"

    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]

        return f"https://www.youtube.com/embed/{video_id}"

    return url


@app.route("/")
def home():
    dados = dados_API()

    titulo = dados.get("title")
    descricao = dados.get("explanation")
    data = dados.get("date")

    media_url = dados.get("url")
    media_type = dados.get("media_type")

    if media_type == "video":
        media_url = transformar_video_url(media_url)

    return render_template(
        "index.html",
        titulo=titulo,
        descricao=descricao,
        data=data,
        media_url=media_url,
        media_type=media_type
    )


if __name__ == "__main__":
    app.run(debug=True)