from ..models import Parking, db
from sqlalchemy.orm import Session

class ParkingRepository:

    @staticmethod
    def create_parking(data):
        """Создать новую парковку и сохранить в базе данных."""
        new_parking = Parking(
            address=data.get('address'),
            opened=data.get('opened', True),  # Если не указано, по умолчанию парковка открыта
            count_places=data.get('count_places'),
            count_available_places=data.get('count_places')  # Изначально все места доступны
        )
        db.session.add(new_parking)  # Добавляем в сессию
        db.session.commit()  # Сохраняем изменения в базе данных
        return new_parking

    @staticmethod
    def get_all_parkings():
        """Получить список всех парковок."""
        return Parking.query.all()


    @staticmethod
    def get_info_parking(parking_id):
        """Получить парковку по ID."""
        parking = db.session.get(Parking, parking_id)
        if parking:
            return parking
        return {"message": "Парковка не найдена"}, 404
