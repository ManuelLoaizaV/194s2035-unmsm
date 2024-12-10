from functools import reduce

numeros = [5, 4, 3, 10, -1]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)

oraciones = ["Hola, Bryan.", "Chau, Daira.", "Buenas, Eddy.", "Siu, Gabriel."]
texto = reduce(lambda s, t: s + " " + t, oraciones)
print(texto)

n = 6
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)

digitos = [2, 6, 8, 0, 2]
pares = reduce(lambda v, d: v and (d % 2 == 0), digitos, True)
print(pares)
