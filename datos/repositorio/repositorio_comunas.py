from datos.conexion import base_datos
from datos.modelos.comuna import Comuna
from datos.auxiliar import mensaje_error_orm

database = base_datos()

def listado_comunas():
    comunas = Comuna.select().where(Comuna.habilitado == True)
    return comunas

def guardar_comuna(comuna: Comuna):
    try:
        comuna_nueva = comuna.save()
        return comuna_nueva
    except Exception as error:
        print(f'{mensaje_error_orm} {error}')

def comuna_por_nombre(nombre):
    try:
        comunas = Comuna.select().where(Comuna.nombre_comuna.contains(nombre), Comuna.habilitado == True)
        if comunas:
            return comunas
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def comuna_por_id(id):
    try:
        comuna = Comuna[id]
        if comuna:
            return comuna
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')