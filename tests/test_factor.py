from tests.factories import  ClientFactory, ParkingFactory

def test_create_client_using_factory(app, client):
    """Тест создания клиента через ClientFactory."""

    # Создаем клиента с помощью фабрики
    client_obj = ClientFactory()

    # Отправляем запрос на создание клиента (если необходимо)
    response = client.post("/clients/", json={
        "name": client_obj.name,
        "surname": client_obj.surname,
        "credit_card": client_obj.credit_card,
        "car_number": client_obj.car_number
    })

    # Проверяем, что статус 201 (создано)
    assert response.status_code == 201

    # Проверяем, что в ответе есть id клиента
    assert "id" in response.json
    assert response.json["name"] == client_obj.name
    assert response.json["surname"] == client_obj.surname
    assert response.json["credit_card"] in [client_obj.credit_card, ""]
    assert response.json["car_number"] == client_obj.car_number




def test_create_parking_using_factory(app, client):
    """Тест создания парковки через ParkingFactory."""

    # Создаем парковку с помощью фабрики
    parking_obj = ParkingFactory()

    # Отправляем запрос на создание парковки (если необходимо)
    response = client.post("/parkings/", json={
        "address": parking_obj.address,
        "opened": parking_obj.opened,
        "count_places": parking_obj.count_places,
        "count_available_places": parking_obj.count_available_places
    })

    # Проверяем, что статус 201 (создано)
    assert response.status_code == 201

    # Проверяем, что в ответе есть id парковки
    assert "id" in response.json
    assert response.json["address"] == parking_obj.address
    assert response.json["opened"] == parking_obj.opened
    assert response.json["count_places"] == parking_obj.count_places
    assert response.json["count_available_places"] == parking_obj.count_available_places
