numeros = [1, 2, 3, 4]
numeros_impares = []
for numero in numeros:
    if numero % 2 == 1:
        numeros_impares.append(numero)
print(numeros_impares)

caracteres = ["x", "y", "2", "3", "a", "7", "Z"]
letras = []
for caracter in caracteres:
    if caracter.lower() in "abcdefghijklmnopqrstuvwxyz":
        letras.append(caracter)
print(letras)

palabras = ["abc", "", "", "d", ""]
palabras_no_vacias = []
for palabra in palabras:
    if len(palabra) > 0:
        palabras_no_vacias.append(palabra)
print(palabras_no_vacias)

nombres = ["Jimmy", "Hilary", "Gabriel", "Javier"]
comienzan_con_j = []
for nombre in nombres:
    if nombre[0] == "J":
        comienzan_con_j.append(nombre)
print(comienzan_con_j)

comienzan_con_z = []
for nombre in nombres:
    if nombre[0] == "Z":
        comienzan_con_z.append(nombre)
print(comienzan_con_z)


def es_digito(c):
    return len(c) == 1 and c in "0123456789"


cadenas = ["a", "1", "b", "2", "c", "45"]
digitos = []
for cadena in cadenas:
    if es_digito(cadena):
        digitos.append(cadena)
print(digitos)

otros = []
for cadena in cadenas:
    if not es_digito(cadena):
        otros.append(cadena)
print(otros)
