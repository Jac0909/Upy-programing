#12 factorial
#13 suma de numeros pares
#14 contar vocales dentro de una palabra

palabra=input("Ingrese una palabra: ")
contar=0
for i in palabra.lower():
    if i in "aeiou":
        contar+=1
print("La cantidad de vocales en la palabra es:", contar)
