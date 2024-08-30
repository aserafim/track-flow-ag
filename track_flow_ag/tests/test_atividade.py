from http import HTTPStatus


def test_cria_atividade(client):
    response = client.post(
        '/clientes/',
        json={
            'username': 'teste1',
            'email': 'teste@email.com',
            'password': 'teste_pass',
            'tipo_usuario': 'G',
        },
    )

    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'teste',
        },
    )

    response = client.post(
        '/atividades/',
        json={
            'id_projeto': 1,
            'descricao': 'teste',
            'status': 'CRIADO',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'descricao': 'teste',
        'id_atividade': 1,
        'status': 'CRIADO',
        'id_projeto': 1,
    }


def test_cria_atividade_projeto_nao_encontrado(client):
    response = client.post(
        '/atividades/',
        json={
            'nome': 'teste',
            'id_projeto': -1,
            'status': 'teste',
            'descricao': 'teste',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Projeto não encontrado'}


def test_altera_atividade(client):
    response = client.post(
        '/clientes/',
        json={
            'username': 'teste1',
            'email': 'teste@email.com',
            'password': 'teste_pass',
            'tipo_usuario': 'G',
        },
    )

    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'teste',
        },
    )

    response = client.post(
        '/atividades/',
        json={
            'id_projeto': 1,
            'descricao': 'teste',
            'status': 'CRIADO',
        },
    )

    response = client.put(
        '/atividades/1',
        json={
            'descricao': 'teste',
            'id_atividade': 1,
            'status': 'Finalizado',
            'id_projeto': 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'descricao': 'teste',
        'id_atividade': 1,
        'status': 'Finalizado',
        'id_projeto': 1,
    }


def test_altera_atividade_not_found(client):
    response = client.put(
        '/atividades/0',
        json={
            'descricao': 'teste',
            'status': 'status',
            'id_projeto': -2,
            'id_atividade': -2,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_lista_atividades(client):
    response = client.post(
        '/clientes/',
        json={
            'username': 'teste1',
            'email': 'teste@email.com',
            'password': 'teste_pass',
            'tipo_usuario': 'G',
        },
    )

    response = client.post(
        '/projetos/',
        json={
            'nome': 'teste',
            'id_cliente': 1,
            'status': 'teste',
        },
    )

    response = client.post(
        '/atividades/',
        json={
            'id_projeto': 1,
            'descricao': 'teste',
            'status': 'CRIADO',
        },
    )

    response = client.get('/atividades/')
    assert response.json() == {
        'atividades': [
            {
                'descricao': 'teste',
                'id_atividade': 1,
                'status': 'CRIADO',
                'id_projeto': 1,
            }
        ]
    }
