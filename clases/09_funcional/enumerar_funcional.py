# Anadir de prefijo la posición del alumno en la lista.
# ("Bryan", "Daira", "Evelin", "Gabriel")
# ("1. Bryan", "2. Daira", "3. Evelin", "4. Gabriel")

def anadir_alumno(alumno, alumnos):
    prefijo = f"{len(alumnos) + 1}. "
    nuevo_alumno = prefijo + alumno
    return alumnos + (nuevo_alumno,)


alumnos = ("Bryan", "Daira", "Evelin", "Gabriel")
alumnos_enumerados = ()
for alumno in alumnos:
    alumnos_enumerados = anadir_alumno(alumno, alumnos_enumerados)
print(alumnos_enumerados)
