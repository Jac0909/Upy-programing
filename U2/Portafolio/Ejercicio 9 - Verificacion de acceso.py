# Ejercicio 9 - Verificacion de acceso
# Pide la edad del usuario y verifica si tiene acceso permitido (mayor o igual a 18 anios)

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Acceso PERMITIDO. Bienvenido.")
else:
    print("Acceso DENEGADO. Debes ser mayor de edad.")
