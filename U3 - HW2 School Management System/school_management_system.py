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

while autenticado == False:
    user = input('Usuario: ')
    pw = input('Contraseña: ')

    if user in usuarios and usuarios[user]['password'] == pw:
        autenticado = True
        usuario_actual = user
        print('Login exitoso, bienvenido/a', usuarios[user]['nombre'])
    else:
        print('Usuario o contraseña incorrectos, intenta de nuevo.')

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

    alumno_elegido = input('Escribe el usuario del alumno a calificar: ')

    while alumno_elegido not in usuarios or usuarios[alumno_elegido]['rol'] != 'alumno':
        alumno_elegido = input('Usuario inválido, intenta otra vez: ')

    materia_elegida = input('Escribe la materia a calificar: ')

    while materia_elegida not in materias:
        materia_elegida = input('Materia inválida, escribe una de la lista ' + str(materias) + ': ')

    nueva_nota = float(input('Escribe la nueva calificación: '))

    calificaciones[alumno_elegido][materia_elegida] = nueva_nota

    print('Calificación actualizada correctamente.')
    print(alumno_elegido, 'ahora tiene', nueva_nota, 'en', materia_elegida)

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