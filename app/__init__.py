from flask import Flask
from pymongo import MongoClient
from .routes import api_blueprint
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # MongoDB connection
    client = MongoClient(app.config['MONGO_URI'])
    app.db = client[app.config['DATABASE_NAME']]

    # Register routes
    app.register_blueprint(api_blueprint)

    return app
