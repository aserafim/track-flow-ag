from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from schemas import (
    ClienteDB,
    ClienteList,
    ClientePublic,
    ClienteSchema,
    ProjetoDB,
    ProjetoSchema,
)

app = FastAPI()

clientes_db = []  # banco de dados provisório
projetos_db = []  # banco de dados provisório
atividades_db = []  # banco de dados provisório


@app.post('/clientes/', status_code=HTTPStatus.CREATED, response_model=ClientePublic)
def add_usuario(user: ClienteSchema):
    user_with_id = ClienteDB(**user.model_dump(), id=len(clientes_db) + 1)
    clientes_db.append(user_with_id)

    return user_with_id


@app.get('/clientes/', response_model=ClienteList, status_code=HTTPStatus.OK)
def lista_usuarios():
    return {'clientes': clientes_db}


@app.put('/clientes/{user_id}', response_model=ClientePublic)
def altera_usuario(user_id: int, user: ClienteSchema):
    if user_id < 1 or user_id > len(clientes_db) + 1:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Usuário não encontrado'
        )
    user_with_id = ClienteDB(**user.model_dump(), id=user_id)
    clientes_db[user_id - 1] = user_with_id
    return user_with_id


@app.delete('/clientes/{user_id}', response_model=ClientePublic)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(clientes_db) + 1:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Usuário não encontrado'
        )

    user_with_id = clientes_db[user_id - 1]
    del clientes_db[user_id - 1]
    return user_with_id


@app.post(
    '/projetos/',
    status_code=HTTPStatus.CREATED,
    response_model=ProjetoDB,
)
def add_projeto(projeto: ProjetoSchema):
    project_with_id = ProjetoDB(**projeto.model_dump(), id=len(projetos_db) + 1)
    if not any(cliente.id == project_with_id.cliente_id for cliente in clientes_db):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado'
        )
    else:
        project_with_id.status = 'CRIADO'
        projetos_db.append(project_with_id)
        return project_with_id


@app.put('/projetos/{project_id}', status_code=HTTPStatus.OK)
def altera_projetos(user: ClientePublic, projeto: ProjetoSchema): ...
