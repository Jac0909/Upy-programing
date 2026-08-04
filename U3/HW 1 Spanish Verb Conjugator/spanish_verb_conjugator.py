# Conjugador de verbos en español

pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

verbo = input("Escribe un verbo en infinitivo: ")  # INPUT

raiz = verbo[:-2]  # PROCESS
sufijo = verbo[-2:]  # PROCESS

if sufijo in terminaciones:
    lista_term = terminaciones[sufijo]
    for i in range(len(pronombres)):
        conjugado = raiz + lista_term[i]  # PROCESS
        print(pronombres[i], conjugado)  # OUTPUT
else:
    print("Ese verbo no termina en ar, er o ir")  # OUTPUT