import sqlite3
from contextlib import contextmanager

class Database():
    def __init__(self,nome_arquivo="crimson.db"):
        self.nome_arquivo = nome_arquivo
        self.start_database()
        
    @contextmanager
    def connect(self):
        connection = sqlite3.connect(self.nome_arquivo)
        try:
            yield connection
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()
            
    def start_database(self):
        with self.connect() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS clientes(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            telefone TEXT NOT NULL
                        )
                    ''')
        print("Banco de dados inicializado")