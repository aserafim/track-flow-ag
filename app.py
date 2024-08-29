from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from schemas import (
    ProjetoSchema,
    UserDB,
    UserList,
    UserPublic,
    clienteschema,
)

app = FastAPI()

database = []  # banco de dados provisório
pjdatabase = []


@app.post(
    '/clientes/', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def add_usuario(user: clienteschema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return user_with_id


@app.get('/clientes/', response_model=UserList, status_code=HTTPStatus.OK)
def lista_usuarios():
    return {'clientes': database}


@app.put('/clientes/{user_id}', response_model=UserPublic)
def altera_usuario(user_id: int, user: clienteschema):
    if user_id < 1 or user_id > len(database) + 1:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Usuário não encontrado'
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete('/clientes/{user_id}', response_model=UserPublic)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database) + 1:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Usuário não encontrado'
        )

    user_with_id = database[user_id - 1]
    del database[user_id - 1]
    return user_with_id


@app.post(
    '/projetos/',
    status_code=HTTPStatus.CREATED,
    response_model=ProjetoSchema,
)
def add_projeto(projeto: ProjetoSchema):
    if projeto.alcada_criador != ('G' or 'C'):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Usuário não autorizado',
        )
    else:
        projeto.status = 'CRIADO'
        pjdatabase.append(projeto)
        return projeto


@app.put('/projetos/', status_code=HTTPStatus.OK)
def altera_projetos(user: UserPublic, projeto: ProjetoSchema): ...
