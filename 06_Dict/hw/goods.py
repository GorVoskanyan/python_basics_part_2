# Лампа — 27 штук, стоимость 1134 рубля.
# Стол — 54 штуки, стоимость 27 860 рублей.
# Диван — 3 штуки, стоимость 3550 рублей.
# Стул — 105 штук, стоимость 10 311 рублей.

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product_name, product_code in goods.items():
    total_price = 0
    total_quantity = 0
    for item in store[product_code]:
        total_quantity += item['quantity']
        total_price += item['price'] * item['quantity']
    # print(f"{product_name} — {total_quantity} штук, стоимость {total_price} рубля.")
    print(product_name, '-', total_quantity, 'հատ, ընդհանուր գինը՝', total_price, 'դրամ')