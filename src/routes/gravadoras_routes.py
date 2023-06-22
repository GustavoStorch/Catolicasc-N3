from flask import Blueprint, request, jsonify
import mysql.connector

gravadoras_routes = Blueprint('gravadoras_routes', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicas"
)

# Rota para criar uma nova gravadora
@gravadoras_routes.route('/gravadoras', methods=['POST'])
def criar_gravadora():
    nome = request.json['nome']
    valor_contrato = request.json['valor_contrato']
    vencimento_contrato = request.json['vencimento_contrato']
    
    try:
        cursor = db.cursor()
        sql = "INSERT INTO gravadoras (nome, valor_contrato, vencimento_contrato) VALUES (%s, %s, %s)"
        val = (nome, valor_contrato, vencimento_contrato)
        cursor.execute(sql, val)
        db.commit()
        
        return jsonify({'message': 'Gravadora criada com sucesso!'})
    except mysql.connector.Error as error:
            if error.errno == 1644:
                return jsonify({'message': 'Registro duplicado. Não é possível criar a gravadora.'}), 400

# Rota para obter todas as gravadoras
@gravadoras_routes.route('/gravadoras', methods=['GET'])
def obter_gravadoras():
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, valor_contrato, vencimento_contrato FROM gravadoras")
    result = cursor.fetchall()
    
    gravadoras = []
    for gravadora in result:
        gravadoras.append({
            'id': gravadora[0],
            'nome': gravadora[1],
            'valor_contrato': gravadora[2],
            'vencimento_contrato': gravadora[3]
        })
    
    return jsonify(gravadoras)

# Rota para obter uma gravadora pelo ID
@gravadoras_routes.route('/gravadoras/<int:gravadora_id>', methods=['GET'])
def obter_gravadora(gravadora_id):
    cursor = db.cursor()
    sql = "SELECT id, nome, valor_contrato, vencimento_contrato FROM gravadorasView WHERE id = %s"
    val = (gravadora_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'message': 'Gravadora não encontrada'}), 404
    
    gravadora = {
        'id': result[0],
        'nome': result[1],
        'valor_contrato': result[2],
        'vencimento_contrato': result[3]
    }
    
    return jsonify(gravadora)

# Rota para atualizar uma gravadora
@gravadoras_routes.route('/gravadoras/<int:gravadora_id>', methods=['PUT'])
def atualizar_gravadora(gravadora_id):
    cursor = db.cursor()
    sql = "SELECT id, nome, valor_contrato, vencimento_contrato FROM gravadorasView WHERE id = %s"
    val = (gravadora_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'message': 'Gravadora não encontrada'}), 404
    
    nome = request.json['nome']
    valor_contrato = request.json['valor_contrato']
    vencimento_contrato = request.json['vencimento_contrato']
    
    sql = "UPDATE gravadoras SET nome = %s, valor_contrato = %s, vencimento_contrato = %s WHERE id = %s"
    val = (nome, valor_contrato, vencimento_contrato, gravadora_id)
    cursor.execute(sql, val)
    db.commit()
    
    return jsonify({'message': 'Gravadora atualizada com sucesso!'})

# Rota para excluir uma gravadora
@gravadoras_routes.route('/gravadoras/<int:gravadora_id>', methods=['DELETE'])
def excluir_gravadora(gravadora_id):
    cursor = db.cursor()
    sql = "SELECT id FROM gravadorasView WHERE id = %s"
    val = (gravadora_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'message': 'Gravadora não encontrada'}), 404
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    sql = "DELETE FROM gravadoras WHERE id = %s"
    val = (gravadora_id,)
    cursor.execute(sql, val)
    db.commit()
    
    return jsonify({'message': 'Gravadora excluída com sucesso!'})