from fastapi import FastAPI

from app.routers import atividades, clientes, projetos

app = FastAPI()

app.include_router(clientes.router)
app.include_router(projetos.router)
app.include_router(atividades.router)
