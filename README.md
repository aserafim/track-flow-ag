# FastAPI Projeto de Gerenciamento

Este projeto é uma aplicação web desenvolvida com FastAPI para gerenciar clientes, projetos e atividades. A aplicação expõe endpoints RESTful para criar, listar, atualizar e excluir clientes, projetos e atividades.

## Estrutura do Projeto

- **`app`**: Contém o código principal da aplicação FastAPI.
  - **`main.py`**: Configura a aplicação FastAPI e inclui os roteadores.
  - **`routers`**: Contém os módulos de roteamento para diferentes recursos (clientes, projetos, atividades).
    - **`clientes.py`**: Define endpoints relacionados a clientes.
    - **`projetos.py`**: Define endpoints relacionados a projetos.
    - **`atividades.py`**: Define endpoints relacionados a atividades.
  - **`schemas`**: Contém os schemas Pydantic usados para validação de dados.
    - **`cliente.py`**: Define os schemas para clientes.
    - **`projeto.py`**: Define os schemas para projetos.
    - **`atividade.py`**: Define os schemas para atividades.
  - **`db`**: Contém o código para manipulação do banco de dados.

## Instalando e Executando

1. **Clone o Repositório**

   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
