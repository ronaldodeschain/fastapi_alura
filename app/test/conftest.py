from contextlib import contextmanager
from unittest.mock import MagicMock,AsyncMock,Mock

import pytest
from fastapi import Request

@pytest.fixture
def mock_banco_dados():
    class MockBancoDeDadosLocal:
        def __init__(self):
            self.conexao = MagicMock()
            self.cursor = MagicMock()
            self.conexao.cursor.return_value = self.cursor

        @contextmanager
        def connect(self):
            yield self.conexao
    
    return MockBancoDeDadosLocal()

@pytest.fixture
def mock_cliente_repositorio():
    mock_repo = Mock()
    mock_repo.listar_clientes = AsyncMock()
    mock_repo.obter_cliente = AsyncMock()
    mock_repo.criar_cliente = AsyncMock()
    mock_repo.atualizar_cliente = AsyncMock()
    mock_repo.excluir_cliente = AsyncMock()
    return mock_repo

@pytest.fixture
def mock_usuario_repositorio():
    mock_repo = Mock()
    mock_repo.obter_usuario_por_email = AsyncMock()
    mock_repo.obter_usuario_por_email_e_senha = AsyncMock()
    mock_repo.criar_usuario = AsyncMock()
    return mock_repo

@pytest.fixture
def mock_request():
    return Mock(spec=Request)