from flask import Blueprint

# Создаём Blueprint API
api = Blueprint('api', __name__)

# Подключаем модули с роутами
from .clients import clients_bp
from .parkings import parkings_bp
from .client_parking import client_parking_bp

# Регистрируем их в основном Blueprint
api.register_blueprint(clients_bp, url_prefix="/clients")
api.register_blueprint(parkings_bp, url_prefix="/parkings")
api.register_blueprint(client_parking_bp, url_prefix="/client_parkings")
