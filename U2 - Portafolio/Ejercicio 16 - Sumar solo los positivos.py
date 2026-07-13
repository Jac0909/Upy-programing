#16 Suma de numeros positivos
n=[5,10,-50,70,-6,-5,-8]
t=0
for   i in n:
    if i <0:
        continue
    t=t+i
print("total: ",t)