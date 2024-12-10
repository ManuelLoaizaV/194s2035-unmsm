class Empleado:
    nombre_universidad = "Universidad Nacional Mayor de San Marcos"
    total_empleados = 0

    def __init__(self, primer_nombre, apellido, dni, puesto, salario):
        self.primer_nombre = primer_nombre
        self.apellido = apellido
        self.dni = dni
        self.puesto = puesto
        self.salario = salario
        Empleado.total_empleados += 1

    def obtener_nombre(self):
        return f"{self.primer_nombre} {self.apellido}"

while True:
    primer_nombre = input("Ingrese el primer nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese el DNI: ")
    puesto = input("Ingrese el puesto: ")
    salario = float(input("Ingrese el salario: "))

    empleado = Empleado(primer_nombre, apellido, dni, puesto, salario)

    print("\nDATOS DEL EMPLEADO")
    print("Nombre completo del empleado:", empleado.obtener_nombre())
    print("Total de empleados:", Empleado.total_empleados)
    
    agregar_otro = input("\n¿Desea agregar otro empleado? (s/n): ")
    if agregar_otro.lower() != 's':
        break
