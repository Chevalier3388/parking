import pytest


def test_get_users(client) -> None:
    resp = client.get("/clients/")

    assert resp.status_code == 200
    assert isinstance(resp.json, list)  # Проверяем, что это список

    # Должен быть хотя бы один клиент
    assert len(resp.json) > 0
    assert resp.json[0]["name"] == "John"



def test_get_user_for_id(client) -> None:
    resp = client.get("/clients/1")
    assert resp.status_code == 200
    assert resp.json == {"id": 1,
                         "name": "John",
                         "surname": "Doe",
                         "credit_card":"12345",
                         "car_number":"А123АА"}


@pytest.mark.parametrize("route, expected_status_code", [
    ("/clients/", 200),  # Проверка GET для всех клиентов
    ("/clients/1", 200),  # Проверка GET для конкретного клиента
])
def test_get_routes(client, route, expected_status_code):
    """Тестируем, что GET-запросы на различные маршруты возвращают статус 200"""

    # Выполняем GET-запрос
    response = client.get(route)

    # Проверяем, что статус код ответа соответствует ожидаемому
    assert response.status_code == expected_status_code


def test_create_user(client):

    # Выполняем POST-запрос
    request = client.post("/clients/", json={"name": "Name",
                         "surname": "Surname",
                         "credit_card":"54321",
                         "car_number":"О101ОО"})
    assert request.status_code == 201

    response = client.get("/clients/2")
    assert response.status_code == 200
    assert response.json == {"id": 2,
                         "name": "Name",
                         "surname": "Surname",
                         "credit_card":"54321",
                         "car_number":"О101ОО"}



