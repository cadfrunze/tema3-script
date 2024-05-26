#   https://github.com/cadfrunze/coffe_machine
import sys
import time
from aplicatii import meniu
from stocuri_ingrediente import MENU, resources
import os

game = True
money = 0
lista = []
monede = {
    "50": 0.5,
    "10": 0.1,
    "5": 0.05,
    "1": 0.01,
}


def alegere_cafea(intrebare):
    """Alegere cafea din meniu"""
    return MENU[intrebare]


def calc_meniu(cafeaua):
    """Calculator resurse"""
    for i in cafeaua['ingredients']:
        if cafeaua['ingredients'][i] > resources[i]:
            print("Ne pare rau...nu sunt destule resurse")
            return False

    else:
        return True


def monezi_cafea(money):
    """Introducere monezi pana la valoarea adevarata"""
    if meniu_calc == True:
        while money <= cafeaua['cost']:
            os.system("clear")
            print("Intrudu o fisa")
            for moneda in monede:
                print(moneda)
            print(
                f"Cafeaua ta {intrebare} costa {round(cafeaua['cost'], 2)},\nPana acum ai introdus {round(money, 2)} mai trebuie {round(cafeaua['cost'] - money, 2)}")
            cerere = input("Introdu monezi : ")
            try:
                monede[cerere]
            except KeyError:
                print("Introdu cate o fisa afisate mai sus")
                time.sleep(3)
                continue
            money = money + monede[cerere]
            if money >= cafeaua['cost']:
                if money > cafeaua['cost']:
                    restul = money - cafeaua['cost']
                    money = money - restul
                    print(f"Poftim restul: {round(restul, 2)}")
                for i in cafeaua['ingredients']:
                    resources[i] = resources[i] - cafeaua['ingredients'][i]
                print(f"Enjoy the coffee {intrebare}")
                print(f"Ai introdus {round(money, 2)}....Cafeaua se prepara")
                return money
            else:
                continue
    else:
        return 0


if __name__ == '__main__':
    while game:
        intrebare = input("Alege un produs? (espresso/latte/cappuccino):").lower()
        try:
            MENU[intrebare]
        except KeyError:
            print("Ce ai selectat nu exista in meniu, alege corect un produs de mai sus")
            continue
        if intrebare == "off":
            print("Turn off the machine")
            game = False
        elif intrebare == "report":
            for a in resources:
                if a == 'water' or a == 'milk':
                    print(f"{a}: {resources[a]}ml")
                elif a == 'coffee':
                    print(f"{a}: {resources[a]}g")
                elif a == 'money':
                    print(f"{a}: ${resources[a]}")
        elif intrebare == "espresso" or intrebare == "latte" or intrebare == "cappuccino":
            cafeaua = alegere_cafea(intrebare)
            meniu_calc = calc_meniu(cafeaua)
            monezi = monezi_cafea(money)
            lista.append(monezi)
            if monezi > 0:
                resources['money'] = sum(lista)
        out: str = input("Doresti sa iesi?, raspunde cu \"da\" respectiv \"nu\": ").lower()
        while out != "nu" and out != "da":
            out: str = input("Nu am inteles, raspunde cu \"da\" respectiv \"nu\": ").lower()
        else:
            if out == "da":
                game = False
                meniu()
                sys.exit()

            else:
                os.system("clear")
                continue
