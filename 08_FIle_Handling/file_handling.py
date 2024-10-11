# write in file
# open('hello.txt', 'x')  # create file if file not exists
# file = open('hello.txt', 'w', encoding='utf-8')
# file = open('hello.txt', 'a', encoding='utf-8')
# print(type(file))
# file.write('Hello World!\n')

# numbers_list = ('1\n', '2\n', '3\n')
# file.writelines(numbers_list)

# print(file.closed)
# file.close()
# print(file.closed)

# read file
# file = open('hello.txt', 'r', encoding='utf-8')
# print(file)

# iterate over file object
# for line in file:
#     print(line.rstrip().upper())
    # print(type(line))

# all_lines = file.read()
# print(all_lines)
# file.seek(0)
# lines = file.read()
# print(lines)
# print(len(all_lines))

# first_line = file.readline(5)
# second_line = file.readline(5)

# print(first_line)
# print(second_line)

# lines_list = file.readlines()
# print(str(lines_list))
# print(repr(lines_list))

# file = open('hello.txt', 'r', encoding='utf-8')
# _sum = sum([int(line.rstrip()) for line in file if line.rstrip().isdigit()])
# _sum = 0
#
# for line in file:
#     line = line.rstrip()
#     if line.isdigit():
#         line = int(line)
#         _sum += line
# file.close()
# print(_sum)


# context manager
# _sum = 0
# with open('hello.txt', 'r', encoding='utf-8') as file:
#     _sum = sum([int(line.rstrip()) for line in file if line.rstrip().isdigit()])
#
# print(_sum)
