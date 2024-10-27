# Registros de Estudiantes de la UNMSM

# Especificamos la Universidad
universidad = "Universidad Nacional Mayor de San Marcos"
class Estudiante:
    def __init__(self, ape_pat, ape_mat, nombre, facultad, carrera):
        self.ape_pat = ape_pat
        self.ape_mat = ape_mat
        self.nombre = nombre
        self.facultad = facultad
        self.carrera = carrera
        self.cursos = {}
        
# Agregamos calificaciones para un curso específico
    def agregar_calificacion(self,curso, calificacion):
        self.cursos[curso] = calificacion
        
# Convertimos calificacion(de numeros) a letra
    def obtener_calificacion_letra(self, calificacion):
        if 15 <= calificacion <= 20:
            return "A"
        elif 13 <= calificacion < 15:
            return "B"
        elif 12 <= calificacion < 13:
            return "C"
        elif 10.5 <= calificacion < 12:
            return "D"
        else:
            return "F"

# Mostramos las calificaciones en letras para cada curso
    def mostrar_calificaciones(self):
        print(f"{self.nombre} {self.ape_pat} {self.ape_mat} estudia en la {universidad} cursando la carrera de {self.carrera} en la facultad de {self.facultad} ha recibido su boleta de notas del pResente ciclo 2024-II: ")
        for curso, calificacion in self.cursos.items():
            calificacion_letra = self.obtener_calificacion_letra(calificacion)
            print(f"{curso}: {calificacion} ({calificacion_letra})")
            
# Creación de 4 estudiantes
estudiante1 = Estudiante("Arizaga", "Vendezu", "Juan", "Ciencias Matemáticas", "Estadística")
estudiante1.agregar_calificacion("Teoría de Muestreo", 17)
estudiante1.agregar_calificacion("Análisis Multivariado", 12)
estudiante1.agregar_calificacion("Probabilidad III", 14.8)
estudiante1.agregar_calificacion("Procesos Estocásticos", 16.8)

estudiante2 = Estudiante("Mendez", "Carlos", "María", "Ciencias Biológicas", "Microbiología y Parasitología")
estudiante2.agregar_calificacion("Virología Clínica", 18)
estudiante2.agregar_calificacion("Hematología", 13.8)
estudiante2.agregar_calificacion("Gestión de Servicios de Salud", 15)
estudiante2.agregar_calificacion("Bacteriología Clínica", 8)

estudiante3 = Estudiante("Ramirez", "Chavez", "Laura", "Medicina", "Enfermería")
estudiante3.agregar_calificacion("Farmacología y Administración en Servicios de Salud", 15.8)
estudiante3.agregar_calificacion("Enfermería en Situaciones Críticas, y Nutrición", 16)
estudiante3.agregar_calificacion("Enfermería Materno Infantil", 12)
estudiante3.agregar_calificacion("Enfermería en Salud Comunitaria", 14)

estudiante4 = Estudiante("Fernandez", "Lopez", "Esmeralda", "Ingeniería Electrónica y Eléctrica", "Ingeniería de Telecomunicaciones")
estudiante4.agregar_calificacion("Microprocesadores", 11)
estudiante4.agregar_calificacion("Redes de Computadoras", 15)
estudiante4.agregar_calificacion("Procesamiento de Señales", 13)
estudiante4.agregar_calificacion("Teoría Electromagnética II", 17)

# Mostrammos los resultados que queremos
estudiante2.mostrar_calificaciones()

# Mostramos los otros resultados aunque repetimos la anterior
estudiante3.mostrar_calificaciones()
estudiante1.mostrar_calificaciones()
estudiante4.mostrar_calificaciones()
estudiante2.mostrar_calificaciones()