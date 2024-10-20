class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__cursos = {}

    def calcular_nota_letra(self, calificacion):
        if calificacion >= 15:
            return "A"
        elif 13 <= calificacion < 15:
            return "B"
        elif 12 <= calificacion < 13:
            return "C"
        elif 10.5 <= calificacion < 12:
            return "D"
        else:
            return "F"

    def agregar_curso(self, nombre_curso, calificacion):
        nota_letra = self.calcular_nota_letra(calificacion)
        self.__cursos[nombre_curso] = nota_letra

    def obtener_cursos(self):
        return self.__cursos

def ingresar_datos_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    estudiante = Estudiante(nombre)

    while True:
        nombre_curso = input("Ingrese el nombre del curso: ")
        calificacion = float(input("Ingrese la calificación sobre 20: "))
        
        estudiante.agregar_curso(nombre_curso, calificacion)

        agregar_otro = input("¿Desea agregar otro curso? (s/n): ")
        if agregar_otro.lower() != 's':
            break

    return estudiante

estudiante = ingresar_datos_estudiante()
print(f"\nCursos de {estudiante.nombre}: {estudiante.obtener_cursos()}")