"""
Առաջադրանք 1. Ուսանողները

Ինչ պետք է անել
Իրականացրեք մոդել Student անունով, որը կունենա հետևյալ դաշտերը՝
«Անուն Ազգանուն», «Խմբի համար», «Ուսուցման ցուցանիշ» (ցանկ, որը բաղկացած է հինգ տարրերից):
Այնուհետև ստեղծեք տաս ուսանողների ցուցակ (մուտքագրեք ուսանողների տվյալները կամ հարցրեք օգտատիրոջը)
և դասավորեք ցուցակը ըստ միջին գնահատականի աճման կարգով: Արդյունքը պետք է արտածել էկրանին:

Ինչ է գնահատվում
1. Արդյունքը ճիշտ է։
2. Input-ը պարունակում է ճիշտ հրամաններ մուտքագրման համար:
3. Մոդելները իրականացված են օբյեկտային ծրագրավորման ոճում, հիմնական ֆունկցիոնալությունը նկարագրված է դասերի մեթոդներում և առանձին ֆունկցիաներում։
4. Գործընթացի վերաբերյալ հաղորդագրությունները իմաստալից և հասկանալի են օգտատիրոջ համար:
5. Փոփոխականները, ֆունկցիաները և դասերի մեթոդները ունեն իմաստալից անուններ, ոչ թե a, b, c, d։
"""

class Student:
    def __init__(self, fullname, group_number, learning_rates):
        self.name, self.surname = fullname.split()
        self.group_number = group_number
        self.learning_rates = learning_rates

    def __str__(self):
        return f"{self.name} {self.surname}: {self.group_number} | {self.learning_rates}"


    def get_major_rate(self):
        return sum(self.learning_rates) / len(self.learning_rates)


if __name__ == '__main__':
    import random

    students_names = ['Calipse Antonyan', 'Jirayr Antonyan', 'Rafayel Khachikyan', 'Edmond Atoyan', 'Gor Voskanyan']
    students_list: list[Student] = []

    for i in range(5):
        student_group_number = random.randint(1, 5)
        student_grades = random.choices(range(1, 10), k=5)
        student_object = Student(fullname=students_names[i], group_number=student_group_number, learning_rates=student_grades)
        students_list.append(student_object)

    print(students_list)
    for student in students_list:
        print(student)

    print()
    students_list.sort(key=lambda student: student.get_major_rate())
    for student in students_list:
        print(student)
