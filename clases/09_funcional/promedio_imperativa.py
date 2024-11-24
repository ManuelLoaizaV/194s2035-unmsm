def obtener_promedio(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    promedio = suma / len(numeros)
    return promedio


numeros = [11, 20, 14, 17]
print(obtener_promedio(numeros))
