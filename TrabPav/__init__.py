from flask import Flask
from flask_restful import Api
from .endpoints import initialize_endpoints
from .models import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123@localhost:3306/new_schema'

    db.init_app(app)

    # Flask API
    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app