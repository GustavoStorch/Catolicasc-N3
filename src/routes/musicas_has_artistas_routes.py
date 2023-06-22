from flask import Blueprint, request, jsonify
import mysql.connector

musicas_has_artistas_routes = Blueprint('musicas_has_artistas_routes', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicas"
)

# Rota para associar uma música a um artista
@musicas_has_artistas_routes.route('/musicas_has_artistas', methods=['POST'])
def associar_musica_artista():
    musicas_id = request.json['musicas_id']
    artistas_id = request.json['artistas_id']

    try:
        cursor = db.cursor()
        sql = "INSERT INTO musicas_has_artistas (musicas_id, artistas_id) VALUES (%s, %s)"
        val = (musicas_id, artistas_id)
        cursor.execute(sql, val)
        db.commit()

        return jsonify({'message': 'Associação entre música e artista criada com sucesso!'})
    except mysql.connector.Error as error:
        if error.errno == 1644:
            return jsonify({'message': 'Erro ao associar música e artista'}), 400
        elif error.errno == 1452:
            return jsonify({'message': 'Chave estrangeira inválida. Não é possível criar a música.'}), 400

# Rota para obter todas as associações entre músicas e artistas
@musicas_has_artistas_routes.route('/musicas_has_artistas', methods=['GET'])
def obter_musicas_artistas():
    cursor = db.cursor()
    cursor.execute("SELECT musicas_id, artistas_id FROM musicasHasArtistasView")
    result = cursor.fetchall()

    musicas_artistas = []
    for musica_artista in result:
        musicas_artistas.append({
            'musicas_id': musica_artista[0],
            'artistas_id': musica_artista[1]
        })

    return jsonify(musicas_artistas)

# Rota para obter a associação entre música e artista pelo ID da música
@musicas_has_artistas_routes.route('/musicas_has_artistas/musicas/<int:musicas_id>', methods=['GET'])
def obter_musicas_por_artista(musicas_id):
    cursor = db.cursor()
    sql = "SELECT musicas_id, artistas_id FROM musicasHasArtistasView WHERE musicas_id = %s"
    val = (musicas_id,)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if not result:
        return jsonify({'message': 'Associação entre música e artista não encontrada'}), 404

    musicas_artistas = []
    for musica_artista in result:
        musicas_artistas.append({
            'musica_id': musica_artista[0],
            'artista_id': musica_artista[1]
        })

    return jsonify(musicas_artistas)

# Rota para obter a associação entre música e artista pelo ID do artista
@musicas_has_artistas_routes.route('/musicas_has_artistas/artistas/<int:artistas_id>', methods=['GET'])
def obter_artistas_por_musica(artistas_id):
    cursor = db.cursor()
    sql = "SELECT musicas_id, artistas_id FROM musicasHasArtistasView WHERE artistas_id = %s"
    val = (artistas_id,)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if not result:
        return jsonify({'message': 'Associação entre música e artista não encontrada'}), 404

    musicas_artistas = []
    for musica_artista in result:
        musicas_artistas.append({
            'musicas_id': musica_artista[0],
            'artistas_id': musica_artista[1]
        })

    return jsonify(musicas_artistas)

# Rota para excluir um relacionamento entre música e artista
@musicas_has_artistas_routes.route('/musicas_has_artistas/<int:musicas_id>/<int:artistas_id>', methods=['DELETE'])
def excluir_relacionamento(musicas_id, artistas_id):
    cursor = db.cursor()
    sql = "DELETE FROM musicas_has_artistas WHERE musicas_id = %s AND artistas_id = %s"
    val = (musicas_id, artistas_id)
    cursor.execute(sql, val)
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({'message': 'Relacionamento não encontrado'}), 404

    return jsonify({'message': 'Relacionamento excluído com sucesso!'})