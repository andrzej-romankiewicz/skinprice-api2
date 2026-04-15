from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Definiujemy folder z wyglądem strony
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    skins_data = [
        {"name": "AK-47 | Slate (FT)", "price": 12.50},
        {"name": "M4A1-S | Mecha Industries", "price": 25.80},
        {"name": "AWP | Atheris", "price": 9.20}
    ]
    
    # TUTAJ JEST ZMIANA: Dodajemy request=, name= i context=
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"skins": skins_data}
    )
