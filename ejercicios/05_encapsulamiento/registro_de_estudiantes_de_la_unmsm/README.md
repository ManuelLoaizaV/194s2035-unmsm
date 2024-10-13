# Registros de Estudiantes de la UNMSM

En la **Universidad Nacional Mayor de San Marcos**,
los estudiantes son evaluados en sus distintos cursos.
Dependiendo de sus calificaciones (sobre 20), reciben diferentes calificaciones en formato de letra.

Completa la clase `Estudiante`.

## Constructor

El constructor debe asignar el parámetro `nombre` a la variable de instancia `nombre`.

También debe inicializar un variable de instancia privada llamada `__cursos`, que será un diccionario vacío.

## Método `calcular_nota_letra`

Debe recibir una calificación sobre 20 como parámetro.

- Si la calificación es **15 o mayor**, la función debe devolver `"A"`.
- Si la calificación está entre **13 (incluido) y menos de 15**, la función debe devolver `"B"`.
- Si la calificación está entre **12 (incluido) y menos de 13**, la función debe devolver `"C"`.
- Si la calificación está entre **10.5 (incluido) y menos de 12**, la función debe devolver `"D"`.
- Si la calificación es **menor a 10.5**, la función debe devolver `"F"`.

## Método `agregar_curso`

Debe recibir un `nombre_curso` y una `calificacion` como parámetros.

Debe calcular la nota en letra usando `calcular_nota_letra` basado en la calificación.
Luego, debe agregar el `nombre_curso` como clave en el diccionario `__cursos` y la nota calculada como el valor correspondiente.

## Método `obtener_cursos`

Debe devolver el diccionario privado `__cursos`.
