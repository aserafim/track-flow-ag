from http import HTTPStatus

from fastapi import FastAPI

from schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []  # banco de dados provisório


@app.get('/users/', status_code=HTTPStatus.OK, response_model=Message)
def lista_clientes():
    return database


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def add_usuario(user: UserSchema):
    user_with_id = UserDB(
        **user.model_dump(), id=user.tipo_usuario + str(len(database) + 1)
    )
    database.append(user_with_id)

    return user_with_id
