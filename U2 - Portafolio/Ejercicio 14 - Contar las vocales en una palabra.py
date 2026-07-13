# Ejercicio 14 - Contar las vocales en una palabra
# Pide una palabra al usuario y cuenta cuantas vocales contiene

palabra = input("Ingresa una palabra: ")

vocales = "aeiouAEIOU"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra '{palabra}' tiene {contador} vocal(es).")
