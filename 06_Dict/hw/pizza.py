# Введите количество заказов: 6
# Первый заказ: Иванов Пепперони 1
# Второй заказ: Петров Де-Люкс 2
# Третий заказ: Иванов Мясная 3
# Четвёртый заказ: Иванов Мексиканская 2
# Пятый заказ: Иванов Пепперони 2
# Шестой заказ: Петров Интересная 5

# Иванов:
# Мексиканская: 2
# Мясная: 3
# Пепперони: 3
# Петров:
# Де-Люкс: 2
# Интересная: 5

orders_quantity = int(input('Введите количество заказов: '))

data = dict()
for i in range(1, orders_quantity + 1):
    name, pizza, count = input(f"{i} заказ: ").split(' ')
    count = int(count)
    if name not in data:
        data[name] = {}

    if pizza not in data[name]:
        data[name][pizza] = count
    else:
        data[name][pizza] += count

print()
for name in data:
    print(f"{name}:")
    for pizza, count in data[name].items():
        print(f"{pizza}: {count}")

print(data)