# def sumar(numeros):
#     if len(numeros) == 0:
#         return 0
#     return numeros[0] + sumar(numeros[1:])


# def obtener_promedio(numeros):
#     return sumar(numeros) / len(numeros)

def obtener_promedio(numeros):
    return sum(numeros) / len(numeros)


numeros = [11, 20, 14, 17]
print(obtener_promedio(numeros))
