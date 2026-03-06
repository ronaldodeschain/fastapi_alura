from fastapi import APIRouter

from app.models.cliente import Cliente

router = APIRouter(
    prefix="/clientes"
)

CLIENTE_LIST = [Cliente(id_ =1 ,nome="Erasmo",email="asdwe@amil",telefone="43433232"),
                Cliente(id_=2 ,nome="Jovs",email="asdwe@amil",telefone="43433232")]


@router.get("/",response_model=list[Cliente])
async def listar_clientes():
    return CLIENTE_LIST

@router.get("/{cliente_id}",response_model=Cliente | None)
async def get_cliente(cliente_id:int):
    for cliente in CLIENTE_LIST:
        if cliente.id_ == cliente_id:
            return cliente
    
    return None