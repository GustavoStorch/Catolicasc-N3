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

# Teste de integração com o bd para testar a criação de música
def test_criar_musica(client):
    dados_musica = {
        'nome': 'Música Teste',
        'duracao': '3:45',
        'generos_id': 1,
        'lancamento': '2023-06-21'
    }

    response = client.post('/musicas', json=dados_musica)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Música criada com sucesso!'

# Teste de integração com o bd para testar a busca de músicas
def test_obter_musicas(client):
    response = client.get('/musicas')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)

# Teste de integração com o bd para testar a busca de músicas por id
def test_obter_musica_existente(client):
    response = client.get('/musicas/21')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'id' in data
    assert 'nome' in data
    assert 'duracao' in data
    assert 'generos_id' in data
    assert 'lancamento' in data

# Teste de integração com o bd para testar a busca de músicas inexistentes
def test_obter_musica_inexistente(client):
    response = client.get('/musicas/100')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['messange'] == 'Música não encontrada'

# Teste de integração com o bd para testar a atualização de música
def test_atualizar_musica(client):
    dados_musica = {
        'nome': 'Música Atualizar',
        'duracao': '4:30',
        'generos_id': 2,
        'lancamento': '2022-01-01'
    }
    client.post('/musicas', json=dados_musica)

    dados_atualizados = {
        'nome': 'Música Atualizada',
        'duracao': '3:15',
        'generos_id': 1,
        'lancamento': '2023-06-21'
    }
    response = client.put('/musicas/22', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['messange'] == 'Música atualizada com sucesso!'

# Teste de integração com o bd para testar a atualização de música inexistente
def test_atualizar_musica_inexistente(client):
    dados_atualizados = {
        'nome': 'Música Inexistente',
        'duracao': '5:00',
        'generos_id': 1,
        'lancamento': '2023-06-21'
    }
    response = client.put('/musicas/100', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['messange'] == 'Música não encontrada'

# Teste de integração com o bd para testar a exclusão de música
def test_excluir_musica(client):
    # Primeiro, cria uma música para testar
    dados_musica = {
        'nome': 'Música Excluir',
        'duracao': '3:30',
        'generos_id': 1,
        'lancamento': '2023-06-21'
    }
    client.post('/musicas', json=dados_musica)

    response = client.delete('/musicas/23')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['messange'] == 'Música excluída com sucesso!'

# Teste de integração com o bd para testar a exclusão de música inexistente
def test_excluir_musica_inexistente(client):
    response = client.delete('/musicas/100')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['messange'] == 'Música não encontrada'
