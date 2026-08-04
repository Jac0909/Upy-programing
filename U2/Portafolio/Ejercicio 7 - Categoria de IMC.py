# 17 Categoria IMC
#IMC < 18.5= flaco
#18.5 <= IMC < 25= normal
#25 <= IMC < 30= gordito
#30 <= IMC=majim boo
w=float(input("Ingrese su altura: "))
h=float(input("Ingrese su altura: (m): "))
IMC=w/(h*h)
if IMC<18.5:
    print("flaco")
elif 18.5 <= IMC < 25:
    print("normal")
elif 25 <= IMC < 30:
    print("gordito")
else:
    print("majim boo")
