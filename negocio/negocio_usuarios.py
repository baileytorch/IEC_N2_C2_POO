from datos.repositorio.repositorio_usuarios import listado_usuarios_habilitados,guardar_usuario
from prettytable import PrettyTable
from datos.modelos.usuario import Usuario
from datetime import datetime

def cargar_usuarios(tabla: PrettyTable):
    usuarios = listado_usuarios_habilitados()
    tabla.field_names = ['Id','RUT','Nombre Completo','Correo','Origen','Fecha Nacimiento','Género','Fecha Incorporación']

    if usuarios:
        for usuario in usuarios:
            nombre_completo = f'{usuario.nombre} {usuario.apellido}'
            genero_usuario = ''
            match usuario.genero:
                case 184:
                    genero_usuario = 'Masculino'
                case 185:
                    genero_usuario = 'Femenino'
                case 186:
                    genero_usuario = 'Otro'
    
            tabla.add_row([
                usuario.id_usuario, 
                usuario.rut, 
                nombre_completo, 
                usuario.correo, 
                usuario.pais,
                usuario.fecha_nacimiento,
                genero_usuario,
                usuario.fecha_incorporacion])

    return tabla

def crear_usuario(str_rut, str_nombre, str_apellido, str_correo, id_pais, str_fecha_nacimiento, genero, str_contrasenia):
    nuevo_usuario = Usuario()
    nuevo_usuario.rut = str_rut
    nuevo_usuario.nombre = str_nombre
    nuevo_usuario.apellido = str_apellido
    nuevo_usuario.correo = str_correo
    nuevo_usuario.pais = id_pais
    nuevo_usuario.fecha_nacimiento = datetime.strptime(str_fecha_nacimiento, "%d/%m/%Y")
    
    match genero:
        case '1':
            genero = 184
        case '2':
            genero = 185
        case '3':
            genero = 186

    nuevo_usuario.genero = genero
    nuevo_usuario.fecha_incorporacion = datetime.now()
    nuevo_usuario.habilitado = True
    nuevo_usuario.password = str_contrasenia
    usuario = guardar_usuario(nuevo_usuario)
    if usuario == 1:
        print(f'Usuario gurdado con éxito {nuevo_usuario.nombre} con ID: {nuevo_usuario.id_usuario}')