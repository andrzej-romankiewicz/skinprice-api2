from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Symulacja bazy danych skinów (w przyszłości pobierzemy to z API/Bazy)
skins_data = [
    {"name": "AK-47 | Slate (FT)", "price": 12.50, "trend": [10, 11, 13, 12, 12.5]},
    {"name": "M4A1-S | Mecha Industries", "price": 25.80, "trend": [20, 22, 25, 24, 25.8]},
    {"name": "AWP | Atheris", "price": 9.20, "trend": [7, 8.5, 9, 8.8, 9.2]}
]

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "skins": skins_data,
        "labels": ["Pon", "Wt", "Śr", "Czw", "Pt"],
        "prices": [s["price"] for s in skins_data],
        "names": [s["name"] for s in skins_data]
    })