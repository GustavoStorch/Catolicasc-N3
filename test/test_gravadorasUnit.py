import json
import pytest
import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from unittest import mock

from src.routes.gravadoras_routes import gravadoras_routes

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(gravadoras_routes)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Utiliza-se o mock para testar a criação de gravadoras
@mock.patch('src.routes.gravadoras_routes.db')
def test_criar_gravadora(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.execute.return_value = None
    mock_db.commit.return_value = None

    data = {
        'nome': 'Gravadora de teste',
        'valor_contrato': 1000,
        'vencimento_contrato': '2023-06-30'
    }

    response = client.post('/gravadoras', json=data)

    assert response.status_code == 200
    assert response.json == {'message': 'Gravadora criada com sucesso!'}

# Utiliza-se o mock para testar a busca de gravadoras
@mock.patch('src.routes.gravadoras_routes.db')
def test_obter_gravadoras(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 'Gravadora 1', 1000, '2023-06-30'),
        (2, 'Gravadora 2', 2000, '2023-07-31')
    ]

    response = client.get('/gravadoras')

    assert response.status_code == 200
    assert response.json == [
        {
            'id': 1,
            'nome': 'Gravadora 1',
            'valor_contrato': 1000,
            'vencimento_contrato': '2023-06-30'
        },
        {
            'id': 2,
            'nome': 'Gravadora 2',
            'valor_contrato': 2000,
            'vencimento_contrato': '2023-07-31'
        }
    ]

# Utiliza-se o mock para testar a busca de gravadoras por id
@mock.patch('src.routes.gravadoras_routes.db')
def test_obter_gravadora(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Gravadora 1', 1000, '2023-06-30')

    response = client.get('/gravadoras/1')

    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'nome': 'Gravadora 1',
        'valor_contrato': 1000,
        'vencimento_contrato': '2023-06-30'
    }

# Utiliza-se o mock para testar o update do gravadora
@mock.patch('src.routes.gravadoras_routes.db')
def test_atualizar_gravadora(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Gravadora existente', 1000, '2023-06-30')

    response = client.put('/gravadoras/1', json={
        'nome': 'Gravadora atualizada',
        'valor_contrato': 2000,
        'vencimento_contrato': '2023-07-31'
    })

    assert response.status_code == 200
    assert response.json == {'message': 'Gravadora atualizada com sucesso!'}

# Utiliza-se o mock para testar o delete de gravadoras
@mock.patch('src.routes.gravadoras_routes.db')
def test_excluir_gravadora(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1,)

    response = client.delete('/gravadoras/1')

    assert response.status_code == 200
    assert response.json == {'message': 'Gravadora excluída com sucesso!'}

# Utiliza-se o mock para testar a busca de gravadora por id inexistente
@mock.patch('src.routes.gravadoras_routes.db')
def test_obter_gravadora_nao_encontrada(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.get('/gravadoras/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Gravadora não encontrada'}

# Utiliza-se o mock para testar o update de gravadora inexistente
@mock.patch('src.routes.gravadoras_routes.db')
def test_atualizar_gravadora_nao_encontrada(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.put('/gravadoras/1', json={
        'nome': 'Gravadora atualizada',
        'valor_contrato': 2000,
        'vencimento_contrato': '2023-07-31'
    })

    assert response.status_code == 404
    assert response.json == {'message': 'Gravadora não encontrada'}

# Utiliza-se o mock para testar o delete de gravadora inexistente
@mock.patch('src.routes.gravadoras_routes.db')
def test_excluir_gravadora_nao_encontrada(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.delete('/gravadoras/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Gravadora não encontrada'}

# Utiliza-se o mock para testar a criação de gravadora duplicado
@mock.patch('src.routes.gravadoras_routes.db')
def test_criar_gravadora_registro_duplicado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1644)

    data = {
        'nome': 'Gravadora duplicada',
        'valor_contrato': 1000,
        'vencimento_contrato': '2023-06-30'
    }

    response = client.post('/gravadoras', json=data)

    assert response.status_code == 400
    assert response.json == {'message': 'Registro duplicado. Não é possível criar a gravadora.'}