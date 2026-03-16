from app.database.local import Database
from app.models.usuario import Usuario,UsuarioCriarAtualizar

class UsuarioRepository:
    def __init__(self,database:Database):
        self.db = database

    async def get_usuario_por_email_e_senha(self,
                                            email:str,
                                            senha:str) -> Usuario | None:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id,nome,email FROM usuarios where email=? and senha=?",
                    (email,senha))
            linha = cursor.fetchone()
            if linha:
                return Usuario(id_=linha[0],nome=linha[1],email=linha[2])
            return None

    async def get_usuario_por_email(self,email:str) -> Usuario | None:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
            "SELECT id, nome, email FROM usuarios WHERE email = ?", (email,))
            linha = cursor.fetchone()
            if linha:
                return Usuario(id_=linha[0], nome=linha[1], email=linha[2])
            return None

    async def criar_usuario(self,
                        usuario_criar:UsuarioCriarAtualizar) -> Usuario | None:
        with self.db.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO usuarios (nome,email,senha) values (?,?,?)
                ''',
                (usuario_criar.nome,usuario_criar.email,usuario_criar.senha)
            )
            id_ = cursor.lastrowid
            return Usuario(id_=id_,nome=usuario_criar.nome,
                        email=usuario_criar.email,senha=usuario_criar.senha)