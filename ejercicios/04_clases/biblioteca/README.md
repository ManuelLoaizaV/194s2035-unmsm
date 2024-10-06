# Biblioteca Central Pedro Zulen

Te han encargado escribir algo de código para la biblioteca central Pedro Zulen.
Completa las clases `Biblioteca` y `Libro` que se describen a continuación.

## Clase `Libro`

`__init__(self, titulo, autor)`

Asigna los valores de los parámetros a `.titulo` y `.autor`.

## Clase `Biblioteca`

`__init__(self, nombre)`

Inicializa `.nombre` con el valor del parámetro `nombre`.
Crea una variable `.libros` que se inicializa como una lista vacía.

`agregar_libro(self, libro)`

Agrega un libro, que es una instancia de `Libro`, al final de la lista `.libros`.

`remover_libro(self, libro)`

Si el título y el autor del libro coinciden con los de un libro en la biblioteca,
eliminar dicho libro de la lista.

`buscar_libros(self, cadena_busqueda)`

Para cada libro en la biblioteca,
verifica si `cadena_busqueda` está contenido en el campo título o en el campo autor
(sin distinguir entre mayúsculas y minúsculas).
Devuelve una lista de todos los libros que coincidan con la cadena de búsqueda,
ordenados en el mismo orden en que fueron añadidos a la biblioteca.
