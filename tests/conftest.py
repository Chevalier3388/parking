import pytest
import os
from app import create_app
from app.models import db as database, Client, Parking, ClientParking
from datetime import datetime


# Фикстура app
@pytest.fixture
def app():
    _app = create_app()  # Создаём Flask-приложение
    _app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'  # Используем SQLite для тестов
    _app.config['TESTING'] = True

    with _app.app_context():
        print("\nСбрасываем все таблицы")  # Сообщение для отладки
        database.drop_all()  # Удаляем все таблицы из базы данных (если они есть)

        print("Создаём новые таблицы")  # Сообщение для отладки
        database.create_all()  # Создаем таблицы

        # Добавляем тестового клиента
        user = Client(id=1,
                      name="John",
                      surname="Doe",
                      credit_card="12345",
                      car_number="А123АА")
        database.session.add(user)  # Добавляем клиента в сессию
        database.session.commit()  # Сохраняем изменения в базе данных

        # Добавляем парковку
        parking = Parking(id=1,
                          address="Main Parking",
                          count_places=50,
                          count_available_places=50)
        database.session.add(parking)
        database.session.commit()

        # Добавляем парковочный лог (время въезда)
        client_parking = ClientParking(id=1,
                                       client_id=1,
                                       parking_id=1,
                                       time_in=datetime.now(),
                                       time_out=None)
        database.session.add(client_parking)
        database.session.commit()


        yield _app  # Возвращаем объект Flask-приложения для тестов

        database.session.close()  # Закрываем сессию
        database.drop_all()  # Удаляем все таблицы (очищаем базу данных)





@pytest.fixture
def client(app):
    # Создаём клиент для отправки запросов
    client = app.test_client()
    yield client


@pytest.fixture
def db(app):
    # with app.app_context():
    yield database

