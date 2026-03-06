#Arquivo responsável pelas queries do cliente
from app.database.local import Database
from app.models.cliente import Cliente

class ClienteRepository:
    def __init__(self,database:Database):
        self.db = database
        
    async def listar_clientes(self) -> list[Cliente] | None:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM clientes")
            linhas = cursor.fetchall()
            clientes = [Cliente(id_=linha[0],nome=linha[1],email=linha[2],telefone=linha[3])
                    for linha in linhas
            ]
            return clientes