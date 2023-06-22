from flask import Blueprint, request, jsonify
import mysql.connector

music_routes = Blueprint('music_routes', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicas"
)

# Rota para criar uma nova música
@music_routes.route('/musicas', methods=['POST'])
def criar_musica():
    nome = request.json['nome']
    duracao = request.json['duracao']
    generos_id = request.json['generos_id']
    lancamento = request.json['lancamento']
    
    try:
        cursor = db.cursor()
        sql = "INSERT INTO musicas (nome, duracao, generos_id, lancamento) VALUES (%s, %s, %s, %s)"
        val = (nome, duracao, generos_id, lancamento)
        cursor.execute(sql, val)
        db.commit()
        
        return jsonify({'message': 'Música criada com sucesso!'})
    except mysql.connector.Error as error:
        if error.errno == 1644:
            return jsonify({'messange': 'Erro ao gravar a musica no banco de dados'}), 400
        elif error.errno == 1452:
            return jsonify({'message': 'Chave estrangeira inválida. Não é possível criar a música.'}), 400

# Rota para obter todas as músicas
@music_routes.route('/musicas', methods=['GET'])
def obter_musicas():
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, duracao, generos_id, lancamento FROM musicasView")
    result = cursor.fetchall()
    
    musicas = []
    for musica in result:
        musicas.append({
            'id': musica[0],
            'nome': musica[1],
            'duracao': str(musica[2]),
            'generos_id': musica[3],
            'lancamento': str(musica[4])
        })
    
    return jsonify(musicas)

# Rota para obter uma música pelo ID
@music_routes.route('/musicas/<int:musica_id>', methods=['GET'])
def obter_musica(musica_id):
    cursor = db.cursor()
    sql = "SELECT id, nome, duracao, generos_id, lancamento FROM musicasView WHERE id = %s"
    val = (musica_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'messange': 'Música não encontrada'}), 404
    
    musica = {
        'id': result[0],
        'nome': result[1],
        'duracao': str(result[2]),
        'generos_id': result[3],
        'lancamento': str(result[4])
    }
    
    return jsonify(musica)

# Rota para atualizar uma música
@music_routes.route('/musicas/<int:musica_id>', methods=['PUT'])
def atualizar_musica(musica_id):
    cursor = db.cursor()
    sql = "SELECT id, nome, duracao, generos_id, lancamento FROM musicasView WHERE id = %s"
    val = (musica_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'messange': 'Música não encontrada'}), 404
    
    nome = request.json['nome']
    duracao = request.json['duracao']
    generos_id = request.json['generos_id']
    lancamento = request.json['lancamento']
    
    sql = "UPDATE musicas SET nome = %s, duracao = %s, generos_id = %s, lancamento = %s WHERE id = %s"
    val = (nome, duracao, generos_id, lancamento, musica_id)
    cursor.execute(sql, val)
    db.commit()
    
    return jsonify({'messange': 'Música atualizada com sucesso!'})

# Rota para excluir uma música
@music_routes.route('/musicas/<int:musica_id>', methods=['DELETE'])
def excluir_musica(musica_id):
    cursor = db.cursor()
    sql = "SELECT id FROM musicasView WHERE id = %s"
    val = (musica_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
        return jsonify({'messange': 'Música não encontrada'}), 404
    
    sql = "DELETE FROM musicas WHERE id = %s"
    val = (musica_id,)
    cursor.execute(sql, val)
    db.commit()
    
    return jsonify({'messange': 'Música excluída com sucesso!'})
