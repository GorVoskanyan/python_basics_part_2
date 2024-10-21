class Car:

    def __init__(self, mark , year_of_creation, is_electronic):
        self.mark =mark
        self.yoc= year_of_creation
        self.is_electronic = is_electronic

    car1=Car('BMW',2015,False)
    car2=Car(mark='Mercedes', year_of_creation=2000, id_electronic=True)
    print(car1.mark)






