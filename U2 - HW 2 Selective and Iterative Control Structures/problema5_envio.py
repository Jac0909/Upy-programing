# Problema 5 - Calculadora de Costo de Envio
# El usuario ingresa peso y distancia de varios paquetes
# Se calcula el costo de envio segun reglas y se acumula el total
total_acumulado = 0
while True:
    # INPUT
    entrada_peso = input("Ingresa el peso en kg (o 'exit' para terminar): ")
    if entrada_peso.lower() == "exit":
        break
    peso = float(entrada_peso)
    distancia = float(input("Ingresa la distancia en km: "))
    # PROCESS
    if distancia <= 100:
        if peso <= 5:
            costo = 50.00
        else:
            costo = 80.00
    else:
        if peso <= 5:
            costo = 120.00
        else:
            costo = 200.00

    total_acumulado += costo
    # OUTPUT
    print(f"Shipping cost: ${costo:.2f} MXN")
print(f"Total: ${total_acumulado:.2f} MXN")
