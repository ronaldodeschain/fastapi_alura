from typing import Annotated
from fastapi import Depends

from app.database.local import Database
from app.database.cliente_repository import ClienteRepository

db = Database()

def get_database() -> Database:
    return db

def get_cliente_repository(
        local_db:Annotated[Database,Depends(
            get_database)]) -> ClienteRepository:
        return ClienteRepository(local_db)
    