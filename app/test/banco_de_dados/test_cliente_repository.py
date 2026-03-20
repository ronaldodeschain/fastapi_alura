import pytest
from app.database.cliente_repository import ClienteRepository
from app.models.cliente import ClienteCreateUpdate

@pytest.fixture
def cliente_repository(mock_banco_dados):
    return ClienteRepository(mock_banco_dados)

class TestClienteRepository:

    @pytest.mark.asyncio
    async def test_listar_clientes_retorna_lista_vazia(self,
                    cliente_repository,mock_banco_dados):
        mock_banco_dados.cursor.fetchall.return_value = []

        resultado = await cliente_repository.listar_clientes()

        assert resultado == []
        mock_banco_dados.cursor.execute.assert_called_once_with(
            "SELECT * FROM clientes"
        )

    @pytest.mark.asyncio
    async def test_listar_clientes_retorna_lista_com_clientes(self,cliente_repository,mock_banco_dados):
        mock_banco_dados.cursor.fetchall.return_value = [
            (1,"Cliente 1","cliente1@example.com","(11) 99999-9999"),
            (2,"Cliente 2","cliente2@example.com","(22) 88888-8888")
        ]
    
        resultado = await cliente_repository.listar_clientes()
        
        assert len(resultado) == 2
        assert resultado[0].id_ == 1
        assert resultado[0].nome == "Cliente 1"
        assert resultado[0].email == "cliente1@example.com"
        assert resultado[0].telefone == "(11) 99999-9999"
        assert resultado[1].id_ == 2
        assert resultado[1].nome == "Cliente 2"
        mock_banco_dados.cursor.execute.assert_called_once_with(
            "SELECT * FROM clientes"
        )