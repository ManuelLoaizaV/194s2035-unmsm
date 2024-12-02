class Aula:
    # Constructor
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def obtener_area(self):
        print( f"El área del aula es {self.largo * self.ancho}")

    def obtener_perimetro(self):
       print (f"El perímetro del aula es {2 * (self.largo + self.ancho)}")

class Laboratorio(Aula):

    def __init__(self, largo, ancho):
        super().__init__(largo, ancho)


    def es_cuadrado(self):
        if self.largo == self.ancho:
          print(f'El aula de {self.largo} metros de largo por {self.ancho} metros de ancho, tienen las dimensiones para ser un laboratorio')
        else:
          print(f"El aula no cumple las dimensiones para ser laboratorio")
