from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    tipo_usuario: str


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    tipo_usuario: str


class UserList(BaseModel):
    users: list[UserPublic]


class ProjetoSchema(BaseModel):
    nome: str
    cliente: str
    status: str
    alcada_criador: str
