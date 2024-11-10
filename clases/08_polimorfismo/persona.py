class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def obtener_edad(self):
        return self.__edad

    def __add__(self, otra):
        return Persona("experimento", self.obtener_edad() + otra.obtener_edad())

    def __str__(self):
        return f"{self.__nombre} tiene {self.__edad}"

# __str__ es llamado por la función print.
# Leer https://docs.python.org/3/reference/datamodel.html#object.__str__
x = 42 + 31
print(x)

y = "42" + "31"
print(y)

evelin = Persona("Evelin", 18)
print(evelin)

bryan = Persona("Bryan", 22)
print(bryan)

z = evelin + bryan
print(z)
