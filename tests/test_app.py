from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture()
def client():
    return TestClient(app)


def test_add_usuario(client):
    response = client.post(
        '/users/',
        json={
            'username': 'teste1',
            'email': 'teste@email.com',
            'password': 'teste_pass',
            'tipo_usuario': 'G',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 'G1',
        'username': 'teste1',
        'email': 'teste@email.com',
        'tipo_usuario': 'G',
    }
