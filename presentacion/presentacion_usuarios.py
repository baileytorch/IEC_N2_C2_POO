from negocio.negocio_usuarios import cargar_usuarios,crear_usuario
from negocio.negocio_paises import buscar_pais
from datos.repositorio.repositorio_comunas import comuna_por_id,guardar_comuna
from prettytable import PrettyTable
import re

def mostrar_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios = cargar_usuarios(tabla_usuarios)
    print(tabla_usuarios)

def datos_usuario():
    rut = nombre = apellido = correo = nombre_pais = fecha_nacimiento = genero = contrasenia = ''
    print('\nIngrese Datos Usuario')

    while rut == '':
        rut = input('RUT: ')
    while nombre == '':
        nombre = input('Nombre: ')
    while apellido == '':
        apellido = input('Apellido: ')
    while correo == '':
        correo = input('Correo: ')
        patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_correo, correo):
            print('Correo electrónico NO corresponde, ingrese nuevamente...')
            correo = ''
    while nombre_pais == '':
        nombre_pais = input('Nombre País: ')
        tabla_paises = PrettyTable()
        tabla_paises = buscar_pais(tabla_paises, nombre_pais)
        print(tabla_paises)
        id_pais = input('Id País: ')

    while fecha_nacimiento == '':
        fecha_nacimiento = input('Fecha Nacimiento (dd/MM/aaaa): ')

    while genero == '':
        print('Opciones de Género')
        print('[1] Masculino')
        print('[2] Femenino')
        print('[3] Otro')
        genero = input('Opción Género [1-3]: ')
        if genero not in ['1','2','3']:
            print('Género NO corresponde, ingrese nuevamente...')
            genero = ''

    while contrasenia == '':
        patron_contrasenia = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$'
        print('Ingrese una contraseña segura:')
        print('Al menos una minúscula\nAl menos una mayúscula\nAl menos un dígito\nAl menos un caracter especial')
        print('Al menos 8 caracteres de largo')
        contrasenia = input('Contraseña: ')
        if not re.match(patron_contrasenia, contrasenia):
            print('Su contraseña NO es segura, ingrese nuevamente...')
            contrasenia = ''
    crear_usuario(rut, nombre.title(), apellido.title(), correo, id_pais, fecha_nacimiento, genero, contrasenia)