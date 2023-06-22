import json
import pytest
import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from unittest import mock

from src.routes.planos_routes import planos_routes

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(planos_routes)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Utiliza-se o mock para testar a criação de planos
@mock.patch('src.routes.planos_routes.db')
def test_criar_plano(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.execute.return_value = None
    mock_db.commit.return_value = None

    data = {
        'descricao': 'Plano de teste',
        'valor': 9.99,
        'limite': 50
    }

    response = client.post('/planos', json=data)

    assert response.status_code == 200
    assert response.json == {'messange': 'Plano criado com sucesso!'}

# Utiliza-se o mock para testar a busca de planos
@mock.patch('src.routes.planos_routes.db')
def test_obter_planos(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 'Plano básico', 19.99, 100),
        (2, 'Plano premium', 29.99, 200)
    ]

    response = client.get('/planos')

    assert response.status_code == 200
    assert response.json == [
        {
            'id': 1,
            'descricao': 'Plano básico',
            'valor': 19.99,
            'limite': 100
        },
        {
            'id': 2,
            'descricao': 'Plano premium',
            'valor': 29.99,
            'limite': 200
        }
    ]
    
# Utiliza-se o mock para testar a busca de planos por id
@mock.patch('src.routes.planos_routes.db')
def test_obter_plano(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Plano básico', 19.99, 100)

    response = client.get('/planos/1')

    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'descricao': 'Plano básico',
        'valor': 19.99,
        'limite': 100
    }
    
# Utiliza-se o mock para testar o update do plano
@mock.patch('src.routes.planos_routes.db')
def test_atualizar_plano(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Plano existente', 19.99, 100)

    response = client.put('/planos/1', json={
        'descricao': 'Plano atualizado',
        'valor': 29.99,
        'limite': 200
    })

    assert response.status_code == 200
    assert response.json == {'messange': 'Plano atualizado com sucesso!'}

# Utiliza-se o mock para testar o delete de plano
@mock.patch('src.routes.planos_routes.db')
def test_excluir_plano(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1,)

    response = client.delete('/planos/1')

    assert response.status_code == 200
    assert response.json == {'messange': 'Plano excluído com sucesso!'}

# Utiliza-se o mock para testar a busca de plano por id inexistente
@mock.patch('src.routes.planos_routes.db')
def test_obter_plano_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.get('/planos/1')

    assert response.status_code == 404
    assert response.json == {'messange': 'Plano não encontrado'}

# Utiliza-se o mock para testar o update de plano inexistente
@mock.patch('src.routes.planos_routes.db')
def test_atualizar_plano_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.put('/planos/1', json={
        'descricao': 'Plano atualizado',
        'valor': 29.99,
        'limite': 200
    })

    assert response.status_code == 404
    assert response.json == {'messange': 'Plano não encontrado'}

# Utiliza-se o mock para testar o delete de plano inexistente
@mock.patch('src.routes.planos_routes.db')
def test_excluir_plano_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.delete('/planos/1')

    assert response.status_code == 404
    assert response.json == {'messange': 'Plano não encontrado'}
    
# Utiliza-se o mock para testar a criação de plano duplicado
@mock.patch('src.routes.planos_routes.db')
def test_criar_plano_registro_duplicado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1644)

    response = client.post('/planos', json={'descricao': 'Plano de teste', 'valor': 9.99, 'limite': 50})

    assert response.status_code == 400
    assert response.json == {'messange': 'Registro duplicado. Não é possível criar o plano.'}