from Capturador import *
from Detector import *


def menu():
    print("Menu para las imagenes")
    print("  [1] Imagenes positivas")
    print("  [2] Imagenes negativas")
    print("  [3] Detectar objeto")
    print("  [4] Salir")
    print("  Opción: ", end='')


def main():
    op = ""
    while (op != "4"):
        menu()
        op = input()

        match op:
            case "1":
                Capture(POSITIVES).start()
            case "2":
                Capture(NEGATIVES).start()
            case "3":
                Detector().start()
            case "4":
                print("Adios")
            case _:
                print("Esa opcion no existe")


if (__name__ == '__main__'):
    main()
