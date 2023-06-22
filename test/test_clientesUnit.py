import json
import pytest
import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from unittest import mock

from src.routes.clientes_routes import clientes_routes

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(clientes_routes)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Utiliza-se o mock para testar a criação de clientes
@mock.patch('src.routes.clientes_routes.db')
def test_criar_cliente(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.execute.return_value = None
    mock_db.commit.return_value = None

    data = {
        'login': 'cliente_teste',
        'senha': 'senha123',
        'planos_id': 1,
        'email': 'cliente@teste.com'
    }

    response = client.post('/clientes', json=data)

    assert response.status_code == 200
    assert response.json == {'message': 'Cliente criado com sucesso!'}

# Utiliza-se o mock para testar a busca de clientes
@mock.patch('src.routes.clientes_routes.db')
def test_obter_clientes(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 'cliente1', 'senha123', 1, 'cliente1@teste.com'),
        (2, 'cliente2', 'senha456', 2, 'cliente2@teste.com')
    ]

    response = client.get('/clientes')

    assert response.status_code == 200
    assert response.json == [
        {
            'id': 1,
            'login': 'cliente1',
            'senha': 'senha123',
            'planos_id': 1,
            'email': 'cliente1@teste.com'
        },
        {
            'id': 2,
            'login': 'cliente2',
            'senha': 'senha456',
            'planos_id': 2,
            'email': 'cliente2@teste.com'
        }
    ]

# Utiliza-se o mock para testar a busca de clientes por id
@mock.patch('src.routes.clientes_routes.db')
def test_obter_cliente(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'cliente1', 'senha123', 1, 'cliente1@teste.com')

    response = client.get('/clientes/1')

    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'login': 'cliente1',
        'senha': 'senha123',
        'planos_id': 1,
        'email': 'cliente1@teste.com'
    }

# Utiliza-se o mock para testar o update do cliente
@mock.patch('src.routes.clientes_routes.db')
def test_atualizar_cliente(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'cliente1', 'senha123', 1, 'cliente1@teste.com')

    response = client.put('/clientes/1', json={
        'login': 'cliente1_atualizado',
        'senha': 'novasenha',
        'planos_id': 2,
        'email': 'cliente1_atualizado@teste.com'
    })

    assert response.status_code == 200
    assert response.json == {'message': 'Cliente atualizado com sucesso!'}

# Utiliza-se o mock para testar o delete de clientes
@mock.patch('src.routes.clientes_routes.db')
def test_excluir_cliente(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1,)

    response = client.delete('/clientes/1')

    assert response.status_code == 200
    assert response.json == {'message': 'Cliente excluído com sucesso!'}

# Utiliza-se o mock para testar a busca de cliente por id inexistente
@mock.patch('src.routes.clientes_routes.db')
def test_obter_cliente_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.get('/clientes/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Cliente não encontrado'}

# Utiliza-se o mock para testar o update de cliente inexistente
@mock.patch('src.routes.clientes_routes.db')
def test_atualizar_cliente_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.put('/clientes/1', json={
        'login': 'cliente1_atualizado',
        'senha': 'novasenha',
        'planos_id': 2,
        'email': 'cliente1_atualizado@teste.com'
    })

    assert response.status_code == 404
    assert response.json == {'message': 'Cliente não encontrado'}

# Utiliza-se o mock para testar o delete de cliente inexistente
@mock.patch('src.routes.clientes_routes.db')
def test_excluir_cliente_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.delete('/clientes/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Cliente não encontrado'}

# Utiliza-se o mock para testar a criação de cliente duplicado
@mock.patch('src.routes.clientes_routes.db')
def test_criar_cliente_erro_registro_duplicado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1644)

    data = {
        'login': 'cliente_duplicado',
        'senha': 'senha123',
        'planos_id': 1,
        'email': 'cliente_duplicado@teste.com'
    }

    response = client.post('/clientes', json=data)

    assert response.status_code == 400
    assert response.json == {'message': 'Erro ao criar o cliente no banco de dados.'}

# Utiliza-se o mock para testar a criação de cliente por chave estrangeira inválida
@mock.patch('src.routes.clientes_routes.db')
def test_criar_cliente_erro_chave_estrangeira(mock_db, client):
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1452)

    data = {
        'login': 'cliente_invalido',
        'senha': 'senha123',
        'planos_id': 999,
        'email': 'cliente_invalido@teste.com'
    }

    response = client.post('/clientes', json=data)

    assert response.status_code == 400
    assert response.json == {'message': 'Erro ao criar o cliente no banco de dados.'}