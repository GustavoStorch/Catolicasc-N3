from flask import Blueprint, request, jsonify
import mysql.connector

clientes_routes = Blueprint('clientes_routes', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicas"
)

# Rota para criar um novo cliente
@clientes_routes.route('/clientes', methods=['POST'])
def criar_cliente():
    login = request.json['login']
    senha = request.json['senha']
    planos_id = request.json['planos_id']
    email = request.json['email']

    try:
        cursor = db.cursor()
        sql = "INSERT INTO clientes (login, senha, planos_id, email) VALUES (%s, %s, %s, %s)"
        val = (login, senha, planos_id, email)
        cursor.execute(sql, val)
        db.commit()

        return jsonify({'message': 'Cliente criado com sucesso!'}), 200  # Alterado para retornar 200
    except mysql.connector.Error as error:
        if error.errno == 1062:  # Adicionado tratamento para erro de chave duplicada
            return jsonify({'message': 'Login ou email já existente. Não é possível criar o cliente.'}), 400
        else:
            return jsonify({'message': 'Erro ao criar o cliente no banco de dados.'}), 400

# Rota para obter todos os clientes
@clientes_routes.route('/clientes', methods=['GET'])
def obter_clientes():
    cursor = db.cursor()
    cursor.execute("SELECT id, login, senha, planos_id, email FROM clientesView")
    result = cursor.fetchall()

    clientes = []
    for cliente in result:
        clientes.append({
            'id': cliente[0],
            'login': cliente[1],
            'senha': cliente[2],
            'planos_id': cliente[3],
            'email': cliente[4]
        })

    return jsonify(clientes)

# Rota para obter um cliente pelo ID
@clientes_routes.route('/clientes/<int:cliente_id>', methods=['GET'])
def obter_cliente(cliente_id):
    cursor = db.cursor()
    sql = "SELECT id, login, senha, planos_id, email FROM clientesView WHERE id = %s"
    val = (cliente_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Cliente não encontrado'}), 404

    cliente = {
        'id': result[0],
        'login': result[1],
        'senha': result[2],
        'planos_id': result[3],
        'email': result[4]
    }

    return jsonify(cliente)

# Rota para atualizar um cliente
@clientes_routes.route('/clientes/<int:cliente_id>', methods=['PUT'])
def atualizar_cliente(cliente_id):
    cursor = db.cursor()
    sql = "SELECT id, login, senha, planos_id, email FROM clientesView WHERE id = %s"
    val = (cliente_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Cliente não encontrado'}), 404

    login = request.json['login']
    senha = request.json['senha']
    planos_id = request.json['planos_id']
    email = request.json['email']

    sql = "UPDATE clientes SET login = %s, senha = %s, planos_id = %s, email = %s WHERE id = %s"
    val = (login, senha, planos_id, email, cliente_id)
    cursor.execute(sql, val)
    db.commit()

    return jsonify({'message': 'Cliente atualizado com sucesso!'})

# Rota para excluir um cliente
@clientes_routes.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def excluir_cliente(cliente_id):
    cursor = db.cursor()
    sql = "SELECT id FROM clientesView WHERE id = %s"
    val = (cliente_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Cliente não encontrado'}), 404

    sql = "DELETE FROM clientes WHERE id = %s"
    val = (cliente_id,)
    cursor.execute(sql, val)
    db.commit()

    return jsonify({'message': 'Cliente excluído com sucesso!'})