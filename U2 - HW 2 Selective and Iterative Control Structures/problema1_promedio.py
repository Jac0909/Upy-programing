# Problema 1 - Sistema de Promedio de Calificaciones
# El usuario ingresa calificaciones una por una hasta escribir "done"
# Se calcula el promedio y se indica si aprobo (>=7.0) o reprobo
# INPUT
calificaciones = []
while True:
    entrada = input("Ingresa una calificacion (o 'done' para terminar): ")

    if entrada.lower() == "done":
        break

    calificacion = float(entrada)
    calificaciones.append(calificacion)
# PROCESS
if len(calificaciones) == 0:
    mensaje = "No grades entered. Please enter at least one grade."
else:
    suma = 0
    for nota in calificaciones:
        suma += nota
    promedio = suma / len(calificaciones)
    if promedio >= 7.0:
        estado = "Passed"
    else:
        estado = "Failed"
    mensaje = f"Average: {promedio:.2f} — {estado}"
# OUTPUT
print(mensaje)
