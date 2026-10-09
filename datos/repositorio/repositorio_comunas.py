from datos.conexion import base_datos
from datos.modelos.comuna import Comuna

database = base_datos()

def listado_comunas():
    comunas = Comuna.select()
    return comunas

def guardar_comuna(comuna: Comuna):
    comuna_nueva = comuna.save()
    return comuna_nueva