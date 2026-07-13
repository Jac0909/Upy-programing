# Ejercicio 8 - Estado del agua
# Pide una temperatura en grados Celsius y determina el estado del agua

temperatura = float(input("Ingresa la temperatura del agua en grados Celsius: "))

if temperatura <= 0:
    print("El agua esta en estado SOLIDO (hielo).")
elif temperatura < 100:
    print("El agua esta en estado LIQUIDO.")
else:
    print("El agua esta en estado GASEOSO (vapor).")
