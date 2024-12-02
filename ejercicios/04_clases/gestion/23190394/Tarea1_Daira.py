# Gestión de empleados de la UNMSM
# 04_clases/gestion/UNMSM/
# Daira Trinidad, 23190394
class Empleado:
    # Variables de clase
    nombre_universidad = "Universidad Nacional Mayor de San Marcos"
    total_empleados = 0

    def __init__(self, primer_nombre, apellido, dni, puesto, salario):
        # Variables de instancia
        self.primer_nombre = primer_nombre
        self.apellido = apellido
        self.dni = dni.upper()  
        self.puesto = puesto
        self.salario = salario
        self.hora_ingreso = "08:00 A.M."  
        self.hora_salida = "05:00 P.M."

        # Incrementar el número total de empleados
        Empleado.total_empleados += 1

    # Información completa del empleado
    def obtener_informacion_empleado(self):
        return f"{self.primer_nombre} {self.apellido} - DNI: {self.dni} - Horario: {self.hora_ingreso} - {self.hora_salida}"

    @classmethod
    def obtener_informacion_universidad(cls):
        return f"La universidad {cls.nombre_universidad} tiene {cls.total_empleados} empleados."


# Crear instancias de la clase Empleado
empleado1 = Empleado("Daira", "Trinidad", "78901234", "Investigadora", 1823)
empleado2 = Empleado("Paola", "Maldonado", "72353893", "Investigadora", 3200)  
empleado3 = Empleado("Gabriel", "Laurente", "73097347", "Administrativo", 2900)
empleado4 = Empleado("Kerry", "Martinez", "76316073", "Soporte", 3100)  

print(empleado1.obtener_informacion_empleado())
print(empleado2.obtener_informacion_empleado())
print(empleado3.obtener_informacion_empleado())
print(empleado4.obtener_informacion_empleado())

# Mostrar el total de empleados y la universidad
print(Empleado.obtener_informacion_universidad())

