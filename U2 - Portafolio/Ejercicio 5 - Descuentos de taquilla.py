#Discount
#children year > 12 = 30%
#children 12< year <25 = 20%(with ID)
#adultos 26-64 = no discount
#grandfathers 65 >= :40% discount
price = 150
age=int(input("Ingresa la edad:"))
id=input("¿Tiene tarjeta? (Si/No): ")

if age < 12:
    rate=.30
elif age <=12 and id =="si":
    rate=.20
elif age <=64:
    rate =0.00
else:
    rate=0.40
n_price=price*(1-rate)
print(f"Price $: {n_price}")


