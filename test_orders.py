#Екатерина Кундиус, 35 когорта, Финальный проект. Инженер по тетированию.


import pytest  # Для фреймворка тестирования
from sender_stand_request import post_new_order, get_orders_track # Импорт функций из sender_stand_request.py

def test_order_creation():
    # Создаём заказ (POST /api/v1/orders)
    creation_response = post_new_order()  # Вызываем функцию
    print("Ответ на создание заказа:", creation_response.json())  # Отладка: вывод ответа
    assert creation_response.status_code == 201  # Проверяем статус — заказ создан успешно
    
    # Получаем track_id из ответа на создание
    track_id = creation_response.json()['track']  # Извлекаем трек-номер
    
    # Получаем заказ по треку (GET /api/v1/orders/track)
    response = get_orders_track(track_id)  # Теперь функция импортирована и доступна
    print("Ответ на получение заказа:", response.json())  # Отладка: вывод ответа
    assert response.status_code == 200  # Проверяем статус — заказ найден
    
    # Дополнительные проверки (пример: убедимся, что данные заказа присутствуют)
    order_data = response.json()
    assert 'order' in order_data  # Проверяем, что есть ключ 'order' в ответе
    # Можно добавить больше проверок, например: assert order_data['order']['firstName'] == "Naruto"



    
