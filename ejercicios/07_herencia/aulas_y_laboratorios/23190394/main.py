import math

class Aula:
    def __init__(self, largo, ancho):
        #dimensiones
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

    def obtener_perimetro(self):
        return 2 * (self.largo + self.ancho)


class Laboratorio(Aula):
    def __init__(self, lado):
        super().__init__(lado, lado)

#Ejemplo para crear un aula de 8*4
Aula = Aula(8, 4)
print("Área del aula:", Aula.calcular_area()) 
print("perimetro del aula:", Aula.obtener_perimetro())

# Ejemplo para crear un laboratorio de 8*8
Laboratorio = Laboratorio(8)
print("Área del laboratorio:",Laboratorio.calcular_area())
print("perimetro del laboratorio:", Laboratorio.obtener_perimetro())