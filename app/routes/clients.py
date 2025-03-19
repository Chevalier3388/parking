from flask import Blueprint, request, jsonify
from ..repositories.client_repo import ClientRepository # Импортируем репозиторий


clients_bp = Blueprint('clients_bp', __name__)  # Создаём Blueprint для клиентов


@clients_bp.route("/", methods=["GET"])
def get_clients():
    clients = ClientRepository.get_all_clients()  # Вызываем метод репозитория
    clients_list = [client.to_dict() for client in clients]  # Преобразуем в список словарей
    return jsonify(clients_list)  # Отправляем список клиентов в ответе


# Эндпоинт: Информация клиента по ID
@clients_bp.route('/<int:client_id>', methods=['GET'])
def get_client_by_id(client_id):
    client = ClientRepository.get_client_by_id(client_id)  # Вызываем метод репозитория
    if client:
        return jsonify(client.to_dict())  # Отправляем данные клиента
    return jsonify({"message": "Client not found"}), 404  # Обработка случая, если клиент не найден


# Эндпоинт: Создание нового клиента
@clients_bp.route('/', methods=['POST'])
def create_client():
    data = request.get_json()  # Получаем данные из тела запроса
    print(f"\nАргументы: {data}")
    if not data:
        return jsonify({'error': 'No input data'}), 400  # Проверяем, если данных нет

    # Проверяем обязательные поля
    if not data.get('name') or not data.get('surname'):
        return jsonify({'error': 'Name and surname are required'}), 400

    new_client = ClientRepository.create_client(data)  # Создаем клиента, передаем весь словарь
    return jsonify(new_client.to_dict()), 201  # Отправляем данные нового клиента