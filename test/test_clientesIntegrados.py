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

# Teste de integração com o bd para testar a criação de clientes
def test_criar_cliente(client):
    dados_cliente = {
        'login': 'Cliente Teste',
        'senha': 'Teste',
        'planos_id': 2,
        'email': 'cliente_teste@teste.com'
    }

    response = client.post('/clientes', json=dados_cliente)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Cliente criado com sucesso!'

# Teste de integração com o bd para testar a busca de clientes
def test_obter_clientes(client):
    response = client.get('/clientes')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)

# Teste de integração com o bd para testar a busca de clientes por id
def test_obter_cliente_existente(client):
    response = client.get('/clientes/4')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'id' in data
    assert 'login' in data
    assert 'senha' in data
    assert 'planos_id' in data
    assert 'email' in data

# Teste de integração com o bd para testar a busca de cliente inexistentes
def test_obter_cliente_inexistente(client):
    response = client.get('/clientes/100')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Cliente não encontrado'

# Teste de integração com o bd para testar o update de cliente
def test_atualizar_cliente(client):
    dados_cliente = {
        'login': 'Ciente atualizar',
        'senha': 'atualizar',
        'planos_id': 3,
        'email': 'cliente_atualizar@teste.com'
    }
    client.post('/clientes', json=dados_cliente)

    dados_atualizados = {
        'login': 'Cliente atualizado',
        'senha': 'atualizado',
        'planos_id': 2,
        'email': 'cliente_atualizado@teste.com'
    }
    response = client.put('/clientes/5', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Cliente atualizado com sucesso!'

# Teste de integração com o bd para testar o update de cliente inexisente
def test_atualizar_cliente_inexistente(client):
    dados_atualizados = {
        'login': 'fulano',
        'senha': 'fulano',
        'planos_id': 2,
        'email': 'fulano@teste.com'
    }
    response = client.put('/clientes/100', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Cliente não encontrado'

# Teste de integração com o bd para testar o delete de cliente
def test_excluir_cliente(client):
    # Primeiro, cria um cliente para testar
    dados_cliente = {
        'login': 'Cliente excluir',
        'senha': 'excluir',
        'planos_id': 2,
        'email': 'cliente_excluir@teste.com'
    }
    client.post('/clientes', json=dados_cliente)

    response = client.delete('/clientes/6')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Cliente excluído com sucesso!'

# Teste de integração com o bd para testar o delete de cliente inexistente
def test_excluir_cliente_inexistente(client):
    response = client.delete('/clientes/100')
    data = json.loads(response.data)

    assert response.status_code == 404
    assert data['message'] == 'Cliente não encontrado'
