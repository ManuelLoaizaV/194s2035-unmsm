class Curso:
    def __init__(self, nombre, codigo, horas, ciclo, numero_alumnos):
        self.nombre = nombre
        self.horas = horas
        self.codigo = codigo
        self.ciclo = ciclo
        self.numero_alumnos = numero_alumnos

    def agregar_hora(self):
        self.horas += 1

    def agregar_alumnos(self, numero_alumnos):
        self.numero_alumnos += numero_alumnos

    def presentar(self):
        print(f"{self.nombre} tiene {self.horas} horas por semana, {self.numero_alumnos} alumnos y es del ciclo {self.ciclo}")
        
aga = Curso("algebra y geometria analitica", 2018435, 6, 1, 30)
aga.presentar()

edo = Curso("Ecuaciones a¡diferenciales ordinarias", 23190124, 4, 3, 25)
edo.presentar()