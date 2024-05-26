import time    # din modulul time vom folosi functia sleep pt a opri scriptul in functie de argument
from pathlib import Path    # va itera fiecare folder/subfolder si va afisa in consola toate directoarele/fisierele
from prettytable import PrettyTable
import os
from pynput import keyboard as kb
from threading import Thread
from aplicatii import meniu

root: str = "/"

tabel_list: list


def on_relase(key) -> bool:
    if key == kb.Key.esc:
        return False


def inside_dir() -> None:
    global root, tabel_list
    var_index = input("SCrie nr. de index din tabelul de mai sus: ")
    if ''.join([char for char in var_index if char == '/']):
        root = '/'
    else:
        var_index = ''.join([char for char in var_index if char.isdigit()])
        try:
            int(var_index)
            try:
                root1: str = f"{root}/{tabel_list[int(var_index) - 1]}/"
                root = root1
            except IndexError:
                os.system("clear")
                print("Alege un index doar unde vezi la TIP: DIR")
                time.sleep(3)
        except ValueError:
            os.system("clear")
            print("Nu am inteles....te rog scrie un numar")
            time.sleep(3)
    afisare()


def up_dir() -> None:
    global root
    root_list: list = root.split("/")
    try:
        root_list.pop(-1)
        root_list.pop(-1)
        root = "/".join(root_list)
        root = f"{root}"
    except IndexError:
        os.system("clear")
        root = '/'
        print("ATENTIE: Locatia ta este ", root)
        time.sleep(3)
    finally:
        afisare()


def on_press(key) -> None:
    if key == kb.Key.alt:
        fir_exec: Thread = Thread(target=inside_dir)
        fir_exec.start()
    elif key == kb.Key.up:
        fir_exec: Thread = Thread(target=up_dir)
        fir_exec.start()
    elif key == kb.Key.esc:
        meniu()


def afisare() -> None:
    """Iterarea pt fiecare folder"""
    global root, tabel_list
    os.system("clear")
    path: Path = Path(root)
    index: int = 1
    tabla: PrettyTable = PrettyTable()
    list_dir: list[str] = list()
    list_file: list[str] = list()
    for elem in path.glob("*"):
        if elem.is_dir():
            list_dir.append(elem.name)
        elif elem.is_file():
            list_file.append(elem.name)

    list_dir.sort()
    tabel_list = list_dir
    list_file.sort()
    tabla.field_names = ["INDEX", "NUME", "TIP"]
    for director in list_dir:
        tabla.add_row([f"{index}", director, "DIR"])
        index += 1
    for fisier in list_file:
        tabla.add_row([f"{index}", fisier, "FILE"])
        index += 1
    tb: PrettyTable = PrettyTable()
    tb.field_names = ["TASTA", "DESCRIERE"]
    tb.add_row(["ALT", "Va trebui sa scri numele unui director\nPentru a intra va trebui\sa apesi si tasta ENTER\n"])
    tb.add_row(["UP", "Sari 1 level\n"])
    tb.add_row(["ESC", "Iesire program"])
    tabla.align, tb.align = "c", "c"
    print(f"\n{7 * ' '}---LISTA DIR/FISIER---\n{tabla}\n\n---Esti in locatia {root}\n\n{25 * ' '}---LISTA COMENZI---\n{tb}")


afisare()

listener = kb.Listener(on_press=on_press, on_release=on_relase)
listener.start()
listener.join()
