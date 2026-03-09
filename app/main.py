from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.routers import cliente

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Crimson Clawn",
    description="CRM para Crimson Claw",
    version="1.0.0",    
)

app.mount("/static",StaticFiles(directory="static"),name="static")
app.include_router(cliente.router)

@app.get("/health")
async def health_check():
    return {"status":"ok"}

@app.get("/", response_class=HTMLResponse)
async def front_page(request:Request):
    return templates.TemplateResponse("index.html",{"request":request,"titulo":"Crimson Claw Studio","versão":"1.0.0"})