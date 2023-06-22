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

# Teste de integração com o bd para testar a criação de artista
def test_criar_artista(client):
    dados_artista = {
        'nome': 'Artista teste',
        'gravadoras_id': 1
    }

    response = client.post('/artistas', json=dados_artista)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Artista criado com sucesso!'

# Teste de integração com o bd para testar a busca de artistas
def test_obter_artistas(client):
    response = client.get('/artistas')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)

# Teste de integração com o bd para testar a busca de artista por id
def test_obter_artista_existente(client):
    response = client.get('/artistas/20')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'id' in data
    assert 'nome' in data
    assert 'gravadoras_id' in data

# Teste de integração com o bd para testar a busca de artista inexistentes
def test_obter_artista_inexistente(client):
    response = client.get('/artistas/100')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Artista não encontrado'

# Teste de integração com o bd para testar o update de artista
def test_atualizar_artista(client):
    dados_artista = {
        'nome': 'Artista atualizar',
        'gravadoras_id': 1
    }
    client.post('/artistas', json=dados_artista)

    dados_atualizados = {
        'nome': 'Artista Atualizado',
        'gravadoras_id': 2
    }
    response = client.put('/artistas/21', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Artista atualizado com sucesso!'

# Teste de integração com o bd para testar o update de artista inexistente
def test_atualizar_artista_inexistente(client):
    dados_atualizados = {
        'nome': 'Fulano',
        'gravadoras_id': 1
    }
    response = client.put('/artistas/100', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Artista não encontrado'

# Teste de integração com o bd para testar o delete de artistas
def test_excluir_artista(client):
    dados_artista = {
        'nome': 'Artista Excluir',
        'gravadoras_id': 1
    }
    client.post('/artistas', json=dados_artista)

    response = client.delete('/artistas/22')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Artista excluído com sucesso!'

# Teste de integração com o bd para testar o delete de artistas inexistentes
def test_excluir_artista_inexistente(client):
    response = client.delete('/artistas/100')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Artista não encontrado'
