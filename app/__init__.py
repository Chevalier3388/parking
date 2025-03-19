from flask import Flask
from .config import Config
from .models import db
from .routes import api


def create_app():
    app = Flask(__name__)  # Создаем Flask-приложение

    app.config.from_object(Config)  # Загружаем конфигурацию

    db.init_app(app)  # Инициализируем SQLAlchemy с помощью init_app

    app.register_blueprint(api)  # Регистрируем Blueprint api

    return app  # Возвращаем готовое приложение