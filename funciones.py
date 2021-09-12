from Convertor import in_out
import time
import os


def inicializar_In_out():
    entrada = int(input("Digita la base de entrada: "))
    salida = int(input("Digita la base de salida: "))
    obj = in_out(entrada, salida)
    return obj


def Valor():
    valor = str(input("Digita el numero a convertir: "))

    return valor


def menu():
    print("\t\tConvertor de bases\n")
    time.sleep(1)
    os.system("cls")
    valor = Valor()
    obj = inicializar_In_out()
    if obj.entrada > 2 and obj.entrada <= 30:
        if obj.entrada <= 9:
            band = False
            for i in valor:
                if int(i) > obj.entrada:
                    band = True
            if band == True:
                print("El valor que accediste es invalido para la base que ingresaste")
                os.system("pause")
                os.system("cls")
                menu()
            aux = obj.convertir_de_xa10(valor)
            obj.convertir_de_10a(aux)
        else:
            aux = obj.convertir_de_xa10(valor)
            obj.convertir_de_10a(aux)
    else:
        print(
            "El valor de la entrada es mayor al soportado por la app, vuelve a intentarlo\n")
        os.system("pause")
        os.system("cls")
        menu()
