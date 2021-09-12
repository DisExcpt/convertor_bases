from funciones import menu
import os
def limpar():
    os.system("pause")
    os.system("cls")
    main()



def main():
    menu()
    opc = str(input("Deseas volver a convertir un numero [s/n]: "))
    if opc != "n":
        limpar()
    else:
        os.system("cls")
        print("\n\t\tGracias por utilizar mi convertor de bases\n")

main()