import json
import pytest
import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from unittest import mock

from src.routes.music_routes import music_routes

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(music_routes)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Utiliza-se o mock para testar a criação de musicas
@mock.patch('src.routes.music_routes.db')
def test_criar_musica(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.execute.return_value = None
    mock_db.commit.return_value = None

    data = {
        'nome': 'Música de teste',
        'duracao': '3:30',
        'generos_id': 1,
        'lancamento': '2023-06-30'
    }

    response = client.post('/musicas', json=data)

    assert response.status_code == 200
    assert response.json == {'message': 'Música criada com sucesso!'}

# Utiliza-se o mock para testar a busca de musicas
@mock.patch('src.routes.music_routes.db')
def test_obter_musicas(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 'Música 1', '3:30', 1, '2023-06-30'),
        (2, 'Música 2', '4:15', 2, '2023-07-31')
    ]

    response = client.get('/musicas')

    assert response.status_code == 200
    assert response.json == [
        {
            'id': 1,
            'nome': 'Música 1',
            'duracao': '3:30',
            'generos_id': 1,
            'lancamento': '2023-06-30'
        },
        {
            'id': 2,
            'nome': 'Música 2',
            'duracao': '4:15',
            'generos_id': 2,
            'lancamento': '2023-07-31'
        }
    ]

# Utiliza-se o mock para testar a busca de musicas por id
@mock.patch('src.routes.music_routes.db')
def test_obter_musica(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Música 1', '3:30', 1, '2023-06-30')

    response = client.get('/musicas/1')

    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'nome': 'Música 1',
        'duracao': '3:30',
        'generos_id': 1,
        'lancamento': '2023-06-30'
    }

# Utiliza-se o mock para testar o update do musicas
@mock.patch('src.routes.music_routes.db')
def test_atualizar_musica(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Música existente', '3:30', 1, '2023-06-30')

    response = client.put('/musicas/1', json={
        'nome': 'Música atualizada',
        'duracao': '4:00',
        'generos_id': 2,
        'lancamento': '2023-07-31'
    })

    assert response.status_code == 200
    assert response.json == {'messange': 'Música atualizada com sucesso!'}

# Utiliza-se o mock para testar o delete de musicas
@mock.patch('src.routes.music_routes.db')
def test_excluir_musica(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1,)

    response = client.delete('/musicas/1')

    assert response.status_code == 200
    assert response.json == {'messange': 'Música excluída com sucesso!'}

# Utiliza-se o mock para testar a busca de musica por id inexistente
@mock.patch('src.routes.music_routes.db')
def test_obter_musica_nao_encontrada(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.get('/musicas/1')

    assert response.status_code == 404
    assert response.json == {'messange': 'Música não encontrada'}

# Utiliza-se o mock para testar o update de musica inexistente
@mock.patch('src.routes.music_routes.db')
def test_atualizar_musica_nao_encontrada(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.put('/musicas/1', json={
        'nome': 'Música atualizada',
        'duracao': '4:00',
        'generos_id': 2,
        'lancamento': '2023-07-31'
    })

    assert response.status_code == 404
    assert response.json == {'messange': 'Música não encontrada'}

# Utiliza-se o mock para testar o delete de musica inexistente
@mock.patch('src.routes.music_routes.db')
def test_excluir_musica_nao_encontrada(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.delete('/musicas/1')

    assert response.status_code == 404
    assert response.json == {'messange': 'Música não encontrada'}

# Utiliza-se o mock para testar a criação de musica duplicada
@mock.patch('src.routes.music_routes.db')
def test_criar_musica_erro_registro_duplicado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1644)

    data = {
        'nome': 'Música duplicada',
        'duracao': '3:30',
        'generos_id': 1,
        'lancamento': '2023-06-30'
    }

    response = client.post('/musicas', json=data)

    assert response.status_code == 400
    assert response.json == {'messange': 'Erro ao gravar a musica no banco de dados'}

# Utiliza-se o mock para testar a criação de musica por chave estrangeira inválida
@mock.patch('src.routes.music_routes.db')
def test_criar_musica_erro_chave_estrangeira(mock_db, client):
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1452)

    data = {
        'nome': 'Música inválida',
        'duracao': '3:30',
        'generos_id': 999,
        'lancamento': '2023-06-30'
    }

    response = client.post('/musicas', json=data)

    assert response.status_code == 400
    assert response.json == {'message': 'Chave estrangeira inválida. Não é possível criar a música.'}
