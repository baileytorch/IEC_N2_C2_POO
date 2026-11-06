from datos.conexion import base_datos
from datos.modelos.pais import Pais

database = base_datos()

def listado_paises():
    listado_paises = Pais.select()
    return listado_paises

def obtener_pais_nombre(nombre):
    try:
        paises = Pais.select().where(Pais.nombre.contains(nombre))
        if paises:
            return paises
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')

def guardar_pais():
    print('GG')