import subprocess

CALE_TERMINAL: str = "/usr/bin/xfce4-terminal"


def index1() -> None:
    cale_script: str = "./guess_a_num.py"
    comanda: list = [CALE_TERMINAL, "--command", f"python3 {cale_script}"]
    subprocess.run(comanda)


def meniu() -> None:
    cale_script: str = "./fodor_marius.py"
    comanda: list = [CALE_TERMINAL, "--command", f"python3 {cale_script}"]
    subprocess.run(comanda)


def index2() -> None:
    cale_script: str = "./Coffee_machine.py"
    comanda: list = [CALE_TERMINAL, "--command", f"python3 {cale_script}"]
    subprocess.run(comanda)


def index3() -> None:
    cale_script: str = "./explorer.py"
    comanda: list = [CALE_TERMINAL, "--command", f"python3 {cale_script}"]
    subprocess.run(comanda)


def index4() -> None:
    cale_script: str = "./citire_fisier.py"
    comanda: list = [CALE_TERMINAL, "--command", f"python3 {cale_script}"]
    subprocess.run(comanda)
