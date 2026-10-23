from datos.conexion import base_datos
from datos.modelos.usuario import Usuario
from datos.auxiliar import mensaje_error_orm

database = base_datos()

def listado_usuarios_habilitados():
    usuarios = Usuario.select().where(Usuario.habilitado == True)
    return usuarios

def listado_usuarios_deshabilitados():
    usuarios = Usuario.select().where(Usuario.habilitado == False)
    return usuarios

def listado_usuarios():
    usuarios = Usuario.select()
    return usuarios

def guardar_usuario(usuario: Usuario):
    try:
        nuevo_usuario = usuario.save()
        return nuevo_usuario
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def usuario_por_nombre(rut):
    try:
        usuarios = Usuario.select().where(Usuario.rut == rut)
        if usuarios:
            return usuarios
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def usuario_por_id(id):
    try:
        usuario = Usuario[id]
        if usuario:
            return usuario
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')