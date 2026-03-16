from typing import Annotated

from fastapi import APIRouter,Depends,HTTPException,Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates

from app.models.usuario import UsuarioCriarAtualizar
from app.database.usuario_repository import UsuarioRepository 
import app.dependencies as dependencies

router = APIRouter(
    prefix="/registro"
)

templates = Jinja2Templates(directory="templates")

@router.get("/",response_class=HTMLResponse)
async def pagina_registro(request:Request):
    return templates.TemplateResponse("registro.html",{"request":request})

@router.post("/")
async def registrar_usuario(
    usuario_repository:Annotated[UsuarioRepository,Depends(
        dependencies.get_usuario_repository)],
    request:Request,
    nome:str = Form(...),
    email:str=Form(...),
    senha:str=Form(...),
    confirma_senha=Form(...),):

    data={
        "nome":nome,
        "email":email,
        "senha":senha,
        "confirma_senha":confirma_senha,
    }
    if not all([nome,email,senha,confirma_senha]):
        return templates.TemplateResponse("registro.html",{
            "request":request,
            "error":"Campos obrigatorios faltantes",
            **data
        })

    usuario_existente = await usuario_repository.get_usuario_por_email(email)
    if usuario_existente:
        return templates.TemplateResponse("registro.html",{
            "request":request,
            "error":"Usuario invalido!",
            **data
        })

    usuario_criar = UsuarioCriarAtualizar(nome=nome, email=email, senha=senha)
    usuario = await usuario_repository.criar_usuario(usuario_criar)
    
    if usuario:
        response = RedirectResponse(url="/login",status_code=303)
        return response
    
    return templates.TemplateResponse("registro.html",{
            "request":request,
            "error":"Nao foi possivel criar o usuario, tente novamente mais tarde",
            **data
        })