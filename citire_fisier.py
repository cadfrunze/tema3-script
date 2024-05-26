import os
from pathlib import Path  # va itera fiecare folder/subfolder si va afisa in consola toate directoarele/fisierele
import pandas as pd  # pandas alias pd pt citire/editare fisier.csv
from prettytable import PrettyTable
from aplicatii import meniu
import time
import sys

PATH_ROOT: str = "./citire-fisier-csv"
path: Path = Path(PATH_ROOT)
EXTENSII = [".csv"]
tabel: PrettyTable = PrettyTable()

# var FISIERE = iterarea si returnarea FISIERE de tip list a folderului ./citire-fisier-csv cu extnsia din EXTENSII
# intentionat am lasat test.txt pentru a verifica daca FISIERE o va citi
FISIERE: list = [element.name for element in path.glob("*") if element.is_file() and element.suffix in EXTENSII]


def citire_elemente(elemente: list) -> str:
    if len(FISIERE) < 1:
        print(f"Creeaza un fisier cu una din extensii: {''.join(EXTENSII)}")
    elif len(FISIERE) > 1:
        print("Selecteaza un fisier")
        for elem in elemente:
            print(elem)
        var_input: str = input("Scrie aici fisierul: ")
        if var_input not in elemente:
            os.system("clear")
            print("Numele fisierului pe care l-ai scris nu exista: ")
            return citire_elemente(FISIERE)
        else:
            elemente[0] = var_input
    root_fisier: str = f"{PATH_ROOT}/{elemente[0]}"
    return root_fisier


def citire_fisier(fisier: str) -> object:
    data: pd.read_csv = pd.read_csv(fisier)
    tabel.field_names = [x.upper() for x in data.to_dict()]
    data_dict: dict = data.to_dict("list")
    for n in range(len(data_dict.values())):
        row = [data_dict[key][n] for key in data_dict]
        tabel.add_row(row)
    print(f"Am citit fisierul: {fisier}")
    return tabel


# variabila specialasa de declansare a scriptului, de la scriptul fodor_marius.py cand se intra in acest modul
# de aici se va declansa scriptul
if __name__ == '__main__':
    while True:
        os.system("clear")
        element: str = citire_elemente(FISIERE)
        print(citire_fisier(element))
        var_ext: str = input("Doresti sa iesi? (Raspunde cu \"da\" sau \"nu\": ").lower()
        while var_ext != "da" and var_ext != "nu":
            var_ext: str = input("Nu am inteles, (raspunde cu \"da\" sau \"nu\"): ").lower()
        if var_ext == "da":
            meniu()
            sys.exit()
        else:
            os.system("clear")
            print(f"Ai posibilatea sa adaugi fisiere .csv in {PATH_ROOT}")
            time.sleep(4)
            continue
