numeros = [5, 4, 3, 10, -1]
suma = 0
for numero in numeros:
    suma += numero
print(suma)

oraciones = ["Hola, Bryan.", "Chau, Daira.", "Buenas, Eddy.", "Siu, Gabriel."]
texto = ""
for i in range(len(oraciones)):
    if i > 0:
        texto += " "
    texto += oraciones[i]
print(texto)

# n! = 1 x 2 x 3 x ... x n
n = 6
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

digitos = [2, 6, 8, 7, 2]
pares = True
for digito in digitos:
    pares = pares and (digito % 2 == 0)
print(pares)
