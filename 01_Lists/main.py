# students = ['Calipso', 'Edmond', 'Jiro', 'Rafo']
# print(students)
# print(type(students))

# mutable vs immutable
# text = 'internationalization'
# print(text[0])      # indexing
# print(text[-1])
# text[0] = 'a'       # TypeError


# students[0] = 'Gor'
# print(students)


# empty = list()
# empty = []
# print(type(empty))

# for num in range(1, 10):
#     empty += [num]

# print(empty)

# range_10 = list(range(10))
# print(range_10)
# print(type(range_10))

# text = 'hello world'
# my_list = list(text)
# print(my_list)


# even_numbers = list(range(0, 10, 2))
# print(even_numbers)

# even_numbers = []
# odd_numbers = []
#
# for num in range(10):
#     if num % 2 == 0:
#         even_numbers += [num]
#     else:
#         odd_numbers += [num]

# print(even_numbers)
# print(odd_numbers)


# list methods

# l = []

# adding
# l.append('a')
# l.append('b')
# l[len(l) - 1] = 'e'
# l.insert(0, 'c')
# l[0:0] = 'd'
# l.extend('hello')
# l.append('hello')
# l.extend([1, 2, 3])
# print(l)

# for elem in l:
#     print(elem, '->', type(elem))

# remove
# l.remove('a')
# last_elem = l.pop()
# first_elem = l.pop(0)
# med = l.pop(len(l) // 2)
# print(l)
# del l[0]
# print(l)
# print(last_elem)
# print(first_elem)
# print(med)
# l.clear()
# print(l)


# count, index
# l = ['a', 'b', 'c', 'a', 'a']
# a_index = l.index('a', 2, 1000)
# print(a_index)
# a_count = l.count('a')
# print(a_count)



def my_function(l: list) -> list:
    maximum = l[0]
    minimum = l[0]
    length = 0

    for elem in l:
        if elem > maximum:
            maximum = elem
        elif elem < minimum:
            minimum = elem

        length += 1

    return [maximum, minimum, length]


# l = [-2, 3, 4, -10, 23, 45, 1]
# result = my_function(l)
# maximum, minimum, length = my_function(l)   # unpacking

# print("Maximum:", maximum)
# print("Minimum:", minimum)
# print("Length:", length)


# print("Maximum:", max(l))
# print("Minimum:", min(l))
# print("Length:", len(l))



# class ImListy:
#     def __init__(self):
#         self.data = []
#
#     def avelacnel(self, elem):
#         self.data.append(elem)
#
#     def __str__(self):
#         return '++' + ', '.join(self.data) + '++'


# create instance
# im_listi_orinaky = ImListy()
# im_listi_orinaky.avelacnel('a')
# im_listi_orinaky.avelacnel('b')
# im_listi_orinaky.avelacnel('c')
# print(im_listi_orinaky)


# reverse, sort
# l = ['B', 'A', 'a']
# l.sort(key=None, reverse=None)
# sorted_l = sorted(l, key=None, reverse=None)
# print(sorted_l)

# l.reverse()
# reversed_l = list(reversed(l))
# print(l)
# print(reversed_l)
# for elem in reversed_l:
#     print(elem)


# copy
# l = [1, 2, 3]
# l_copy = l.copy()
# l_copy = l[:]
# l_copy[0] = 'a'

# print(l_copy)
# print(l)


# deepcopy, nested lists
# import copy
# l = [1, 2, 3, ['a', 'b', 'cd']]
# print(len(l))
# print(l[-1][-1][-1])

# l_copy = l.copy()
# l_copy = copy.deepcopy(l)
# l_copy[-1][-1] = 'x'

# print(l_copy)
# print(l)


