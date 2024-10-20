#Registros de estudio de la UNMSM
#Tare2
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__cursos = {}
    
    def calcular_nota_letra( self, calificacion ):
        if calificacion >= 15:
            return 'A'
        elif 13 <= calificacion < 15:
            return 'B'
        elif 12 <= calificacion < 13:
            return 'C'
        elif 10.5 <= calificacion < 12:
            return 'D'
        else:
            return 'F'
        
    def  agregar_curso ( self, nombre_curso, calificacion ):
        nota_letra = self.calcular_nota_letra( calificacion  )
        self.__cursos[nombre_curso] = nota_letra 

    def obtener_cursos (self):
        return self.__cursos
#Registros de estudio de la UNMSM
Estudiante =  Estudiante( "Daira Tinidad" )

Estudiante.agregar_curso( "Lenguaje de programación-teoría" , 16 )
Estudiante.agregar_curso( "Variable compleja" , 14)
Estudiante.agregar_curso( "Circuitos Electronicos I" , 13 )

cursos =  Estudiante.obtener_cursos()
print(cursos)
