from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.routers import cliente

app = FastAPI(
    title="Crimson Clawn",
    description="CRM para Crimson Claw",
    version="1.0.0",    
)

app.include_router(cliente.router)

@app.get("/")
async def health_check():
    return {"status":"ok"}

@app.get("/front", response_class=HTMLResponse)
async def front_page():
    html_content="""
        <html>
            <head>
                <title> Crimson Claw</title>
            </head>
            <body>
                <h1> Crimson Claw Studio </h1>
                <p> Sistema de Gestão de pedidos Crimson Claw</p>
                <p>Status: <strong>Operacional</strong></p>
            </body>
        </html>
        """
    return html_content
        