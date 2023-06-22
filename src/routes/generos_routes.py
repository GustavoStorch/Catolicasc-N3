from flask import Blueprint, request, jsonify
import mysql.connector

generos_routes = Blueprint('generos_routes', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicas"
)

# Rota para criar um novo gênero
@generos_routes.route('/generos', methods=['POST'])
def criar_genero():
    descricao = request.json['descricao']

    try:
        cursor = db.cursor()
        sql = "INSERT INTO generos (descricao) VALUES (%s)"
        val = (descricao,)
        cursor.execute(sql, val)
        db.commit()

        return jsonify({'message': 'Gênero criado com sucesso!'})
    except mysql.connector.Error as error:
            if error.errno == 1644:
                return jsonify({'message': 'Registro duplicado. Não é possível criar o genero.'}), 400

# Rota para obter todos os gêneros
@generos_routes.route('/generos', methods=['GET'])
def obter_generos():
    cursor = db.cursor()
    cursor.execute("SELECT id, descricao FROM generosView")
    result = cursor.fetchall()

    generos = []
    for genero in result:
        generos.append({
            'id': genero[0],
            'descricao': genero[1]
        })

    return jsonify(generos)

# Rota para obter um gênero pelo ID
@generos_routes.route('/generos/<int:genero_id>', methods=['GET'])
def obter_genero(genero_id):
    cursor = db.cursor()
    sql = "SELECT id, descricao FROM generosView WHERE id = %s"
    val = (genero_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Gênero não encontrado'}), 404

    genero = {
        'id': result[0],
        'descricao': result[1]
    }

    return jsonify(genero)

# Rota para atualizar um gênero
@generos_routes.route('/generos/<int:genero_id>', methods=['PUT'])
def atualizar_genero(genero_id):
    cursor = db.cursor()
    sql = "SELECT id, descricao FROM generosView WHERE id = %s"
    val = (genero_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Gênero não encontrado'}), 404

    descricao = request.json['descricao']

    sql = "UPDATE generos SET descricao = %s WHERE id = %s"
    val = (descricao, genero_id)
    cursor.execute(sql, val)
    db.commit()

    return jsonify({'message': 'Gênero atualizado com sucesso!'})

# Rota para excluir um gênero
@generos_routes.route('/generos/<int:genero_id>', methods=['DELETE'])
def excluir_genero(genero_id):
    cursor = db.cursor()
    sql = "SELECT id FROM generos WHERE id = %s"
    val = (genero_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Gênero não encontrado'}), 404
    
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    sql = "DELETE FROM generos WHERE id = %s"
    val = (genero_id,)
    cursor.execute(sql, val)
    db.commit()

    return jsonify({'message': 'Gênero excluído com sucesso!'})