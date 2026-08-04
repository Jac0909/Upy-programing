# Conjugador de verbos en español

pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

verbo = input("Escribe un verbo en infinitivo: ")  # INPUT
verbo = verbo.strip().lower()  # PROCESS - quitamos espacios y pasamos a minúsculas

# Validamos que el verbo tenga sentido antes de intentar conjugarlo
if verbo == '':
    print("No escribiste nada, intenta de nuevo con un verbo válido")  # OUTPUT
elif not verbo.isalpha():
    print("El verbo solo debe contener letras, sin números ni símbolos")  # OUTPUT
elif len(verbo) < 3:
    print("El verbo es muy corto, debe tener al menos raíz + terminación (ej: dar, ir)")  # OUTPUT
else:
    try:
        raiz = verbo[:-2]  # PROCESS
        sufijo = verbo[-2:]  # PROCESS

        if sufijo in terminaciones:
            lista_term = terminaciones[sufijo]
            for i in range(len(pronombres)):
                conjugado = raiz + lista_term[i]  # PROCESS
                print(pronombres[i], conjugado)  # OUTPUT
        else:
            print("Ese verbo no termina en ar, er o ir")  # OUTPUT
    except Exception as e:
        # por si algo raro pasa que no contemplamos arriba
        print("Ocurrió un error inesperado al procesar el verbo:", e)  # OUTPUT
