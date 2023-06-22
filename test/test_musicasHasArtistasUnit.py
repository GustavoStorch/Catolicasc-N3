import json
import pytest
import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from unittest import mock

from src.routes.musicas_has_artistas_routes import musicas_has_artistas_routes

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(musicas_has_artistas_routes)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Utiliza-se o mock para testar a associação de musicas e artistas
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_associar_musica_artista(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.execute.return_value = None
    mock_db.commit.return_value = None

    data = {
        'musicas_id': 1,
        'artistas_id': 1
    }

    response = client.post('/musicas_has_artistas', json=data)

    assert response.status_code == 200
    assert response.json == {'message': 'Associação entre música e artista criada com sucesso!'}

# Utiliza-se o mock para testar a busca de associações de musicas e artistas
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_obter_musicas_artistas(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 1),
        (2, 2)
    ]

    response = client.get('/musicas_has_artistas')

    assert response.status_code == 200
    assert response.json == [
        {
            'musicas_id': 1,
            'artistas_id': 1
        },
        {
            'musicas_id': 2,
            'artistas_id': 2
        }
    ]

# Utiliza-se o mock para testar a busca de musicas pelo artista
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_obter_musicas_por_artista(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 1),
        (1, 2)
    ]

    response = client.get('/musicas_has_artistas/musicas/1')

    assert response.status_code == 200
    assert response.json == [
        {
            'musica_id': 1,
            'artista_id': 1
        },
        {
            'musica_id': 1,
            'artista_id': 2
        }
    ]

# Utiliza-se o mock para testar a busca de artistas pela musica
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_obter_artistas_por_musica(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 1),
        (2, 1)
    ]

    response = client.get('/musicas_has_artistas/artistas/1')

    assert response.status_code == 200
    assert response.json == [
        {
            'musicas_id': 1,
            'artistas_id': 1
        },
        {
            'musicas_id': 2,
            'artistas_id': 1
        }
    ]

# Utiliza-se o mock para testar o delete de associação
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_excluir_relacionamento(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.rowcount = 1

    response = client.delete('/musicas_has_artistas/1/1')

    assert response.status_code == 200
    assert response.json == {'message': 'Relacionamento excluído com sucesso!'}

# Utiliza-se o mock para testar o delete de associação não encontrada
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_excluir_relacionamento_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.rowcount = 0

    response = client.delete('/musicas_has_artistas/1/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Relacionamento não encontrado'}

# Utiliza-se o mock para testar a associação por chave estrangeira inválida
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_associar_musica_artista_erro_chave_estrangeira(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1452)

    data = {
        'musicas_id': 1,
        'artistas_id': 1
    }

    response = client.post('/musicas_has_artistas', json=data)

    assert response.status_code == 400
    assert response.json == {'message': 'Chave estrangeira inválida. Não é possível criar a música.'}

@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_associar_musica_artista_erro_generico(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1644)

    data = {
        'musicas_id': 1,
        'artistas_id': 1
    }

    response = client.post('/musicas_has_artistas', json=data)

    assert response.status_code == 400
    assert response.json == {'message': 'Erro ao associar música e artista'}

# Utiliza-se o mock para testar a busca por artista inexistente
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_obter_musicas_por_artista_nao_encontrada(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = []

    response = client.get('/musicas_has_artistas/musicas/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Associação entre música e artista não encontrada'}

# Utiliza-se o mock para testar o delete de relacionamento não encontrado
@mock.patch('src.routes.musicas_has_artistas_routes.db')
def test_excluir_relacionamento_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.rowcount = 0

    response = client.delete('/musicas_has_artistas/1/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Relacionamento não encontrado'}