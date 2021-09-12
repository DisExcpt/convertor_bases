from math import floor
from equivalencias import Obtener_valor_pL, Obtener_valor_pN


class in_out():
    def __init__(self, e, s):
        self.entrada = int(e)
        self.salida = int(s)

    def convertir_de_xa10(self, valor):
        decimal = 0
        posicion = 0
        valor = valor.lower()
        valor = valor[::-1]
        for digito in valor:
            valor2 = Obtener_valor_pL(digito)
            num_ele = int(self.entrada ** posicion)
            equiva = int(num_ele * valor2)
            decimal += equiva
            posicion += 1
        return int(decimal)

    def convertir_de_10a(self, b1):
        l = []
        num = []
        cont = 0
        while True:
            D = b1 / self.salida  # division
            R = b1 % self.salida  # residuo
            b1 = floor(D)
            l.append(R)
            num.append(Obtener_valor_pN(R))

            if floor(D) == 0:
                break
        # if b1>
        print("\nValor convertido: ", end=" ")
        for i in num[::-1]:
            print(i, end="")
        print(" base", self.salida)
