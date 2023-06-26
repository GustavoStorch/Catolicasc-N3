from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.routes.music_routes import music_routes
from src.routes.generos_routes import generos_routes
from src.routes.artista_routes import artista_routes
from src.routes.gravadoras_routes import gravadoras_routes
from src.routes.clientes_routes import clientes_routes
from src.routes.planos_routes import planos_routes
from src.routes.musicas_has_artistas_routes import musicas_has_artistas_routes
from src.routes.musicas_has_clientes_routes import musicas_has_clientes_routes

app = Flask(__name__)

app.register_blueprint(music_routes)

app.register_blueprint(generos_routes)

app.register_blueprint(artista_routes)

app.register_blueprint(gravadoras_routes)

app.register_blueprint(clientes_routes)

app.register_blueprint(planos_routes)

app.register_blueprint(musicas_has_artistas_routes)

app.register_blueprint(musicas_has_clientes_routes)

if __name__ == '__main__':
    app.run()