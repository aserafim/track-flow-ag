from pydantic import BaseModel


class AtividadeSchema(BaseModel):
    id_projeto: int
    status: str
    descricao: str


class AtividadeDB(AtividadeSchema):
    id_atividade: int


class AtividadeList(BaseModel):
    atividades: list[AtividadeDB]
