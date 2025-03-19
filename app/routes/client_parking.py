from flask import Blueprint, request, jsonify
from ..repositories.clt_pag_repo import ClientParkingRepository

client_parking_bp = Blueprint('client_parking_bp', __name__)  # Создаем Blueprint

# Эндпоинт: Заезд на парковку
@client_parking_bp.route("/", methods=["POST"])
def enter_parking():
    data = request.get_json()
    print(f"\nАргументы: {data}")
    client_id = data.get("client_id")
    parking_id = data.get("parking_id")

    result, status_code = ClientParkingRepository.enter_parking(client_id, parking_id)
    return jsonify(result), status_code  # Возвращаем результат


# Эндпоинт: Выезд с парковки
@client_parking_bp.route("/", methods=["DELETE"])
def exit_parking():
    data = request.get_json()
    print(f"\nАргументы: {data}")  # Отладочный вывод

    if not data or "client_id" not in data or "parking_id" not in data:
        return jsonify({"error": "Не валидные данные"}), 400  # Возвращаем 400, если данные некорректны
    client_id = data.get("client_id")
    parking_id = data.get("parking_id")

    result, status_code = ClientParkingRepository.exit_parking(client_id, parking_id)
    return jsonify(result), status_code  # Возвращаем результат
