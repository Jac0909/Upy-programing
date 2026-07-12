# Problema 2 - Calculadora de IMC
# El usuario ingresa peso y estatura de varias personas
# Se calcula el IMC y se clasifica hasta que escriba "exit" en peso
while True:
    # INPUT
    entrada_peso = input("Ingresa el peso en kg (o 'exit' para terminar): ")
    if entrada_peso.lower() == "exit":
        break
    peso = float(entrada_peso)
    altura = float(input("Ingresa la altura en metros: "))
    # PROCESS
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Underweight"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Overweight"
    else:
        categoria = "Obese"
    # OUTPUT
    print(f"BMI: {imc:.2f} — {categoria}")
