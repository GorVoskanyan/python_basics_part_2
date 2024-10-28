"""Առաջադրանք 2. Կարմա
Ինչ անել
Բուդդայական ծրագրավորողներից մեկը որոշել է ստեղծել իր սեփական կյանքի սիմուլյատորը, որում լուսավորության
 հասնելու համար անհրաժեշտ է հավաքել 500 կարմա միավոր (սա հաստատուն է):

Ամեն օր կանչվում է հատուկ գործառույթ one_day(), որը վերադարձնում է կարմայի քանակը 1-ից մինչև 7 և կարող
 է բացառություններից մեկը նետել 10-ից 1-ի հավանականությամբ.

KillError
DrunkError
CarCrashError
GluttonyError
DepressionError
(Դուք ինքներդ պետք է բացառություններ ստեղծեք՝ օգտագործելով ժառանգությունը Exception-ից):

Գրեք այսպիսի ծրագիր
Գործառույթը փաթաթեք անսահման օղակով, որից դուրս գալը հնարավոր է միայն այն դեպքում, երբ կարման կուտակվում
 է մշտական ​​մակարդակի վրա: Գործընթացի բացառությունները մշակեք և դրանք գրեք առանձին karma.log-ում:

Ինչ է գնահատվում
Հաշվարկի արդյունքը ճիշտ է։
Մոդելներն իրականացվում են OOP ոճով, հիմնական ֆունկցիոնալությունը նկարագրված է դասի մեթոդներով և անհատական
​​գործառույթներով։
Դասեր գրելիս պահպանվում են OOP-ի հիմնական սկզբունքները՝ ինկապսուլյացիա, ժառանգականություն և պոլիմորֆիզմ:
Սեթերներն ու ստացողները օգտագործվում են մասնավոր ատրիբուտների արժեքներ ստանալու և սահմանելու համար:
Ժառանգությունն օգտագործվում է գոյություն ունեցող դասի հիման վրա նոր դաս ստեղծելու համար:
Արդյունքների ստացման գործընթացի մասին հաղորդագրությունները իմաստալից և հասկանալի են օգտագործողի համար:
Փոփոխականները, ֆունկցիաները և դասերի սեփական մեթոդներն ունեն իմաստալից անուններ, այլ ոչ թե a, b, c, d:
Օգտագործված ֆայլերի անվանումները համապատասխանում են առաջադրանքում նշվածներին:
"""
import random


class KarmaError(Exception):
    pass
class KillError(KarmaError):
    pass
class DrunkError(KarmaError):
    pass
class CarCrashError(KarmaError):
    pass
class GluttonyError(KarmaError):
    pass
class DepressionError(KarmaError):
    pass

class LifeSimulator:
    def __init__(self, karma_points):
        self.karma_points = 0

    def one_day(self):
        self.karma_points += random.randint(1, 7)
        if random.randint(1, 10) <= 1:
            error_type = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
            raise error_type

    def simulate(self):

        while self.karma_points < 500:
            try:
                self.one_day()
            except KarmaError as e:
                print(f"{e} - Կարմայի կուտակում: {self.karma_points}")

        print(f"Life simulation is ended՝ {self.karma_points}")


if __name__ == "__main__":
    simulator = LifeSimulator(random)
    simulator.simulate()

