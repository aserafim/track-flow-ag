from http import HTTPStatus

from app.db.db import clientes_db, projetos_db
from app.schemas.projeto import (
    ProjetoDB,
    ProjetoList,
    ProjetoSchema,
)
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/projetos', tags=['projetos'])


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=ProjetoDB,
)
def add_projeto(projeto: ProjetoSchema):
    project_with_id = ProjetoDB(**projeto.model_dump(), id_projeto=len(projetos_db) + 1)
    if not any(cliente.id_cliente == project_with_id.id_cliente for cliente in clientes_db):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Cliente não encontrado')
    else:
        project_with_id.status = 'CRIADO'
        projetos_db.append(project_with_id)
        return project_with_id


@router.put('/{id_projeto}', status_code=HTTPStatus.OK, response_model=ProjetoDB)
def altera_projeto(id_projeto: int, projeto: ProjetoSchema):
    project_with_id = ProjetoDB(**projeto.model_dump(), id_projeto=id_projeto)
    if not any(project_with_id.id_cliente == id_projeto for projeto in projetos_db):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Projeto não encontrado')
    else:
        projetos_db[id_projeto - 1] = project_with_id
        return project_with_id


@router.get('/', response_model=ProjetoList, status_code=HTTPStatus.OK)
def lista_projetos():
    return {'projetos': projetos_db}
