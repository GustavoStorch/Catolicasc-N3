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


# Teste de integração com o bd para testar a criação de planos
def test_criar_plano(client):
    dados_plano = {
        'descricao': 'Plano de teste',
        'valor': 10.99,
        'limite': 100
    }

    response = client.post('/planos', json=dados_plano)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['messange'] == 'Plano criado com sucesso!'


# Teste de integração com o bd para testar a busca de planos
def test_obter_planos(client):
    response = client.get('/planos')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)

# Teste de integração com o bd para testar a busca de planos por id
def test_obter_plano_existente(client):
    # Em seguida, obtém o plano criado pelo seu ID
    response = client.get('/planos/8')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['id'] == 8

# Teste de integração com o bd para testar a busca de planos inexistentes
def test_obter_plano_nao_existente(client):
    response = client.get('/planos/999')

    assert response.status_code == 404
    assert 'Plano não encontrado' in response.json['messange']

# Teste de integração com o bd para testar o update de plano
def test_atualizar_plano(client):
    # Primeiro, cria um plano para testar
    dados_plano = {
        'descricao': 'Plano de teste atualizar',
        'valor': 9.0,
        'limite': 90
    }
    client.post('/planos', json=dados_plano)

    # Em seguida, atualiza o plano criado
    dados_atualizados = {
        'descricao': 'Novo plano de teste',
        'valor': 15.0,
        'limite': 200
    }
    response = client.put('/planos/9', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['messange'] == 'Plano atualizado com sucesso!'

# Teste de integração com o bd para testar o delete de planos
def test_excluir_plano(client):
    # Primeiro, cria um plano para testar
    dados_plano = {
        'descricao': 'Plano de teste excluir',
        'valor': 10.0,
        'limite': 100
    }
    client.post('/planos', json=dados_plano)

    # Em seguida, exclui o plano criado
    response = client.delete('/planos/10')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['messange'] == 'Plano excluído com sucesso!'
