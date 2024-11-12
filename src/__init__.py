from flask import Flask
from flask_restful import Api
from src.routes.Endpoints import initialize_endpoints
from src.model.Base import db
from src.model.Produto import Produto
from src.model.Cozinha import Cozinha
from src.model.Restaurante import Restaurante

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/pavFood'

    db.init_app(app)

    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app