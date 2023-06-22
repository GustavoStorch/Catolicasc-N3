from flask import Blueprint, request, jsonify
import mysql.connector

planos_routes = Blueprint('planos_routes', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicas"
)

# Rota para criar um plano
@planos_routes.route('/planos', methods=['POST'])
def criar_plano():
    descricao = request.json['descricao']
    valor = request.json['valor']
    limite = request.json['limite']
    
    try:
        cursor = db.cursor()

        sql = "INSERT INTO planos (descricao, valor, limite) VALUES (%s, %s, %s)"
        val = (descricao, valor, limite)
        cursor.execute(sql, val)
        db.commit()
        
        return jsonify({'messange': 'Plano criado com sucesso!'})
    except mysql.connector.Error as error:
        if error.errno == 1644:
            return jsonify({'messange': 'Registro duplicado. Não é possível criar o plano.'}), 400

# Rota para obter todos os planos
@planos_routes.route('/planos', methods=['GET'])
def obter_planos():
    cursor = db.cursor()
    cursor.execute("SELECT id, descricao, valor, limite FROM planosView")
    result = cursor.fetchall()
    
    planos = []
    for plano in result:
        planos.append({
            'id': plano[0],
            'descricao': plano[1],
            'valor': plano[2],
            'limite': plano[3]
        })
    
    return jsonify(planos)

# Rota para obter um plano pelo ID
@planos_routes.route('/planos/<int:plano_id>', methods=['GET'])
def obter_plano(plano_id):
    cursor = db.cursor()
    sql = "SELECT id, descricao, valor, limite FROM planosView WHERE id = %s"
    val = (plano_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'messange': 'Plano não encontrado'}), 404
    
    plano = {
        'id': result[0],
        'descricao': result[1],
        'valor': result[2],
        'limite': result[3]
    }
    
    return jsonify(plano)

# Rota para atualizar um plano
@planos_routes.route('/planos/<int:plano_id>', methods=['PUT'])
def atualizar_plano(plano_id):
    cursor = db.cursor()
    sql = "SELECT id, descricao, valor, limite FROM planosView WHERE id = %s"
    val = (plano_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'messange': 'Plano não encontrado'}), 404
    
    descricao = request.json['descricao']
    valor = request.json['valor']
    limite = request.json['limite']
    
    sql = "UPDATE planos SET descricao = %s, valor = %s, limite = %s WHERE id = %s"
    val = (descricao, valor, limite, plano_id)
    cursor.execute(sql, val)
    db.commit()
    
    return jsonify({'messange': 'Plano atualizado com sucesso!'})

# Rota para excluir um plano
@planos_routes.route('/planos/<int:plano_id>', methods=['DELETE'])
def excluir_plano(plano_id):
    cursor = db.cursor()
    sql = "SELECT id FROM planosView WHERE id = %s"
    val = (plano_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'messange': 'Plano não encontrado'}), 404
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    sql = "DELETE FROM planos WHERE id = %s"
    val = (plano_id,)
    cursor.execute(sql, val)
    db.commit()
    
    return jsonify({'messange': 'Plano excluído com sucesso!'})