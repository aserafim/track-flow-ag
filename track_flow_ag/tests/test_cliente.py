from http import HTTPStatus


def test_add_cliente(client):
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
        'id_cliente': 1,
        'username': 'teste1',
        'email': 'teste@email.com',
        'tipo_usuario': 'G',
    }


def test_lista_clientes(client):
    # Primeiro, adicionar um cliente para
    # garantir que o banco de dados não esteja vazio
    client.post(
        '/clientes/',
        json={
            'username': 'teste1',
            'email': 'teste@email.com',
            'password': 'teste_pass',
            'tipo_usuario': 'G',
        },
    )

    response = client.get('/clientes/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'clientes': [
            {
                'id_cliente': 1,
                'username': 'teste1',
                'email': 'teste@email.com',
                'tipo_usuario': 'G',
            }
        ]
    }


def test_update_cliente(client):
    response = client.post(
        '/clientes/',
        json={
            'username': 'teste1',
            'email': 'teste@email.com',
            'password': 'teste_pass',
            'tipo_usuario': 'G',
        },
    )

    response = client.put(
        '/clientes/1',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
            'tipo_usuario': 'string',
            'id_cliente': 1,
        },
    )

    assert response.json() == {
        'username': 'string',
        'email': 'user@example.com',
        'tipo_usuario': 'string',
        'id_cliente': 1,
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


def test_delete_cliente(client):
    response = client.post(
        '/clientes/',
        json={
            'username': 'teste1',
            'email': 'teste@email.com',
            'password': 'teste_pass',
            'tipo_usuario': 'G',
        },
    )

    response = client.delete('/clientes/1')

    assert response.json() == {
        'username': 'teste1',
        'email': 'teste@email.com',
        'tipo_usuario': 'G',
        'id_cliente': 1,
    }


def test_delete_cliente_not_found(client):
    response = client.delete('/clientes/0')

    assert response.json() == {'detail': 'Usuário não encontrado'}
    assert response.status_code == HTTPStatus.BAD_REQUEST
