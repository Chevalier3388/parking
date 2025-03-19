from flask import Blueprint, request, jsonify
from ..repositories.parking_repo import ParkingRepository  # Импортируем репозиторий

parkings_bp = Blueprint('parkings_bp', __name__)  # Создаем Blueprint для парковок

# Эндпоинт: Создание новой парковки
@parkings_bp.route('/', methods=['POST'])
def create_parking():
    data = request.get_json()  # Получаем данные из тела запроса
    print(f"\nАргументы: {data}")
    if not data:
        return jsonify({'error': 'No input data'}), 400  # Если нет данных, возвращаем ошибку

    if not data.get('address') or not data.get('count_places'):
        return jsonify({'error': 'Address and count_places are required'}), 400  # Обязательные поля

    new_parking = ParkingRepository.create_parking(data)  # Создаем парковку через репозиторий
    return jsonify(new_parking.to_dict()), 201  # Отправляем данные новой парковки


# Эндпоинт: Получения информации о парковке
@parkings_bp.route('/<int:parking_id>', methods=["GET"])
def get_check_parking(parking_id):
    parking = ParkingRepository.get_info_parking(parking_id)
    print(f"\nАргументы: {parking}")
    if parking:
        return jsonify(parking.to_dict())  # Отправляем данные клиента
    return jsonify({"message": "Парковка не найдена"}), 404  # Обработка случая, если клиент не найден
