#Arquivo responsável pelas queries do cliente
from app.database.local import Database
from app.models.cliente import Cliente,ClienteCreateUpdate

class ClienteRepository:
    def __init__(self,database:Database):
        self.db = database
        
    async def listar_clientes(self) -> list[Cliente] | None:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM clientes")
            linhas = cursor.fetchall()
            clientes = [Cliente(id_=linha[0],nome=linha[1],email=linha[2],
                            telefone=linha[3])
                    for linha in linhas
            ]
            return clientes
    
    async def get_cliente(self,cliente_id:int) -> Cliente | None:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id,nome,email,telefone FROM clientes WHERE id= ?",
                (cliente_id,)
            )
            linha = cursor.fetchone()
            if linha:
                return Cliente(id_=linha[0],nome=linha[1],email=linha[2],
                            telefone=linha[3])
            return None
        
    async def create_cliente(self,cliente:ClienteCreateUpdate)-> Cliente:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO clientes (nome,email,telefone) values (?,?,?)",
                (cliente.nome,cliente.email,cliente.telefone)
            )
            conexao.commit()
            cliente_id = cursor.lastrowid
            # Fetch the newly created cliente to ensure data consistency
            cursor.execute(
                "SELECT id, nome, email, telefone FROM clientes WHERE id = ?",
                (cliente_id,)
            )
            linha = cursor.fetchone()
            if linha:
                return Cliente(id_=linha[0], nome=linha[1], email=linha[2],
                            telefone=linha[3])
            raise Exception("Falha ao criar o cliente")
        
    async def update_cliente(self,cliente_id:int,
                            cliente:ClienteCreateUpdate) -> Cliente | None:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute( 
                "UPDATE clientes set nome = ?,email = ?,telefone =? \
                    WHERE id = ?",
                    (cliente.nome,cliente.email,cliente.telefone,cliente_id)
            )
            if cursor.rowcount == 0:
                return None
            return Cliente(id_=cliente_id,nome=cliente.nome,email=cliente.email,
                        telefone=cliente.telefone)
    
    async def delete_cliente(self,cliente_id:int) -> bool:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "DELETE FROM clientes WHERE id=?",(cliente_id,)
            )
            return cursor.rowcount > 0
        