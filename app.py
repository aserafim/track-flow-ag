from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from schemas import (
    ProjetoSchema,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []  # banco de dados provisório
pjdatabase = []


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def add_usuario(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList, status_code=HTTPStatus.OK)
def lista_usuarios():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def altera_usuario(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(database) + 1:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Usuário não encontrado'
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id


@app.put('/projetos/', status_code=HTTPStatus.OK)
def altera_projetos(user: UserPublic, projeto: ProjetoSchema): ...


@app.post('/projetos/', status_code=HTTPStatus.CREATED)
def add_projeto(
    projeto: ProjetoSchema,
    status_code=HTTPStatus.CREATED,
    response_model=ProjetoSchema,
):
    if projeto.alcada_criador != ('G' or 'C'):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Usuário não autorizado',
        )
    else:
        projeto.status = 'CRIADO'
        pjdatabase.append(projeto)
        return projeto
