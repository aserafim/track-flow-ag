from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    tipo_usuario: str


class UserDB(UserSchema):
    id: str


class UserPublic(BaseModel):
    id: str
    username: str
    email: EmailStr
    tipo_usuario: str
