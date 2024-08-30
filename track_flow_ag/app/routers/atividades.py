from http import HTTPStatus

from app.db.db import atividades_db, projetos_db
from app.schemas.atividade import (
    AtividadeDB,
    AtividadeList,
    AtividadeSchema,
)
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/atividades', tags=['atividades'])


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=AtividadeDB,
)
def add_atividade(atividade: AtividadeSchema):
    atividade_with_id = AtividadeDB(**atividade.model_dump(), id_atividade=len(atividades_db) + 1)
    if not any(projeto.id_projeto == atividade_with_id.id_projeto for projeto in projetos_db):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Projeto não encontrado')
    else:
        atividade_with_id.status = 'CRIADO'
        atividades_db.append(atividade_with_id)
        return atividade_with_id


@router.put(
    '/{id_atividade}',
    status_code=HTTPStatus.OK,
    response_model=AtividadeDB,
)
def altera_atividade(id_atividade: int, atividade: AtividadeSchema):
    atividade_with_id = AtividadeDB(**atividade.model_dump(), id_atividade=id_atividade)
    if not any(atividade_with_id.id_atividade == id_atividade for atividade in atividades_db):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Atividade não encontrada')
    if id_atividade < 1 or id_atividade > len(atividades_db) + 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Atividade não encontrada')
    else:
        projetos_db[id_atividade - 1] = atividade_with_id
        return atividade_with_id


@router.get('/', response_model=AtividadeList, status_code=HTTPStatus.OK)
def lista_atividades():
    return {'atividades': atividades_db}
