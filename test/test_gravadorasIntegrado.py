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

# Teste de integração com o BD para testar a criação de gravadoras
def test_criar_gravadora(client):
    dados_gravadora = {
        'nome': 'Gravadora de teste',
        'valor_contrato': 100000,
        'vencimento_contrato': '2023-12-31'
    }

    response = client.post('/gravadoras', json=dados_gravadora)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Gravadora criada com sucesso!'


# Teste de integração com o BD para testar a busca de gravadoras
def test_obter_gravadoras(client):
    response = client.get('/gravadoras')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)


# Teste de integração com o BD para testar a busca de gravadoras por ID
def test_obter_gravadora_existente(client):
    response = client.get('/gravadoras/6')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['id'] == 6


# Teste de integração com o BD para testar a busca de gravadoras inexistentes
def test_obter_gravadora_nao_existente(client):
    response = client.get('/gravadoras/999')

    assert response.status_code == 404
    assert 'Gravadora não encontrada' in response.json['message']


# Teste de integração com o BD para testar a atualização de gravadora
def test_atualizar_gravadora(client):
    # Primeiro, cria uma gravadora para testar
    dados_gravadora = {
        'nome': 'Gravadora de teste atualizar',
        'valor_contrato': 50000,
        'vencimento_contrato': '2024-06-30'
    }
    client.post('/gravadoras', json=dados_gravadora)

    # Em seguida, atualiza a gravadora criada
    dados_atualizados = {
        'nome': 'Nova gravadora de teste',
        'valor_contrato': 80000,
        'vencimento_contrato': '2025-01-01'
    }
    response = client.put('/gravadoras/7', json=dados_atualizados)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Gravadora atualizada com sucesso!'


# Teste de integração com o BD para testar a exclusão de gravadoras
def test_excluir_gravadora(client):
    # Primeiro, cria uma gravadora para testar
    dados_gravadora = {
        'nome': 'Gravadora de teste excluir',
        'valor_contrato': 200000,
        'vencimento_contrato': '2023-12-31'
    }
    client.post('/gravadoras', json=dados_gravadora)

    # Em seguida, exclui a gravadora criada
    response = client.delete('/gravadoras/8')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data['message'] == 'Gravadora excluída com sucesso!'
