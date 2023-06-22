import json
import pytest
import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from unittest import mock

from src.routes.generos_routes import generos_routes

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(generos_routes)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

# Utiliza-se o mock para testar a criação de generos
@mock.patch('src.routes.generos_routes.db')
def test_criar_genero(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.execute.return_value = None
    mock_db.commit.return_value = None

    data = {
        'descricao': 'Gênero de teste',
    }

    response = client.post('/generos', json=data)

    assert response.status_code == 200
    assert response.json == {'message': 'Gênero criado com sucesso!'}

# Utiliza-se o mock para testar a busca de generos
@mock.patch('src.routes.generos_routes.db')
def test_obter_generos(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchall.return_value = [
        (1, 'Gênero 1'),
        (2, 'Gênero 2')
    ]

    response = client.get('/generos')

    assert response.status_code == 200
    assert response.json == [
        {
            'id': 1,
            'descricao': 'Gênero 1'
        },
        {
            'id': 2,
            'descricao': 'Gênero 2'
        }
    ]

# Utiliza-se o mock para testar a busca de genero por id
@mock.patch('src.routes.generos_routes.db')
def test_obter_genero(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Gênero 1')

    response = client.get('/generos/1')

    assert response.status_code == 200
    assert response.json == {
        'id': 1,
        'descricao': 'Gênero 1'
    }

# Utiliza-se o mock para testar o update do genero
@mock.patch('src.routes.generos_routes.db')
def test_atualizar_genero(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1, 'Gênero existente')

    response = client.put('/generos/1', json={
        'descricao': 'Gênero atualizado'
    })

    assert response.status_code == 200
    assert response.json == {'message': 'Gênero atualizado com sucesso!'}

# Utiliza-se o mock para testar o delete de genero
@mock.patch('src.routes.generos_routes.db')
def test_excluir_genero(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = (1,)

    response = client.delete('/generos/1')

    assert response.status_code == 200
    assert response.json == {'message': 'Gênero excluído com sucesso!'}

# Utiliza-se o mock para testar a busca de genero por id inexistente
@mock.patch('src.routes.generos_routes.db')
def test_obter_genero_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.get('/generos/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Gênero não encontrado'}

# Utiliza-se o mock para testar o update de genero inexistente
@mock.patch('src.routes.generos_routes.db')
def test_atualizar_genero_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.put('/generos/1', json={
        'descricao': 'Gênero atualizado'
    })

    assert response.status_code == 404
    assert response.json == {'message': 'Gênero não encontrado'}

# Utiliza-se o mock para testar o delete de genero inexistente
@mock.patch('src.routes.generos_routes.db')
def test_excluir_genero_nao_encontrado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value

    mock_cursor.fetchone.return_value = None

    response = client.delete('/generos/1')

    assert response.status_code == 404
    assert response.json == {'message': 'Gênero não encontrado'}
    
# Utiliza-se o mock para testar a criação de genero duplicado
@mock.patch('src.routes.generos_routes.db')
def test_criar_genero_registro_duplicado(mock_db, client):
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = mysql.connector.Error(errno=1644)

    response = client.post('/generos', json={'descricao': 'Gênero de teste'})

    assert response.status_code == 400
    assert response.json == {'message': 'Registro duplicado. Não é possível criar o genero.'}
