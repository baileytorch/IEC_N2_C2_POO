# from datos.modelos.autor import Autor
from datos.conexion import base_datos

def guardar_autor(autor):
    db = base_datos()
    db.connect()
    autor.save()
    db.close()