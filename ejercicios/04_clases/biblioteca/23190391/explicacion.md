La primera complicación para realizar el código fue comprender la lógica de los solicitado, una vez comprendí
que primero debía crear el "libro" como objeto de la clase Libro para despúes añadirlo a la subclase "Biblioteca" en una nueva instancia creada, por ejemplo "literatura_española", las demás funciones cumplirían
su efecto al ejecutarse.

Entonces para crear un objeto para Libro, usé la siguiente sintaxis:
libro_borjes= Libro("aleph", "borges")
libro_quijote= Libro("quijote", "miguel cervantes")

Para crear una instancia para Biblioteca, lo definí de la siguiente manera:
literatura_española = Biblioteca("Literatura española")

Ahora podía agregar el libro "quijote" y "aleph" a "literatura española", de la siguiente forma:
literatura_española.agregar_libro(libro_borjes)
literatura_española.agregar_libro(libro_quijote)
Apareciendo el siguiente mensaje:
El libro 'quijote' del autor 'miguel cervantes' ha sido añadido a la biblioteca 'Literatura española'
El libro 'aleph' del autor 'borges' ha sido añadido a la biblioteca 'Literatura española'

Si el libro era prestado (removido), usaba el siguiente script:
literatura_española.remover_libro(libro_quijote)
El output era:
Se ha prestado el libro 'quijote' del autor 'miguel cervantes' ahora mismo
Para comprobar la validez del código, intentaba volver a prestar el mismo libro, y ya no era posible:
Error: El libro 'quijote' del autor 'miguel cervantes' no se encuentra en la estantería 'Literatura española'

Por último para hacer una búsqueda, de libros del autor Borges por ejemplo:
literatura_española.buscar_libros("borges")
Al ejecutar imprimía:
Título: aleph, Autor: borges
[<__main__.Libro at 0x7c40e008b190>]

Entonces el código que escribí cumple lo solicitado, pudiendo ser usado para crear distintas instancias de Biblioteca (novelas, scifi, cuentos, etc) y agregando todos los libros que agreguemos a la clase Libros.
A la vez también también se podría optimizar según el feedback que brinden los usuarios.