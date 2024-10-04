negativ = []
zero = []
positiv = []
line = input("Mutqagreq amboxj tver : ")
while line != '':
     number = int(line)
     if number < 0:
        negativ.append(number)
     elif number > 0:
        positiv.append(number)
     else:
         zero.append(number)
    line = input("Mutqagreq amboxj tver : ")

for number in negativ:
    print(number)
for number in zero:
     print(number)
for number in positiv:
     print(number)