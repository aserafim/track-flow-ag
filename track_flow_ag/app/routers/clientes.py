from http import HTTPStatus

from app.db.db import clientes_db
from app.schemas.cliente import (
    ClienteDB,
    ClienteList,
    ClientePublic,
    ClienteSchema,
)
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/clientes', tags=['clientes'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=ClientePublic)
def add_usuario(user: ClienteSchema):
    user_with_id = ClienteDB(**user.model_dump(), id_cliente=len(clientes_db) + 1)
    clientes_db.append(user_with_id)

    return user_with_id


@router.get('/', response_model=ClienteList, status_code=HTTPStatus.OK)
def lista_usuarios():
    return {'clientes': clientes_db}


@router.put('/{id_cliente}', response_model=ClientePublic)
def altera_usuario(id_cliente: int, user: ClienteSchema):
    if id_cliente < 1 or id_cliente > len(clientes_db) + 1:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Usuário não encontrado')
    user_with_id = ClienteDB(**user.model_dump(), id_cliente=id_cliente)
    clientes_db[id_cliente - 1] = user_with_id
    return user_with_id


@router.delete('/{id_cliente}', response_model=ClientePublic)
def delete_user(id_cliente: int):
    if id_cliente < 1 or id_cliente > len(clientes_db) + 1:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Usuário não encontrado')

    user_with_id = clientes_db[id_cliente - 1]
    del clientes_db[id_cliente - 1]
    return user_with_id
