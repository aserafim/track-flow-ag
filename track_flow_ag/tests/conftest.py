"""import pytest
from fastapi.testclient import TestClient

from track_flow_ag.app.main import app


@pytest.fixture()
def client():
    return TestClient(app)"""

import pytest
from fastapi.testclient import TestClient

from track_flow_ag.app.app import app
from track_flow_ag.app.routers.atividades import atividades_db
from track_flow_ag.app.routers.clientes import clientes_db
from track_flow_ag.app.routers.projetos import projetos_db


@pytest.fixture()
def client():
    # Limpa os bancos de dados em memória antes de cada teste
    clientes_db.clear()
    projetos_db.clear()
    atividades_db.clear()
    return TestClient(app)
