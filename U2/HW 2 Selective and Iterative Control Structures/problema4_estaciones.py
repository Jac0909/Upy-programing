# Problema 4 - Clasificador de Estaciones
# El usuario ingresa numeros de mes uno por uno
# Se muestra la estacion correspondiente hasta que escriba "exit"
while True:
    # INPUT
    entrada = input("Ingresa el numero de mes (o 'exit' para terminar): ")
    if entrada.lower() == "exit":
        break
    mes = int(entrada)
    # PROCESS
    if mes < 1 or mes > 12:
        resultado = "Invalid month. Please enter a number between 1 and 12."
    elif mes in (12, 1, 2):
        resultado = "Winter"
    elif mes in (3, 4, 5):
        resultado = "Spring"
    elif mes in (6, 7, 8):
        resultado = "Summer"
    else:
        resultado = "Fall"
    # OUTPUT
    print(resultado)
