def obtener_mediana(numeros):
    numeros.sort()
    m = (len(numeros) - 1) // 2
    return numeros[m]


numeros = [11, 20, 14, 17, 15]
#   0   1   2   3   4
# [11, 14, 15, 17, 20]


# numeros = [5, 4, 14, 10]
#  0  1   2   3
# [4, 5, 10, 14]

print(obtener_mediana(numeros))

print(numeros)
