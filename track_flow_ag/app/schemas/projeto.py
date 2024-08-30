from pydantic import BaseModel


class ProjetoSchema(BaseModel):
    nome: str
    id_cliente: int
    status: str


class ProjetoDB(ProjetoSchema):
    id_projeto: int


class ProjetoList(BaseModel):
    projetos: list[ProjetoDB]
