from http import HTTPStatus


def test_cria_projeto(client):
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

    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'teste',
        },
    )

    assert response.json() == {
        'id_projeto': 1,
        'nome': 'teste',
        'id_cliente': 1,
        'status': 'CRIADO',
    }

    assert response.status_code == HTTPStatus.CREATED


def test_cria_projeto_cliente_nao_encontrado(client):
    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'id_cliente': 0,
            'status': 'teste',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Cliente não encontrado'}


def test_altera_projeto(client):
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

    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'teste',
        },
    )

    assert response.json() == {
        'id_projeto': 1,
        'nome': 'teste',
        'id_cliente': 1,
        'status': 'CRIADO',
    }

    assert response.status_code == HTTPStatus.CREATED

    response = client.put(
        '/projetos/1',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'Finalizado',
            'id_projeto': 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'nome': 'teste',
        'id_cliente': 1,
        'status': 'Finalizado',
        'id_projeto': 1,
    }


def test_altera_projeto_not_found(client):
    response = client.put(
        '/projetos/0',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'Finalizado',
            'id_projeto': 1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_lista_projetos(client):
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

    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'teste',
        },
    )

    assert response.json() == {
        'id_projeto': 1,
        'nome': 'teste',
        'id_cliente': 1,
        'status': 'CRIADO',
    }

    assert response.status_code == HTTPStatus.CREATED

    response = client.put(
        '/projetos/1',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'Finalizado',
            'id_projeto': 1,
        },
    )

    response = client.get('/projetos/')
    assert response.json() == {
        'projetos': [
            {
                'nome': 'teste',
                'id_cliente': 1,
                'status': 'Finalizado',
                'id_projeto': 1,
            }
        ]
    }
