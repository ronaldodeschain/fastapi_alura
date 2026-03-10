from typing import Annotated
from fastapi import APIRouter,Depends,HTTPException
from fastapi.responses import HTMLResponse

from app.models.cliente import Cliente,ClienteCreateUpdate
from app.database.cliente_repository import ClienteRepository
from app.dependencies import get_cliente_repository

router = APIRouter(
    prefix="/api/clientes"
)

front_router = APIRouter(
    prefix="/clientes"
)


@router.get("/",response_model=list[Cliente])
async def listar_clientes(cliente_repository:Annotated[ClienteRepository,Depends(get_cliente_repository)]):
    return await cliente_repository.listar_clientes()

@router.get("/{cliente_id}",response_model=Cliente | None)
async def get_cliente(
    cliente_id:int,
    cliente_repository:Annotated[ClienteRepository,Depends(get_cliente_repository)]
):
    cliente = await cliente_repository.get_cliente(cliente_id)
    
    if not cliente:
        raise HTTPException(status_code=404,detail="Cliente nao encontrado")
    
    return cliente

@router.post("/",response_model=Cliente,status_code=201)
async def create_cliente(
    cliente_repository:Annotated[ClienteRepository,Depends(get_cliente_repository)],
    cliente:ClienteCreateUpdate
):
    return await cliente_repository.create_cliente(cliente)

@router.put("/{cliente_id}",response_model=Cliente | None)
async def update_cliente(
    cliente_repository: Annotated[ClienteRepository,Depends(get_cliente_repository)],
    cliente_id:int,
    cliente:ClienteCreateUpdate
):
    cliente_atualizado = await cliente_repository.update_cliente(
        cliente_id,cliente)
    if not cliente_atualizado:
        raise HTTPException(status_code=404,detail="Cliente nao encontrado!")
    return cliente_atualizado

@router.delete("/{cliente_id}",status_code=204)
async def deletar_cliente(
    cliente_repositorio:Annotated[ClienteRepository,Depends(get_cliente_repository)],
    cliente_id: int 
):
    success = await cliente_repositorio.delete_cliente(cliente_id)
    if not success:
        raise HTTPException(status_code=404,detail="Cliente nao encontrado!")

