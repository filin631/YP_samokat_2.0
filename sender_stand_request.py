import requests
import configuration
import data

# Cоздания нового заказа


def post_new_orders():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=data.orders_bode)

# Сохранения заказа и поиск по его треку


def scan_orders():
    response = post_new_orders()
    data_create = response.json()
    track_orders = data_create['track']
    return requests.get(configuration.URL_SERVICE + configuration.SCAN_ORDERS_PATH + str(track_orders))

# Проверка ответа на статус кода 200


def test_statys_code():
    response = scan_orders()
    assert response.status_code == 200




