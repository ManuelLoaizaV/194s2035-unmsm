class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor 

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self. libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro) 

    def remover_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro) 

    def buscar_libros(self, cadena_busqueda):
        resultados = []
        cadena_busqueda = cadena_busqueda.lower()
        for libro in self.libros:
            if (cadena_busqueda in libro.titulo.lower() or 
                cadena_busqueda in libro.autor.lower()):
                resultados.append(libro)
        return resultados

#Ejemplos de libros para probar el código:
libro1 = Libro("Electrónica, Teoría de Circuitos","Robert Boylestad")
libro2 = Libro("Introducción al análisis de circuitos","Robert Boylestad")
libro3 = Libro("Transistores, circuitos - diseños" ,"Joseph Waltson")
libro4 = Libro("Diseño basado en microcontroladores" ,"Francisco Marín")
#Libro duplicado:
libro5 = Libro("Diseño basado en microcontroladores" ,"Francisco Marín")     

biblioteca = Biblioteca("Biblioteca Central Pedro Zulen")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)    
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

#Escribo la palabra circuitos con mayúsculas aleatorias de forma intencional para probar la búsqueda
print("Se han encontrado los siguientes libros que contienen la palabra 'CirCuiTos': ")
resultados = biblioteca.buscar_libros("Circuitos")
for libro in resultados:
    print (f"Titulo: {libro.titulo}, Autor: {libro.autor}")

#Elimino el libro duplicado 
biblioteca.remover_libro(libro5)

#Pruebo ahora buscando el otro libro 
print("Se han encontrado los siguientes libros que contienen la palabra 'MicRoControLadOres': ")
resultados = biblioteca.buscar_libros("MicRoControLadOres")
for libro in resultados:
    print (f"Titulo: {libro.titulo}, Autor: {libro.autor}")