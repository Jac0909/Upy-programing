# Ejercicio 11 - Suma de 1 a N
# Pide un numero N y calcula la suma de todos los numeros de 1 a N

n = int(input("Ingresa un numero N: "))

suma = 0
for i in range(1, n + 1):
    suma += i

print(f"La suma de 1 a {n} es: {suma}")
