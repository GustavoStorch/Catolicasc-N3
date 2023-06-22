import json
import pytest
import mysql.connector
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from src.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste de integração com o bd para testar a criação de generos
def test_criar_genero(client):
    dados_genero = {
        'descricao': 'Genero de Teste'
    }

    response = client.post('/generos', json=dados_genero)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Gênero criado com sucesso!'

# Teste de integração com o bd para testar a busca de generos
def test_obter_generos(client):
    response = client.get('/generos')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)

# Teste de integração com o bd para testar a busca de generos por id
def test_obter_genero_existente(client):
    response = client.get('/generos/5')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'id' in data
    assert 'descricao' in data

# Teste de integração com o bd para testar a busca de generos inexistente
def test_obter_genero_inexistente(client):
    response = client.get('/generos/100')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Gênero não encontrado'

# Teste de integração com o bd para testar o update de generos
def test_atualizar_genero(client):
    dados_genero = {
        'descricao': 'Genero para atualizar'
    }
    client.post('/generos', json=dados_genero)

    dados_atualizados = {
        'descricao': 'Genero atualizado'
    }
    response = client.put('/generos/6', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Gênero atualizado com sucesso!'

# Teste de integração com o bd para testar o update de generos inexistente
def test_atualizar_genero_inexistente(client):
    dados_atualizados = {
        'descricao': 'Funk'
    }
    response = client.put('/generos/100', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Gênero não encontrado'

# Teste de integração com o bd para testar o delete de generos
def test_excluir_genero(client):
    # Primeiro, cria um gênero para testar
    dados_genero = {
        'descricao': 'Genero Excluir'
    }
    client.post('/generos', json=dados_genero)

    # Em seguida, exclui o gênero criado
    response = client.delete('/generos/7')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Gênero excluído com sucesso!'

# Teste de integração com o bd para testar o delete de generos inexistente
def test_excluir_genero_inexistente(client):
    response = client.delete('/generos/100')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Gênero não encontrado'
