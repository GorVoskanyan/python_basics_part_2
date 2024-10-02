# student = ['Calipso', 25, True]
#
# print('Name:', student[0])
# print('Age:', student[1])
# print('Is student:', student[2])

# student = {
#     'name': 'Calipso',
#     'age': 25,
#     'is_student': True
# }


# dict methods: get
# print(student['grades'])
# print(student.get('grades', {}))

# updated_student = {
#     'name': 'Calipso',
#     'age': 27,
#     "grades": [5, 5, 5]
# }

# student.update(updated_student)
# updated_student = {**student, **updated_student}
# print(updated_student)

# print(type(student))
# print('Name:', student['name'])
# print('Age:', student['age'])
# print('Is student:', student['is_student'])

# student['name'] = 'Rafayel'
# student['grades'] = [5, 5, 5, 6]
# student['grades'].append(-1)
# print(student)


# empty = {}
# empty = dict()
# print(type(empty))
# empty['name'] = 'Gor'
# print(empty)


# iterate over dict
# student = {
#     'name': 'Calipso',
#     'age': 25,
#     'is_student': True
# }

#
# for key in student:
#     print(key, '->', student[key])


# for key in student.keys():
#     print(key, '->', student[key])

# student_keys = student.keys()
# print(student_keys)

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(key, value)


# deleted = student.pop('name')
# print(student)
# print(deleted)

# student.clear()
# print(student)

# student_copy = student.copy()
# print(student)
# print(student_copy)

# student.popitem()
# print(student)


# student = {
#     'name': 'Calipso',
#     'age': 25,
#     'is_student': True
# }


# student.setdefault('name')
# print(student)

# students = ['Calipso', 'Rafayel', 'Edmond', 'Jirayr']
# students_dict = dict.fromkeys(students, 1)
# print(students_dict)


# dict comprehension
# data = {i: i ** 2 for i in range(1, 10) if not i % 2}
# print(data)



# nested dicts

data = {
    'server': {
        'host': '127.0.0.1',
        'port': '8080'
    },
    'configuration': {
        'ssh': {
            'access': 'true',
            'login': 'superuser',
            'password': 'SsH19823'
        }
    }
}

# for item in data:
#     # print(item, '>>', data[item])
#     for sub_item in data[item]:
#         for s_i in data[item][sub_item]:
#             print(s_i)

# data['configuration']['ssh']['login'] = 'Sudo123'
# print(data)


student_info = {
    'name': 'Calipso',
    'age': 25,
    'addresses': {
        'addr1': {
            'city': 'Yerevan',
            'street': 'Hanrapetutyan',
            'home': '22'
        },
        'addr2': 'example'
    },
    'contacts': {
        'phone': '+37491111111',
        'email': 'calipso@gmail.com',
        'email2': None

    },
    'languages': ['python', 'english', 'Java']
}

# student_info['contacts']['email2'] = 'calipso.work@gmail.com'

# import pprint
# pprint.pprint(student_info, indent=4)