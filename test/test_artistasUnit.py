import json
import pytest
import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from unittest import mock

from src.routes.artista_routes import artista_routes

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(artista_routes)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Utiliza-se o mock para testar a criação de artistas
@mock.patch('src.routes.artista_routes.db')
def test_criar_artista(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    # Configuração do mock do banco de dados
    mock_cursor.execute.return_value = None
    mock_db.commit.return_value = None

    data = {
        'nome': 'Artista de teste',
        'gravadoras_id': 1
    }

    response = client.post('/artistas', json=data)

    assert response.status_code == 200
    assert response.json == {'message': 'Artista criado com sucesso!'}

# Utiliza-se o mock para testar a busca de artistas
@mock.patch('src.routes.artista_routes.db')
def test_obter_artistas(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 'Artista 1', 1),
        (2, 'Artista 2', 2)
    ]

    response = client.get('/artistas')

    assert response.status_code == 200
    assert response.json == [
        {
            'id': 1,
            'nome': 'Artista 1',
            'gravadoras_id': 1
        },
        {
            'id': 2,
            'nome': 'Artista 2',
            'gravadoras_id': 2
        }
    ]

# Utiliza-se o mock para testar a busca de artista por id
@mock.patch('src.routes.artista_routes.db')
def test_obter_artista(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Artista 1', 1)

    response = client.get('/artistas/1')

    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'nome': 'Artista 1',
        'gravadoras_id': 1
    }

# Utiliza-se o mock para testar o update do artista
@mock.patch('src.routes.artista_routes.db')
def test_atualizar_artista(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Artista existente', 1)

    response = client.put('/artistas/1', json={
        'nome': 'Artista atualizado',
        'gravadoras_id': 2
    })

    assert response.status_code == 200
    assert response.json == {'message': 'Artista atualizado com sucesso!'}

# Utiliza-se o mock para testar o delete de artistas
@mock.patch('src.routes.artista_routes.db')
def test_excluir_artista(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1,)

    response = client.delete('/artistas/1')

    assert response.status_code == 200
    assert response.json == {'message': 'Artista excluído com sucesso!'}

# Utiliza-se o mock para testar a busca de artista por id inexistente
@mock.patch('src.routes.artista_routes.db')
def test_obter_artista_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.get('/artistas/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Artista não encontrado'}

# Utiliza-se o mock para testar o update de artista inexistente
@mock.patch('src.routes.artista_routes.db')
def test_atualizar_artista_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.put('/artistas/1', json={
        'nome': 'Artista atualizado',
        'gravadoras_id': 2
    })

    assert response.status_code == 404
    assert response.json == {'message': 'Artista não encontrado'}

# Utiliza-se o mock para testar o delete de artista inexistente
@mock.patch('src.routes.artista_routes.db')
def test_excluir_artista_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.delete('/artistas/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Artista não encontrado'}

# Utiliza-se o mock para testar a criação de artista duplicado
@mock.patch('src.routes.artista_routes.db')
def test_criar_artista_erro_registro_duplicado(mock_db, client):
    # Simula um erro de registro duplicado
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1644)

    data = {
        'nome': 'Artista duplicado',
        'gravadoras_id': 1
    }

    response = client.post('/artistas', json=data)

    assert response.status_code == 400
    assert response.json == {'messange': 'Erro ao gravar a musica no banco de dados'}

# Utiliza-se o mock para testar a criação de artista por chave estrangeira inválida
@mock.patch('src.routes.artista_routes.db')
def test_criar_artista_erro_chave_estrangeira(mock_db, client):
    # Simula um erro de chave estrangeira inválida
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1452)

    data = {
        'nome': 'Artista inválido',
        'gravadoras_id': 999
    }

    response = client.post('/artistas', json=data)

    assert response.status_code == 400
    assert response.json == {'message': 'Chave estrangeira inválida. Não é possível criar o artista.'}