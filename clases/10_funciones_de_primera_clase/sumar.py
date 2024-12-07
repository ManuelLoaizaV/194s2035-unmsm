def sumar(x, y):
    return x + y


def multiplicar_por(k):
    return lambda n: n * k


def aplicar(x, f):
    return f(x)


u = 5
v = False
s = sumar
t = "abacaba"

print(u)
print(t)
x = s(u, 3)
doble = multiplicar_por(2)
print(doble(25))
print(doble(100))
triple = multiplicar_por(3)
print(triple(100))
print(doble(500) + triple(200))
print(aplicar(23, multiplicar_por(5)))
sumar_uno = lambda n: n + 1
print(aplicar(41, sumar_uno))
