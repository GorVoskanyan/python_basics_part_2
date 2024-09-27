# List comprehension

# numbers = [num for num in range(10) if num % 2 == 0]

# for num in range(10):
#     numbers.append(num)


# numbers = [num if num % 2 == 0 else num ** 2 for num in range(10)]
# numbers = []
# for num in range(10):
#     if num % 2 == 0:
#         numbers.append(num)
#     else:
#         numbers.append(num ** 2)
# print(numbers)


# numbers = [num if num < 0 else 'zero' if num == 0 else 'positive' for num in range(-10, 10)]
# print(numbers)

# numbers = [[i, j, k] for i in range(10) for j in range(10) for k in range(10) if i * j == k and i != 0]
# print(numbers)


# nested lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix)

# r = [sub_elem for elem in matrix for sub_elem in elem]
# for elem in matrix:
#     for sub_elem in elem:
#         r.append(sub_elem)
#         print(sub_elem, end=' ')
#     print()
#
# print(r)