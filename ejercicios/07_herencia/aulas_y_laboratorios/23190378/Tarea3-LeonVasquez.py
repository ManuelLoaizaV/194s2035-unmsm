class Aula:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def obtener_area(self):
        return self.largo * self.ancho

    def obtener_perimetro(self):
        return 2 * (self.largo + self.ancho)


class Laboratorio(Aula):
    def __init__(self, largo):
        self.largo= largo
        super().__init__(largo,largo)

#######################
##Probando el código:##
#######################

aula1 = Aula(7,10)
print("Área del aula: ", aula1.obtener_area())
print("Perímetro del aula: ", aula1.obtener_perimetro())

lab1 = Laboratorio(10)
print ("Area del laboratorio: ", lab1.obtener_area())
print ("Perimetro del laboratorio: ", lab1.obtener_perimetro())