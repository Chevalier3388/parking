from ..models import Client, db  # Импортируем модель клиента и db


# Репозиторий для работы с клиентами
class ClientRepository:

    @staticmethod
    def get_all_clients():
        """Получить всех клиентов из базы данных."""
        return Client.query.all()

    @staticmethod
    def get_client_by_id(client_id):
        """Получить клиента по ID."""
        client = db.session.get(Client, client_id)
        if client:
            return client
        else:
            return None

    @staticmethod
    def create_client(data):
        """Создать нового клиента и сохранить в базе данных."""
        new_client = Client(
            name=data.get('name'),
            surname=data.get('surname'),
            credit_card=data.get('credit_card'),
            car_number=data.get('car_number')
        )
        db.session.add(new_client)  # Добавляем в сессию
        db.session.commit()  # Сохраняем изменения в базе данных
        return new_client