# String methods

# s = 'hello world'
# l = s.split()
# n_s = '_^_'.join(l)
# print(n_s)

# print(s.index('q', 6))
# print(s.find('l', 6))
# print('ok')

# print(s.strip())
# print(s.rstrip())
# print(s.lstrip())

# print(s.count('l'))
# print(s.endswith('w'))
# print(s.startswith('hello'))


# s = 'UPPERCASE'
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.isupper())


# s = 'hello world, hi world'
# n_s = s.replace('world', 'friends', 1)
# print(n_s)


# users = ['Gor Voskanian', 'Alex Smith']
# name_surname = input('>>> ').title()
# name_surname = name_surname.upper()
# name_surname = name_surname.lower()
# name_surname = name_surname.capitalize()
# name_surname = name_surname.title()
# if name_surname in users:
#     print('Welcome')


# string formatting
# product = 'Macbook PRO'
# quantity = 10
# price = 1999.99


# result = str(quantity) + ' ' + product + ' total price: ' + str(quantity * price) + '$'
# print(result)
# result = "%04i %s total price: %7.2f$" % (quantity, product, quantity * price)
# print(result)
# result = "{} {} total price: {}$".format(quantity, product, quantity * price)
# print(result)
# result = "{2} {1} total price: {0}$".format(quantity, product, quantity * price)
# print(result)
# result = "{q} {p} total price: {t}$".format(q=quantity, p=product, t=quantity * price)
# print(result)
# # f-string Use python 3.6 +
# result = f"{quantity:04d} {product:^30} total price: {(quantity * price):7.2f}$"
# print(result)


# print('hello_world'.center(20, '_'))

