from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from httpcodegenerator.HTTPCodeGeneratorFactory import HTTPCodeGeneratorFactory

app = FastAPI()
hcg = HTTPCodeGeneratorFactory.create_generator()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/httpcode", response_class=HTMLResponse)
def http_code(request: Request, action: str = Form(...)):
    if not action:
        return templates.TemplateResponse("httpcodes.html", {"request": request, "content": "Please provide an action"})
    try:
        candidates = hcg.generate_codes(action)
        return templates.TemplateResponse("httpcodes.html", {"request": request, "content": candidates})
    except Exception as e:
        return templates.TemplateResponse("httpcodes.html", {"request": request, "content": str(e)})