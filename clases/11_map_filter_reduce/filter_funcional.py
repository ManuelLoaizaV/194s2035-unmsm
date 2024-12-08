numeros = [1, 2, 3, 4]
numeros_impares = list(filter(lambda n: n % 2 == 1, numeros))
print(numeros_impares)

caracteres = ["x", "y", "2", "3", "a", "7", "Z"]
letras = list(filter(lambda c: c.lower() in "abcdefghijklmnopqrstuvwxyz", caracteres))
print(letras)

palabras = ["abc", "", "", "d", ""]
palabras_no_vacias = list(filter(lambda s: len(s) > 0, palabras))
print(palabras_no_vacias)

nombres = ["Jimmy", "Hilary", "Gabriel", "Javier"]
comienzan_con_j = list(filter(lambda s: s[0] == "J", nombres))
print(comienzan_con_j)

comienzan_con_z = list(filter(lambda s: s[0] == "Z", nombres))
print(comienzan_con_z)


def es_digito(c):
    return len(c) == 1 and c in "0123456789"


cadenas = ["a", "1", "b", "2", "c", "45"]
digitos = list(filter(es_digito, cadenas))
print(digitos)

otros = list(filter(lambda s: not es_digito(s), cadenas))
print(otros)
