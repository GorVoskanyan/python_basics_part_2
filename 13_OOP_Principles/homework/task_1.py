"""Առաջադրանք 1. Հարկեր.

Ինչ անել
Իրականացնել դասերի հիերարխիա, որը նկարագրում է հարկ վճարողի գույքը:
Այն պետք է բաղկացած լինի հիմնական դասի Գույքից և
դրանից բխող դասերից Բնակարան, Ավտոմեքենա և Ամառանոց:
Բազային դասը պետք է ունենա արժեքի հատկանիշ, որը փոխանցվում է կոնստրուկտորին, և ստացված դասերից յուրաքանչյուրում
վերացված հարկի հաշվարկման մեթոդ:
Բնակարանի հարկը հաշվարկվում է արժեքի 1/1000, մեքենայի վրա՝ 1/200, ամառանոցինը՝ 1/500։ 

Յուրաքանչյուր երեխա դաս պետք է ունենա մեկ պարամետրով կառուցող(կոնստրուկտոր),
որն իր պարամետրը փոխանցում է բազային դասի կոնստրուկտորին:

Մշակել ծրագրի միջերեսը: Թող օգտագործողից հարցնի իր գումարի չափը և գույքի արժեքը,
իսկ հետո հարկ վճարի համապատասխան գույքի վրա և ցույց տա, թե որքան գումար է պակասում (եթե դա այդպես է):
"""

class Property:
    def __init__(self, value):
        self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        if value > 0:
            self._value = value  # protected
        else:
            raise ValueError('Value must be non-negative.')

    def calculate_tax(self):
        raise NotImplemented('Method must be implemented subclasses.')

class Car(Property):
    def __init__(self, value):
        super().__init__(value)

    def calculate_tax(self):
        tax = self._value / 200
        print(f'Tax for Car: {tax:.2f}')
        return tax

class CountryHouse(Property):
    def __init__(self, value):
        super().__init__(value)

    def calculate_tax(self):
        tax = self.get_value() / 500
        print(f'Tax for Country house: {tax:.2f}')
        return tax

class Apartment(Property):
    def __init__(self, value):
        super().__init__(value)

    def calculate_tax(self):
        tax = self.get_value() / 1000
        print(f'Tax for Apartment: {tax:.2f}')
        return tax

def main():
    try:
        money = float(input('Enter your money: '))
        property_type = input('Enter property type: ').lower().strip()
        if property_type == 'car':
            property_price = float(input('Enter property price: '))
            property_object = Car(property_price)
        elif property_type == 'country house':
            property_price = float(input('Enter property price: '))
            property_object = CountryHouse(property_price)
        elif property_type == 'apartment':
            property_price = float(input('Enter property price: '))
            property_object = Apartment(property_price)
        else:
            print('Invalid property type.')

        tax = property_object.calculate_tax()

        if tax <= money:
            print('You have enough money.')
        else:
            print(f"You don't have enough money. You are short {tax - money}")
    except ValueError as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
