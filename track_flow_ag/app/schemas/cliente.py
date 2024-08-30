from pydantic import BaseModel, EmailStr


class ClienteSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    tipo_usuario: str


class ClienteDB(ClienteSchema):
    id_cliente: int


class ClientePublic(BaseModel):
    id_cliente: int
    username: str
    email: EmailStr
    tipo_usuario: str


class ClienteList(BaseModel):
    clientes: list[ClientePublic]
