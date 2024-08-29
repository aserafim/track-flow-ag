from http import HTTPStatus


def test_add_usuario(client):
    response = client.post(
        '/clientes/',
        json={
            'username': 'teste1',
            'email': 'teste@email.com',
            'password': 'teste_pass',
            'tipo_usuario': 'G',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'teste1',
        'email': 'teste@email.com',
        'tipo_usuario': 'G',
    }


def test_lista_usuarios(client):
    response = client.get('/clientes/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'clientes': [
            {
                'id': 1,
                'username': 'teste1',
                'email': 'teste@email.com',
                'tipo_usuario': 'G',
            }
        ]
    }


def test_update_cliente(client):
    response = client.put(
        '/clientes/1',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
            'tipo_usuario': 'string',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'tipo_usuario': 'string',
        'id': 1,
    }


def test_update_cliente_not_found(client):
    response = client.put(
        '/clientes/0',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
            'tipo_usuario': 'string',
            'id': 0,
        },
    )

    assert response.json() == {'detail': 'Usuário não encontrado'}
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_cria_projeto(client):
    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'cliente_id': 1,
            'status': 'teste',
        },
    )

    assert response.json() == {
        'id': 1,
        'nome': 'teste',
        'cliente_id': 1,
        'status': 'CRIADO',
    }

    assert response.status_code == HTTPStatus.CREATED


def test_cria_projeto_cliente_nao_encontrado(client):
    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'cliente_id': 0,
            'status': 'teste',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado'}


def test_delete_cliente(client):
    response = client.delete('/clientes/1')

    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'tipo_usuario': 'string',
        'id': 1,
    }


def test_delete_cliente_not_found(client):
    response = client.delete('/clientes/0')

    assert response.json() == {'detail': 'Usuário não encontrado'}
    assert response.status_code == HTTPStatus.BAD_REQUEST
