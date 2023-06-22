from flask import Blueprint, request, jsonify
import mysql.connector

musicas_has_clientes_routes = Blueprint('musicas_has_clientes_routes', __name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicas"
)

# Rota para associar uma música a um cliente
@musicas_has_clientes_routes.route('/musicas_has_clientes', methods=['POST'])
def associar_musica_cliente():
    musicas_id = request.json['musicas_id']
    clientes_id = request.json['clientes_id']

    try:
        cursor = db.cursor()
        sql = "INSERT INTO musicas_has_clientes (musicas_id, clientes_id) VALUES (%s, %s)"
        val = (musicas_id, clientes_id)
        cursor.execute(sql, val)
        db.commit()

        return jsonify({'message': 'Associação entre música e cliente criada com sucesso!'})
    except mysql.connector.Error as error:
        if error.errno == 1644:
            return jsonify({'message': 'Erro ao associar música e cliente'}), 400
        elif error.errno == 1452:
            return jsonify({'message': 'Chave estrangeira inválida. Não é possível criar a associação.'}), 400

# Rota para obter todas as associações entre músicas e clientes
@musicas_has_clientes_routes.route('/musicas_has_clientes', methods=['GET'])
def obter_musicas_clientes():
    cursor = db.cursor()
    cursor.execute("SELECT musicas_id, clientes_id FROM musicasHasClientesView")
    result = cursor.fetchall()

    musicas_clientes = []
    for musica_cliente in result:
        musicas_clientes.append({
            'musicas_id': musica_cliente[0],
            'clientes_id': musica_cliente[1]
        })

    return jsonify(musicas_clientes)

# Rota para obter a associação entre música e cliente pelo ID da música
@musicas_has_clientes_routes.route('/musicas_has_clientes/musicas/<int:musicas_id>', methods=['GET'])
def obter_clientes_por_musica(musicas_id):
    cursor = db.cursor()
    sql = "SELECT musicas_id, clientes_id FROM musicasHasClientesView WHERE musicas_id = %s"
    val = (musicas_id,)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if not result:
        return jsonify({'message': 'Associação entre música e cliente não encontrada'}), 404

    musicas_clientes = []
    for musica_cliente in result:
        musicas_clientes.append({
            'musicas_id': musica_cliente[0],
            'clientes_id': musica_cliente[1]
        })

    return jsonify(musicas_clientes)

# Rota para obter a associação entre música e cliente pelo ID do cliente
@musicas_has_clientes_routes.route('/musicas_has_clientes/clientes/<int:clientes_id>', methods=['GET'])
def obter_musicas_por_cliente(clientes_id):
    cursor = db.cursor()
    sql = "SELECT musicas_id, clientes_id FROM musicasHasClientesView WHERE clientes_id = %s"
    val = (clientes_id,)
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if not result:
        return jsonify({'message': 'Associação entre música e cliente não encontrada'}), 404

    musicas_clientes = []
    for musica_cliente in result:
        musicas_clientes.append({
            'musicas_id': musica_cliente[0],
            'clientes_id': musica_cliente[1]
        })

    return jsonify(musicas_clientes)

# Rota para excluir um relacionamento entre música e cliente
@musicas_has_clientes_routes.route('/musicas_has_clientes/<int:musicas_id>/<int:clientes_id>', methods=['DELETE'])
def excluir_relacionamento(musicas_id, clientes_id):
    cursor = db.cursor()
    sql = "DELETE FROM musicas_has_clientes WHERE musicas_id = %s AND clientes_id = %s"
    val = (musicas_id, clientes_id)
    cursor.execute(sql, val)
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({'message': 'Relacionamento não encontrado'}), 404

    return jsonify({'message': 'Relacionamento excluído com sucesso!'})