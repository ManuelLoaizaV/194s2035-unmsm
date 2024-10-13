# Gestión de cuentas del Banco de la Nación

El **Banco de la Nación del Perú** es una institución financiera encargada de
gestionar las cuentas de sus clientes de manera segura y eficiente.
Una de sus principales funcionalidades es permitir a los clientes depositar y retirar fondos.

Completa la clase `CuentaBancaria`.

## Constructor

Inicializa las variables de instancia privadas
`__numero_cuenta` con el valor de `numero_cuenta` y
`__saldo` con el valor de `saldo_inicial`.

## Getters públicos

Define métodos getters `obtener_numero_cuenta` y `obtener_saldo`,
que devuelvan los valores de las variables privadas.

## Método `depositar`

Debe aceptar un monto como entrada y añadirlo al saldo de la cuenta.

Si el monto del depósito no es positivo,
debe lanzar una excepción `ValueError` con el mensaje: **No se puede depositar fondos negativos o nulos**.
De lo contrario, debe añadir el monto al saldo.

## Método `retirar`

Debe aceptar un monto y verificar si hay suficiente dinero en la cuenta para realizar el retiro.

Si el monto del retiro no es positivo, debe lanzar una excepción `ValueError` con el mensaje:
**No se puede retirar fondos negativos o nulos**.
Luego, si no hay suficientes fondos, debe lanzar una excepción `ValueError` con el mensaje:
**Fondos insuficientes**.
De lo contrario, debe deducir el monto del saldo.
