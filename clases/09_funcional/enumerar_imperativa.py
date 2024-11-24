# Anadir de prefijo la posición del alumno en la lista.
# ("Bryan", "Daira", "Evelin", "Gabriel")
# ("1. Bryan", "2. Daira", "3. Evelin", "4. Gabriel")

alumnos = ["Bryan", "Daira", "Evelin", "Gabriel"]

cnt = 0
alumnos_enumerados = []

for alumno in alumnos:
    cnt += 1
    alumnos_enumerados.append(f"{cnt}. {alumno}")

print(alumnos_enumerados)
