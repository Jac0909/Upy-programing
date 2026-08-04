materias = ('Matemáticas', 'Programación', 'Inglés')

usuarios = {
    'coord1': {'password': 'coord123', 'rol': 'coordinador', 'nombre': 'Laura Pérez'},
    'maestro1': {'password': 'maestro123', 'rol': 'maestro', 'nombre': 'Carlos Ramírez'},
    'alu1': {'password': 'alu123', 'rol': 'alumno', 'nombre': 'Ana Torres'},
    'alu2': {'password': 'alu123', 'rol': 'alumno', 'nombre': 'Luis Gómez'},
    'alu3': {'password': 'alu123', 'rol': 'alumno', 'nombre': 'María Sánchez'},
    'alu4': {'password': 'alu123', 'rol': 'alumno', 'nombre': 'Jorge Díaz'},
    'alu5': {'password': 'alu123', 'rol': 'alumno', 'nombre': 'Paola Ruiz'},
    'alu6': {'password': 'alu123', 'rol': 'alumno', 'nombre': 'Diego Flores'}
}

calificaciones = {
    'alu1': {'Matemáticas': 9.0, 'Programación': 7.5, 'Inglés': 8.0},
    'alu2': {'Matemáticas': 6.5, 'Programación': 9.2, 'Inglés': 7.0},
    'alu3': {'Matemáticas': 8.5, 'Programación': 8.0, 'Inglés': 6.0},
    'alu4': {'Matemáticas': 5.0, 'Programación': 6.5, 'Inglés': 7.8},
    'alu5': {'Matemáticas': 9.5, 'Programación': 9.0, 'Inglés': 9.1},
    'alu6': {'Matemáticas': 7.0, 'Programación': 5.5, 'Inglés': 8.2}
}

print('=== SISTEMA DE GESTIÓN ESCOLAR ===')

autenticado = False
usuario_actual = ''
intentos = 0

# login con límite de intentos para que no se quede pegado si el usuario
# se equivoca una y otra vez, y validación de campos vacíos
while autenticado == False and intentos < 5:
    user = input('Usuario: ').strip()  # INPUT
    pw = input('Contraseña: ').strip()  # INPUT

    if user == '' or pw == '':
        print('Usuario y contraseña no pueden estar vacíos, intenta de nuevo.')  # OUTPUT
        intentos = intentos + 1
        continue

    if user in usuarios and usuarios[user]['password'] == pw:
        autenticado = True
        usuario_actual = user
        print('Login exitoso, bienvenido/a', usuarios[user]['nombre'])  # OUTPUT
    else:
        intentos = intentos + 1
        print('Usuario o contraseña incorrectos, intenta de nuevo. (Intento', intentos, 'de 5)')  # OUTPUT

if autenticado == False:
    print('Superaste el número de intentos permitidos. Cerrando el programa.')  # OUTPUT
else:
    rol_actual = usuarios[usuario_actual]['rol']

    if rol_actual == 'alumno':
        nombre = usuarios[usuario_actual]['nombre']
        print('--- Bienvenido/a', nombre, '---')
        print('Tus calificaciones son:')

        notas_alumno = calificaciones[usuario_actual]
        aprobadas = set()
        todas_materias = set(materias)

        for materia in materias:
            nota = notas_alumno[materia]
            print(materia, ':', nota)
            if nota >= 8.0:
                aprobadas.add(materia)

        pendientes = todas_materias - aprobadas

        print('Materias aprobadas:', aprobadas)
        print('Materias pendientes:', pendientes)

    elif rol_actual == 'maestro':
        print('--- Menú Maestro ---')
        print('Lista de alumnos:')

        for u in usuarios:
            if usuarios[u]['rol'] == 'alumno':
                print(u, '-', usuarios[u]['nombre'])

        # validamos que el alumno exista de verdad antes de seguir
        alumno_elegido = input('Escribe el usuario del alumno a calificar: ').strip()  # INPUT

        while alumno_elegido not in usuarios or usuarios[alumno_elegido]['rol'] != 'alumno':
            alumno_elegido = input('Usuario inválido, intenta otra vez: ').strip()  # INPUT

        # validamos que la materia sea una de las que existen
        materia_elegida = input('Escribe la materia a calificar: ').strip()  # INPUT

        while materia_elegida not in materias:
            materia_elegida = input('Materia inválida, escribe una de la lista ' + str(materias) + ': ').strip()  # INPUT

        # validamos que la nota sea un número real entre 0 y 10
        nueva_nota = None
        while nueva_nota is None:
            entrada_nota = input('Escribe la nueva calificación: ')  # INPUT
            try:
                nota_temp = float(entrada_nota)  # PROCESS
                if nota_temp < 0 or nota_temp > 10:
                    print('La calificación debe estar entre 0 y 10, intenta de nuevo.')  # OUTPUT
                else:
                    nueva_nota = nota_temp
            except ValueError:
                print('Eso no es un número válido, intenta de nuevo.')  # OUTPUT

        calificaciones[alumno_elegido][materia_elegida] = nueva_nota  # PROCESS

        print('Calificación actualizada correctamente.')  # OUTPUT
        print(alumno_elegido, 'ahora tiene', nueva_nota, 'en', materia_elegida)  # OUTPUT

    elif rol_actual == 'coordinador':
        print('--- Reporte del Coordinador ---')

        print('1) Maestros:')
        for u in usuarios:
            if usuarios[u]['rol'] == 'maestro':
                print('-', usuarios[u]['nombre'])

        print('2) Materias:')
        for m in materias:
            print('-', m)

        print('3) Estudiantes y calificaciones:')
        for u in usuarios:
            if usuarios[u]['rol'] == 'alumno':
                print(usuarios[u]['nombre'], ':', calificaciones[u])

    print('--- Fin del programa ---')
