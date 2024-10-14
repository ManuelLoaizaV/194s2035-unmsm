
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Se agregó el libro: {libro.titulo}")

    def remover_libro(self, libro):
        for libro_ in self.libros:
            if libro_.titulo == libro.titulo and libro_.autor == libro.autor:
                self.libros.remove(libro_)
                print(f"Se removió el libro: {libro.titulo}")

    def buscar_libros(self, cadena_busqueda):
      cadena_busqueda = cadena_busqueda.lower()
      lista_de_libros_hallados = []
      for libro in self.libros:
            if (cadena_busqueda in libro.titulo.lower() or
            cadena_busqueda in libro.autor.lower()):
                lista_de_libros_hallados.append(libro)
      if lista_de_libros_hallados:
             for libro in lista_de_libros_hallados:
                print(f"* {libro.titulo} de {libro.autor}")
      else:
            print("No se encontraron libros que coincidan")

b = Biblioteca("Biblioteca Central Pedro Zulen")
l1 = Libro("Cumbres Borrascosas", "Emily Bronte ")
l2 = Libro("Shadow Slave", "Guiltythree")
l3 = Libro("Reverend_insanity", "Gu Zhen Ren")
l4 = Libro("Le Rouge et le Noir","Stendhal")
l5 = Libro("Mysteries of Immortal Puppet Master","Gu Zhen Ren")
b.agregar_libro(l1)
b.agregar_libro(l2)
b.agregar_libro(l3)
b.agregar_libro(l4)
b.agregar_libro(l5)
b.remover_libro(l1)
b.buscar_libros("Emily")
b.buscar_libros("Gu Zhen")

