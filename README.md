# FastAPI Aplicação de Gerenciamento de Clientes

Esta é uma aplicação FastAPI simples para gerenciar informações de clientes.

## Visão Geral

A aplicação permite criar, ler, atualizar e excluir informações de clientes armazenadas em um banco de dados SQLite.

## Rotas

### Clientes

*   **GET `/clientes/`**: Retorna uma lista de todos os clientes.

    *   **Resposta de Exemplo**:

    ```json
    [
      {
        "id": 1,
        "nome": "João da Silva",
        "email": "joao@example.com",
        "telefone": "1234-5678"
      },
      {
        "id": 2,
        "nome": "Maria Souza",
        "email": "maria@example.com",
        "telefone": "9876-5432"
      }
    ]
    ```

*   **GET `/clientes/{cliente_id}`**: Retorna um cliente específico com base no ID.

    *   **Parâmetros**:
        *   `cliente_id` (int): O ID do cliente a ser retornado.
    *   **Resposta de Exemplo**:

    ```json
    {
      "id": 1,
      "nome": "João da Silva",
      "email": "joao@example.com",
      "telefone": "1234-5678"
    }
    ```

## Como Executar a Aplicação

1.  **Certifique-se de ter o Python instalado:**

    *   Verifique se o Python está instalado corretamente executando `python --version` no seu terminal.

2.  **Instale as dependências:**

    *   Navegue até o diretório do projeto no seu terminal.
    *   Execute `pip install -r requirements.txt` para instalar as dependências listadas no arquivo `requirements.txt`.

3.  **Execute a aplicação:**

    *   No mesmo diretório, execute o seguinte comando para iniciar o servidor FastAPI:

        ```bash
        uvicorn app.main:app --reload
        ```

        *   `app.main` é o módulo onde sua aplicação FastAPI está definida.
        *   `app` é a instância FastAPI.
        *   `--reload` permite que o servidor reinicie automaticamente em caso de alterações no código.

4.  **Acesse a aplicação:**

    *   Abra seu navegador e acesse `http://127.0.0.1:8000` para interagir com a aplicação.
    *   Para acessar a documentação da API, vá para `http://127.0.0.1:8000/docs`.

## Banco de Dados

A aplicação utiliza um banco de dados SQLite chamado `crimson.db`. O arquivo do banco de dados será criado automaticamente na primeira execução, caso não exista.
