# ¿Por qué Python?

Muchos estudiantes se inician en la programación con Python.
Python es famoso por ser simple y fácil de leer y escribir.
Que sea simple no significa que no sea útil.
Python es brutalmente popular en las ciencias e ingenierías en diversos casos de usos:

- Aprendizaje de máquina
- Scripting
- Backend
- DevOps

Por otro lado, Python no es comúnmente utilizado para implementar interfaces gráficas.

## ¿Qué es código?

Código es una serie de instrucciones que las computadoras siguen una después de otra.
Un programa está conformado por muchas instrucciones.
Imprimir es una de las instrucciones más comunes en programación.

## Imprimiendo

`print` puede imprimir texto utilizando comillas

```python
print("Hola, mundo!")
```

pero también puede imprimir números sin utilizar comillas

```python
print(42)
```

e incluso realizar operaciones dentro de los paréntesis:

```python
print(46 + 23)
```

## Múltiples instrucciones

El código se ejecuta en orden,
comenzando desde el inicio del programa.

```python
print("Primero")
print("Segundo")
print("Tercero")
```

Cada `print` imprime en una nueva línea.

## Errores de sintaxis

Sintaxis es el conjunto de reglas que definen cómo escribir código válido en un lenguaje de programación.

Por ejemplo,
el siguiente código tiene sintaxis inválida:

```python
print("Soy incorrecto')
```

El código es incorrecto porque las comillas no están emparejadas alrededor de la cadena `Soy incorrecto`.

## Variables

Las variables son abstracciones que utilizamos para almacenar datos en nuestros programas.
Hasta ahora solo hemos impreso datos pasados directamente a la función `print`.

Una variable es un nombre que definiremos el cual apuntará a cierto dato.
Por ejemplo, puedo definir una variable llamada
`mi_altura` y asignarle el valor `175`.

Para crear una nueva variable en Python debemos usar la siguiente sintaxis:

```python
especie_favorita = "oranguntanes"
esto_puede_llamarse_como_sea = 2024
```

El valor de una variable puede cambiar.
Por ejemplo, el siguiente ejemplo imprime `15`.

```python
n = 314
n = 15
print(n)
```

La línea `n = 15` reasigna el valor de `n` a `20`.

## Comentarios

Los comentarios no son ejecutados sino ignorados.
Estos suelen ser de utilidad para añadir recordatorios
o explicar qué hace cierto fragmento de código.

### Single-line
```python
# La variable p guarda el valor del primer número primo mayor o igual a 100.
p = 101
```

### Multi-line (docstring)
```python
"""
El código a continuación tiene como objetivo
imprimir Hola, mundo! en la consola.
"""
print("Hola, mundo!")
```

## Nombres de variables

```python
# No hagan esto en casa
nombredeunavariable = 42

# Camel Case
nombreDeUnaVariable = 42

# Snake Case
nombre_de_una_variable = 42

# Pascal Case
NombreDeUnaVariable = 42
```

## Tipos de datos

### Cadena

```python
nombre_entre_comillas_simples = 'Manuel'
nombre_entre_comillas_dobles = "Manuel"
```

### Entero

```python
x = 3
y = -3
```

### Flotante

```python
x = 3.14
y = -3.14
```

### Booleano

```python
moriremos = True
no_moriremos = False
```
