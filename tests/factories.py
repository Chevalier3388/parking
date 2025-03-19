import factory
from faker import Faker
from app.models import db, Client, Parking, ClientParking

fake = Faker()

class ClientFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Фабрика для генерации клиентов"""
    class Meta:
        model = Client
        sqlalchemy_session = db.session  # Используем сессию SQLAlchemy

    name = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    credit_card = factory.Faker("credit_card_number")  # Генерируем номер карты
    car_number = factory.Faker("bothify", text="?###??")  # Генерация номера машины (например, A123CD)

    @factory.lazy_attribute
    def credit_card(self):
        """Либо есть кредитная карта, либо её нет"""
        return fake.credit_card_number() if fake.boolean(chance_of_getting_true=70) else None


class ParkingFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Фабрика для генерации парковок"""
    class Meta:
        model = Parking
        sqlalchemy_session = db.session

    address = factory.Faker("address")
    opened = factory.Faker("boolean")  # Генерируем True или False
    count_places = factory.Faker("random_int", min=10, max=100)

    @factory.lazy_attribute
    def count_available_places(self):
        """Свободные места равны общему количеству в начале"""
        return self.count_places
