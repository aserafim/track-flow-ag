from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class ClienteSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    tipo_usuario: str


class ClienteDB(ClienteSchema):
    id: int


class ClientePublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    tipo_usuario: str


class ClienteList(BaseModel):
    clientes: list[ClientePublic]


class ProjetoSchema(BaseModel):
    nome: str
    cliente_id: int
    status: str


class ProjetoDB(ProjetoSchema):
    id: int


class ProjetoList(BaseModel):
    projetos: list[ProjetoSchema]


class AtividadeSchema(BaseModel):
    id: int
    id_projeto: str
    status: str
    descricao: str


class AtividadeList(BaseModel):
    atividades: list[AtividadeSchema]
