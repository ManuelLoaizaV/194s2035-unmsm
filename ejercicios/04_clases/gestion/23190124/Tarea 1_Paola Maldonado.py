class Empleado: 
    nombre_de_universidad = "Universidad Nacional Mayor de San Marcos"
    total_de_empleados = 0

    def __init__(self, dni, ape_pat, ape_mat, nombre, ocupacion, horas_dtrabajo, salario):
        self.dni = dni
        self.ape_pat = ape_pat
        self.ape_mat = ape_mat
        self.nombre = nombre
        self.ocupacion = ocupacion
        self.horas_dtrabajo = horas_dtrabajo
        self.salario = salario
        Empleado.total_de_empleados += 1
    
    def agregar_hora(self):
        self.horas_dtrabajo += 1

    def presentar(self):
        print(f"{self.ape_pat} {self.ape_mat} {self.nombre} trabaja en la {self.nombre_de_universidad} como {self.ocupacion}, trabaja {self.horas_dtrabajo} horas y gana un sueldo digno de {self.salario} soles.")

    def obtener_total_empleados(cls):
        return cls.total_de_empleados
    
anam = Empleado(85245613, "Mendoza", "Aguayo", "Ana", "portera", 6, 800)
anam.presentar()

monicac = Empleado(82580613, "Rios", "Nuñez", "Mónica", "Personal de limpieza", 4, 800)
monicac.presentar()

roger = Empleado(78455613, "Mendoza", "Aguayo", "Roger", "portero", 6, 800)
roger.presentar()

print(f"Total de empleados: {Empleado.total_de_empleados}")