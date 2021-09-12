
# obtener valor por letra
def Obtener_valor_pL(caracter):
    # para que funcione ocupamos que sea un str
    equivalencias = {
        "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15,
        "g": 16, "h": 17, "i": 18, "j": 19, "k": 20, "l": 21,
        "m": 22, "n": 23, "o": 24, "p": 25, "q": 26, "r": 27,
        "s": 28, "t": 29, "u": 30
    }
    if caracter in equivalencias:
        return equivalencias[caracter]
    else:
        return int(caracter)

# obtener valor por numero
def Obtener_valor_pN(num):

    # para que arroje un valor ocupamos que sea un entero el que sea digitado
    equivalencias = {
        10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f",
        16: "g", 17: "h", 18: "i", 19: "j", 20: "k", 21: "l",
        22: "m", 23: "n", 24: "o", 25: "p", 26: "q", 27: "r",
        28: "s", 29: "t", 30: "u"
    }
    if num in equivalencias:
        return equivalencias[num]
    else:
        return Obtener_valor_pL(num)