# Ejercicio 13 - Suma de numeros pares
# Pide un numero N y calcula la suma de todos los numeros pares entre 1 y N

n = int(input("Ingresa un numero N: "))

suma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        suma += i

print(f"La suma de los numeros pares entre 1 y {n} es: {suma}")
