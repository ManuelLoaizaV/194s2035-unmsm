# Gestión de Empleados de la UNMSM

La *Universidad Nacional Mayor de San Marcos (UNMSM)* está en constante crecimiento.
Necesitan una forma de hacer seguimiento a todos sus empleados, especialmente a los nuevos contratados.
Te han pedido que desarrolles una herramienta interna para ayudar en la gestión de los empleados.

El líder de tu equipo te ha pedido que tomes una decisión de diseño interesante.
Te ha solicitado que uses *variables de clase* para llevar el control del nombre de la universidad y
del número total de empleados dentro de la clase Empleado
(lo ideal sería crear otra clase para la universidad, pero, al final, él manda).

## Variables de clase

Inicializa las siguientes variables de clase:

- nombre_universidad debe estar inicializada como "Universidad Nacional Mayor de San Marcos".
- total_empleados debe estar inicializada en 0.

## Constructor

El constructor debe recibir los siguientes parámetros y asignarlos a las variables de instancia correspondientes:
primer_nombre, apellido, dni, puesto y salario.

Además, el constructor debe *incrementar* la variable de clase total_empleados
cada vez que se cree un nuevo Empleado.
Recuerda que total_empleados es una *variable de clase*, no una variable de instancia.

## Getter

Agrega un método obtener_nombre que devuelva el nombre completo del empleado como una cadena
(por ejemplo, "Manuel Loaiza").