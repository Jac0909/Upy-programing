# Problema 3 - Calculadora de Recibo de Agua
# El usuario ingresa m3 consumidos por varios meses
# Se calcula el cargo por mes con tarifas escalonadas y se acumula el total
total_acumulado = 0
while True:
    # INPUT
    entrada = input("Ingresa los m3 consumidos (o 'exit' para terminar): ")
    if entrada.lower() == "exit":
        break
    m3 = float(entrada)
    # PROCESS
    if m3 <= 10:
        cargo = m3 * 8.00
    elif m3 <= 20:
        cargo = m3 * 12.00
    else:
        cargo = m3 * 18.00
    total_acumulado += cargo
    # OUTPUT
    print(f"Month charge: ${cargo:.2f} MXN")
print(f"Total: ${total_acumulado:.2f} MXN")
