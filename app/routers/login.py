from typing import Annotated

from fastapi import APIRouter,Depends,HTTPException,Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates

from app.database.usuario_repository import UsuarioRepository 
from app.dependencies import get_usuario_repository

router = APIRouter(
    prefix="/login"
)

templates = Jinja2Templates(directory="templates")

@router.get("/",response_class=HTMLResponse)
async def pagina_login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@router.post("/")
async def login(request:Request,
                usuario_repository:Annotated[UsuarioRepository,Depends
                                    (get_usuario_repository)],
                email:str=Form(...),
                senha:str=Form(...)
                ):
    usuario = await usuario_repository.get_usuario_por_email_e_senha(email,senha)
    
    if usuario:
        response = RedirectResponse(url="/",status_code=303)
        response.set_cookie(key="session_token",value="token-senha",
                            httponly=True)
        return response

    return templates.TemplateResponse("login.html",{
        "request":request,
        "email":email,
        "senha":senha,
        "error":"Credenciais invalidas"
    })