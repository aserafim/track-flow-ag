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


def test_update_user(client):
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


def test_update_user_not_found(client):
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


def test_delete_user(client):
    response = client.delete('/clientes/1')

    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'tipo_usuario': 'string',
        'id': 1,
    }


def test_delete_user_not_found(client):
    response = client.delete('/clientes/0')

    assert response.json() == {'detail': 'Usuário não encontrado'}
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_cria_projeto(client):
    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'cliente': 'teste',
            'status': 'teste',
            'alcada_criador': 'G',
        },
    )

    assert response.json() == {
        'nome': 'teste',
        'cliente': 'teste',
        'status': 'CRIADO',
        'alcada_criador': 'G',
    }

    assert response.status_code == HTTPStatus.CREATED


def test_cria_projeto_usuario_nao_autorizado(client):
    response = client.post(
        'projetos',
        json={
            'nome': 'teste',
            'cliente': 'teste',
            'status': 'teste',
            'alcada_criador': 'A',
        },
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Usuário não autorizado'}
