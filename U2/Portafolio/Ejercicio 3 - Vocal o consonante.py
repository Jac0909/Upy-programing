#vocal o consonante
letra=input("Ingresar una letra: ")
vocal = letra.lower() in "aeiou" #<-upper es para hacer todas las letras a mayuscula usando la variable( letra ) agregamos ( . ) y ponemos ( upper ) queda asi
                    #caso contrario lower vuelve todas las letras de la variable a minusculas
print(vocal)