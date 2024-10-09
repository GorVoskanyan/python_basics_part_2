# empty = set()
# print(type(empty))

# my_set = {1, 1, 1, 5, 1, 2}
# print(my_set)
# l = [1, 2, 1, 2, 1, 1, 3, 4, 2]
# l = list(set(l))
# print(l)
# my_tuple = tuple(my_set)
# print(my_dict)

# my_set = set()
# my_set.add('a')
# my_set.add('b')
# my_set.add('c')
#
# my_set.pop()
# set_copy = my_set.copy()
# # my_set.clear()
# other_set = [1, 2, 'c']
# my_set.update(other_set)
# # my_set.remove('w')
# # my_set.discard('w')
# print(my_set)

# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5}

# res = s1.intersection(s2)
# res = s1 & s2
# s1.intersection_update(s2)

# res = s1.difference(s2)
# res = s1 - s2
# s1.difference_update(s2)

# res = s1.symmetric_difference(s2)
# res = s1 ^ s2
# s1.symmetric_difference_update(s2)

# res = s1.union(s2)
# res = s1 | s2

# not_have_a_intersection = s1.isdisjoint(s2)
# print(not_have_a_intersection)

# is_superset = s1.issuperset(s2)
# print(is_superset)
# is_subset = s2.issubset(s1)
# print(is_subset)

# s = {i**2 for i in [1,1,1,2]}
# print(s)


# task
words = ['this', 'is', 'a', 'test', 'for', 'sets']
letters = ['t', 's']
# only = [w for w in words if set(w).issuperset(set(letters))]
# avoids = [w for w in words if not set(w).intersection(set(letters))]
only = []
avoids = []
for word in words:
    set_word = set(word)
    set_letters = set(letters)
    if set_word.issuperset(set_letters):
        only.append(word)

    if not set_word.intersection(set_letters):
        avoids.append(word)

print(only)
print(avoids)
