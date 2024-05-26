# https://github.com/cadfrunze/guess_a_number
from art import logo
import random
import time
import os
import sys
from aplicatii import meniu
print(logo)


def numarul_ales():
    return random.randint(1, 100)


NUMARUL_ALES = numarul_ales()

numere_alese = []
intrebare0 = True
intrebare1 = True


def jocul():
    if intrebare1:
        print("Bine ai venit la jocul \"Ghiceste numarul\"")
        time.sleep(2)
        regulament = "Regulamentul:\n1. Veti fi intrebat de nivelul de dificulate, si va trebui sa alegeti: \"easy\"(10 incercari) sau \"hard\"(5 incercari)\n2. Veti alege un numar de la 1 la 100.\n3. Daca raspunsul nu se afla intre 1 si 100 sau va avea un alt caracter in afara de o cifra, veti fi intrebat din nou fara a se va scadea din incercari.\n4. Cu cat sunteti mai aproape de numarul ales de calculator vi se afisa cate o solutie, respectiv: \"Cald!\" sau \"Foarte cald!\"\n5. Cu cat sunteti mai departe vi se va afisa cate o solutie, respectiv: \"Foarte mic!\" sau \"Foarte mare!\""
        scriere = ""
        for litare in regulament:
            scriere = scriere + litare
            os.system('clear')
            print(scriere)
            if litare == "\n":
                time.sleep(2)
        time.sleep(3)
    alegere_nivel = input("Alege nivelul de dificultate. Scrie \"easy\" sau \"hard\": ").lower()
    sanse = 0

    while alegere_nivel != "easy" and alegere_nivel != "hard":
        alegere_nivel = input("Nu am inteles. Alege nivelul de dificultate. Scrie \"easy\" sau \"hard\": ").lower()
    if alegere_nivel == "easy":
        sanse = sanse + 10
    elif alegere_nivel == "hard":
        sanse = sanse + 5
    print(logo)
    time.sleep(2)
    print("-" * 19)
    print(f"Numar incercari: {sanse}")
    game0 = True
    while sanse >= 1:
        if sanse == 1:
            print("ATENTIE!. Ultima sansa!")
            print("-" * 19)
            print(f"Numar incercari ramase: {sanse}")
        alegere_numar = input("Alege un numar: ")
        while game0:
            user_proba = []
            for i in alegere_numar:
                user_proba.append(i)
                if i == " ":
                    user_proba.remove(i)
            alegere_numar = "".join(user_proba)
            if len(alegere_numar) > 3:
                alegere_numar = input("Hey! Vezi ca ai introdus prea multe caractere!. Alege un numar de la 1 la 100: ")
                continue
            elif alegere_numar.isnumeric():
                alegere_numar = int(alegere_numar)
                if alegere_numar > 100:
                    alegere_numar = input(
                        "Hey! Vezi ca ai scris un numar mai mare ca si 100. Alege un numar de la 1 la 100: ")
                    continue
                elif alegere_numar < 1:
                    alegere_numar = input(
                        "Hey! Vezi ca ai mai scris un numar mai mic ca si 1. Alege un numar de la 1 la 100: ")
                    continue
                elif alegere_numar in numere_alese:
                    alegere_numar = input(
                        f"Hey! Vezi ca ai mai scris acest numar: \"{alegere_numar}\". Pana acum numerele tale alese sunt {str(numere_alese)}. Alege un numar de la 1 la 100: ")
                    continue
                else:
                    game0 = False
                    game1 = True
            elif alegere_numar != alegere_numar.isnumeric:
                alegere_numar = input(f"Hey! Vezi ca nu ai scris o cifra. Alege un numar de la 1 la 100: ")
                game1 = False
                continue

        if game1 == True:
            numere_alese.append(alegere_numar)
            print(f"Ai ales: {numere_alese[-1]}")
            if alegere_numar == NUMARUL_ALES:
                return True
            elif alegere_numar < NUMARUL_ALES:
                if (NUMARUL_ALES - int(numere_alese[-1])) <= 10:
                    if (NUMARUL_ALES - int(numere_alese[-1])) <= 5:
                        print("Foarte cald!")
                    else:
                        print("Cald!")
                else:
                    print("Prea mic!")
            elif alegere_numar > NUMARUL_ALES:
                if (int(numere_alese[-1] - NUMARUL_ALES)) <= 10:
                    if (int(numere_alese[-1] - NUMARUL_ALES)) <= 5:
                        print("Foarte cald!")
                    else:
                        print("Cald!")
                else:
                    print("Prea mare!")
            sanse = sanse - 1
            if sanse > 1:
                print("-" * 19)
                print(f"Numar incercari ramase: {sanse}")
            game1 = False
            game0 = True
        if sanse < 1:
            return False


final = jocul()


def castigatorii():
    if final == True:
        time.sleep(1)
        print("Bravo! Bravo! Bravo!")
        time.sleep(1)
        print(f"Numarul ales de tine: {numere_alese[-1]} s-a potrivit cu numarul ales de calculator ({NUMARUL_ALES})")
        time.sleep(1)
        print(f"Numerele pe care le-ai ales sunt: {numere_alese}")
        time.sleep(1)
        print(f"Ai reusit sa castigi din {len(numere_alese)} incercari")
        time.sleep(1)
    else:
        print(f"Imi pare rau...ultimul numarul ales de tine: {numere_alese[-1]},")
        time.sleep(2)
        print(f"Iar pana acum numerele alese de tine sunt {numere_alese},")
        time.sleep(2)
        print(f"Din pacate nu ai ghicit numarul ales de calculator care este {NUMARUL_ALES}.")


castigatorul = castigatorii()
while intrebare0:
    print("Doresti sa joci din nou?")
    time.sleep(1)
    print("Daca raspunzi \"da\" jocul va porni din nou")
    time.sleep(1)
    print("Daca raspunzi \"nu\" vei iesi din joc")
    raspunde0 = input("Raspunde aici >>> ").lower()
    if raspunde0 == "da" or raspunde0 == "yes":
        os.system('clear')
        print("Doresti sa recitesti regulamentu?. Raspunde cu \"da\" sau \"nu\"")
        raspunde1 = input("Raspunde aici >>> ").lower()
        if raspunde1 == "da" or raspunde1 == "yes":
            intrebare1 = True
            numere_alese = []
            NUMARUL_ALES = numarul_ales()
            final = jocul()
            castigatorul = castigatorii()

        elif raspunde1 == "nu" or raspunde1 == "no":
            intrebare1 = False
            numere_alese = []
            NUMARUL_ALES = numarul_ales()
            final = jocul()
            castigatorul = castigatorii()
        else:
            os.system('clear')
            print("Nu am inteles!")
            continue

    elif raspunde0 == "nu" or raspunde0 == "no":
        os.system('clear')
        print("Bine")
        time.sleep(2)
        print("La revedere!")
        time.sleep(2)
        intrebare0 = False
        meniu()
        sys.exit()
    else:
        os.system('clear')
        print("Nu am inteles!")
        continue
