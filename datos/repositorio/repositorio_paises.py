from datos.conexion import base_datos
from datos.modelos.pais import Pais

database = base_datos()

def listado_paises():
    listado_paises = Pais.select()
    return listado_paises

def obtener_pais_nombre():
    print('GG')

def guardar_pais():
    print('GG')

def actualizar_pais():
    print('GG')

def eliminar_pais():
    print('GG')