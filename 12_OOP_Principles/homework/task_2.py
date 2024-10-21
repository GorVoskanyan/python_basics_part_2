"""
Առաջադրանք 2. Հայրերը, մայրերն ու երեխաները

Ինչ պետք է անել
Իրականացրեք երկու դաս՝ «Ծնող» և «Երեխա»: Ծնողը ունի՝
- անուն,
- տարիքը,
- երեխաների ցանկ։

Ծնողը կարող է՝
- տրամադրել ինֆորմացիա իր մասին,
- հանգստացնել երեխային,
- կերակրել երեխային։

Երեխան ունի՝
- անուն,
- տարիքը (պետք է լինի առնվազն 16 տարով փոքր ծնողից),
- հանգստության վիճակ,
- սովածության վիճակ։

Վիճակների իրականացումը կարող եք ընտրել ինքնուրույն: Այն կարող է լինել պարզ "դրոշ", կամ վիճակների բառարան, կամ ինչ-որ այլ բան։

Ինչ է գնահատվում
1. Արդյունքը ճիշտ է։
2. Մոդելները իրականացված են օբյեկտային ծրագրավորման ոճում։
3. Փոփոխականները, ֆունկցիաները և դասերի մեթոդները ունեն իմաստալից անուններ։
"""


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def provide_info(self):
        print(f'Name: {self.name}\nAge: {self.age}\nChildren: {self.children}')

    def calm_children(self, children):
        children.calm_state = True

    def feed_children(self, children):
        children.hungry_state = True

    def add_children(self, children):
        if self.age - children.age > 16:
            self.children.append(children)
        else:
            print('Parent age must be greater then children age 16 years.')

class Children:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm_state = False
        self.hungry_state = False

    def __str__(self):
        return f"{self.name} - {self.age} |  is hungry: {self.hungry_state} | is calm: {self.calm_state}"


if __name__ == '__main__':
    children1 = Children('A', 12)
    children2 = Children('B', 16)
    children3 = Children('C', 11)
    parent1 = Parent('Parent 1', 30)

    parent1.add_children(children1)
    # parent1.provide_info()
    #
    parent1.add_children(children2)
    # parent1.provide_info()

    # if not children1.calm_state:
    #     # print(children1.calm_state)
    #     print(children1)
    #     parent1.calm_children(children1)
    #     print(children1)
    #
    # if not children1.hungry_state:
    #     print(children1)
    #     parent1.feed_children(children1)
    #     print(children1)

    parent1.add_children(children3)
    children1.hungry_state = False

    for children in parent1.children:
        if not children.calm_state:
            # print(children1.calm_state)
            print(children)
            parent1.calm_children(children1)
            print(children)
        print()
        if not children.hungry_state:
            print(children)
            parent1.feed_children(children1)
            print(children)