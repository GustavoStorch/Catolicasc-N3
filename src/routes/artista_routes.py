from flask import Blueprint, request, jsonify
import mysql.connector

artista_routes = Blueprint('artista_routes', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicas"
)

# Rota para criar um novo artista
@artista_routes.route('/artistas', methods=['POST'])
def criar_artista():
    nome = request.json['nome']
    gravadoras_id = request.json['gravadoras_id']

    try:
        cursor = db.cursor()
        sql = "INSERT INTO artistas (nome, gravadoras_id) VALUES (%s, %s)"
        val = (nome, gravadoras_id)
        cursor.execute(sql, val)
        db.commit()

        return jsonify({'message': 'Artista criado com sucesso!'})
    except mysql.connector.Error as error:
        if error.errno == 1644:
            return jsonify({'messange': 'Erro ao gravar a musica no banco de dados'}), 400
        elif error.errno == 1452:
            return jsonify({'message': 'Chave estrangeira inválida. Não é possível criar o artista.'}), 400
    
# Rota para obter todos os artistas
@artista_routes.route('/artistas', methods=['GET'])
def obter_artistas():
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, gravadoras_id FROM artistasView")
    result = cursor.fetchall()

    artistas = []
    for artista in result:
        artistas.append({
            'id': artista[0],
            'nome': artista[1],
            'gravadoras_id': artista[2]
        })

    return jsonify(artistas)

# Rota para obter um artista pelo ID
@artista_routes.route('/artistas/<int:artista_id>', methods=['GET'])
def obter_artista(artista_id):
    cursor = db.cursor()
    sql = "SELECT id, nome, gravadoras_id FROM artistasView WHERE id = %s"
    val = (artista_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Artista não encontrado'}), 404

    artista = {
        'id': result[0],
        'nome': result[1],
        'gravadoras_id': result[2]
    }

    return jsonify(artista)

# Rota para atualizar um artista
@artista_routes.route('/artistas/<int:artista_id>', methods=['PUT'])
def atualizar_artista(artista_id):
    cursor = db.cursor()
    sql = "SELECT id, nome, gravadoras_id FROM artistasView WHERE id = %s"
    val = (artista_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Artista não encontrado'}), 404

    nome = request.json['nome']
    gravadoras_id = request.json['gravadoras_id']

    sql = "UPDATE artistas SET nome = %s, gravadoras_id = %s WHERE id = %s"
    val = (nome, gravadoras_id, artista_id)
    cursor.execute(sql, val)
    db.commit()

    return jsonify({'message': 'Artista atualizado com sucesso!'})

# Rota para excluir um artista
@artista_routes.route('/artistas/<int:artista_id>', methods=['DELETE'])
def excluir_artista(artista_id):
    cursor = db.cursor()
    sql = "SELECT id FROM artistasView WHERE id = %s"
    val = (artista_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result is None:
        return jsonify({'message': 'Artista não encontrado'}), 404

    sql = "DELETE FROM artistas WHERE id = %s"
    val = (artista_id,)
    cursor.execute(sql, val)
    db.commit()

    return jsonify({'message': 'Artista excluído com sucesso!'})