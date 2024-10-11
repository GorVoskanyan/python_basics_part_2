import os

# print(help(os))
# print(dir(os))

abs_path = os.path.abspath('.')
# print(abs_path)
file_name = 'module_os.py'
# file_path = abs_path + '\\' + file_name
# file_path = os.path.join(abs_path, file_name)
# print(file_path)


for path in os.listdir('..'):
    abs_path = os.path.join(os.path.abspath('..'), path)
    if os.path.isdir(abs_path):
        print(abs_path, 'Directory')
    elif os.path.isfile(abs_path):
        print(abs_path, 'File')