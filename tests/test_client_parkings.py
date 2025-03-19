
import pytest

@pytest.mark.parametrize("payload, expected_status_code", [
    ({"client_id": 1, "parking_id": 1}, 200),  # Успешный выезд
    ({"client_id": 999, "parking_id": 1}, 404),  # Ошибка: клиент не найден
    ({"client_id": 1, "parking_id": 999}, 404),  # Ошибка: парковка не найдена
    ({}, 400),  # Ошибка: пустой запрос
])
def test_exit_parking(client, payload, expected_status_code):
    """Тестируем различные сценарии выезда клиента с парковки"""

    # Отправляем DELETE-запрос на выезд
    response = client.delete("/client_parkings/", json=payload)

    # Проверяем, что статус код соответствует ожидаемому
    assert response.status_code == expected_status_code


@pytest.mark.parking
def test_enter_parking(client):
    """Тест заезда клиента на парковку."""

    request = client.post("/client_parkings/", json={
        "client_id": 1,
        "parking_id": 1
    })

    assert request.status_code == 201
    assert request.json == {"message": "Заезд успешно зарегистрирован"}

    response = client.get("/parkings/1")
    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["count_available_places"] == 49


@pytest.mark.parking
def test_out_parking(client):
    """Тест выезда клиента с парковки."""

    enter_request = client.post("/client_parkings/", json={
        "client_id": 1,
        "parking_id": 1
    })

    assert enter_request.status_code == 201
    assert enter_request.json == {"message": "Заезд успешно зарегистрирован"}

    # Клиент покидает парковку
    exit_request = client.delete("/client_parkings/", json={
        "client_id": 1,
        "parking_id": 1
    })
    assert exit_request.status_code == 200
    assert exit_request.json == {"message": "Выезд успешно зарегистрирован, оплата произведена"}

    # Проверяем, что место освободилось
    response = client.get("/parkings/1")
    assert response.status_code == 200
    assert response.json["count_available_places"] == 50