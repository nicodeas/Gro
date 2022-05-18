from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .models import db
from .apps.test_server.routes import test_bp
from flask_login import LoginManager


def register_bp(app):
    # add blueprints to this list
    blueprints = [test_bp]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app,db)
    register_bp(app)
    return app

login = LoginManager(app)