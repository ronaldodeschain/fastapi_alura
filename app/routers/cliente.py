from typing import Annotated
from fastapi import APIRouter,Depends,HTTPException

from app.models.cliente import Cliente
from app.database.cliente_repository import ClienteRepository
from app.dependency import get_cliente_repository

router = APIRouter(
    prefix="/clientes"
)

CLIENTE_LIST = [Cliente(id_ =1 ,nome="Erasmo",email="asdwe@amil",telefone="43433232"),
                Cliente(id_=2 ,nome="Jovs",email="asdwe@amil",telefone="43433232")]


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