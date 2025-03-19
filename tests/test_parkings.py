import pytest


# Сценарии для теста
@pytest.mark.parametrize("route, payload, expected_status_code, expected_response", [
    ("/parkings/", {"address": "Location 1", "count_places": 100}, 201, "Location 1"),  # Успешное создание
    ("/parkings/", {"address": "", "count_places": 100}, 400, "Address and count_places are required"),  # Ошибка: отсутствует адрес
    ("/parkings/", {"address": "Location 2", "count_places": ""}, 400, "Address and count_places are required"),  # Ошибка: отсутствует количество мест
    ("/parkings/", {}, 400, "No input data"),  # Ошибка: пустой запрос (исправили ожидаемое сообщение)
])
def test_create_parking(client, route, payload, expected_status_code, expected_response):
    """Тестируем, что POST-запрос для создания парковки возвращает правильный статус код и ответ"""

    # Выполняем POST-запрос с payload
    response = client.post(route, json=payload)

    # Проверяем, что статус код ответа соответствует ожидаемому
    assert response.status_code == expected_status_code

    # Проверяем, что в ответе содержится ожидаемое сообщение
    assert expected_response in response.get_data(as_text=True)


def test_create_parking_place(client):
    request = client.post("/parkings/", json={
        "address":"Address for test",
        "opened": True,
        "count_places": 20,
        "count_available_places": 20
    })
    assert request.status_code == 201
    response = client.get("/parkings/2")
    assert response.status_code == 200
    assert response.json == {"id": 2,
                             "address": "Address for test",
                             "opened": True,
                             "count_places": 20,
                             "count_available_places": 20
                             }

