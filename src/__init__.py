from flask import Flask
from flask_restful import Api
from src.routes.Endpoints import initialize_endpoints
from src.model.Base import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3101@localhost:5432/pavFood'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app
