from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from search import search_images
from explanation import explain

app = FastAPI()

app.mount("/images", StaticFiles(directory="data/images"), name="images")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html") as f:
        return f.read()

@app.get("/search")
def search(query: str):
    images = search_images(query)
    return {
        "results": [
            {
                "image": img,
                "explanation": explain(img, query)
            } for img in images
        ]
    }
