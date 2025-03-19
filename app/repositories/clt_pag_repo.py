from datetime import datetime
from sqlalchemy.orm import Session
from ..models import db, ClientParking, Parking, Client


class ClientParkingRepository:
    @staticmethod
    def enter_parking(client_id, parking_id):
        """Заезд клиента на парковку."""
        client = db.session.get(Client, client_id)
        parking = db.session.get(Parking, parking_id)

        if not client:
            return {"error": "Клиент не найден"}, 404
        if not parking:
            return {"error": "Парковка не найдена"}, 404
        if not parking.opened:
            return {"error": "Парковка закрыта"}, 400
        if parking.count_available_places <= 0:
            return {"error": "Нет свободных мест"}, 400

        # Создаем запись о въезде
        client_parking = ClientParking(client_id=client_id, parking_id=parking_id, time_in=datetime.now())
        db.session.add(client_parking)

        # Уменьшаем количество доступных мест
        parking.count_available_places -= 1

        db.session.commit()
        return {"message": "Заезд успешно зарегистрирован"}, 201

    @staticmethod
    def exit_parking(client_id, parking_id):
        """Выезд клиента с парковки."""


        client_parking = ClientParking.query.filter_by(client_id=client_id, parking_id=parking_id, time_out=None).first()
        parking = db.session.get(Parking, parking_id)
        client = db.session.get(Client, client_id)

        if not client:
            return {"error": "Клиент не найден"}, 404
        if not parking:
            return {"error": "Парковка не найдена"}, 404
        if not client_parking:
            return {"error": "Запись о въезде не найдена"}, 404

        # Фиксируем время выезда
        client_parking.time_out = datetime.now()

        # Освобождаем место
        parking.count_available_places += 1

        # Проверяем оплату
        if not client.credit_card:
            return {"error": "У клиента нет привязанной карты для оплаты"}, 400

        db.session.commit()
        return {"message": "Выезд успешно зарегистрирован, оплата произведена"}, 200
