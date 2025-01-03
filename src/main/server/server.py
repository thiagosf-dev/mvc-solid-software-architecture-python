from flask import Flask
from flask_cors import CORS
from ..routes.pets_routes import pet_route_bp
from ..routes.person_routes import person_route_bp
from ...models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)

app.register_blueprint(pet_route_bp)
app.register_blueprint(person_route_bp)

CORS(app)
