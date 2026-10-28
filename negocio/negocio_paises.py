from prettytable import PrettyTable
from datos.modelos.pais import Pais
from datos.repositorio.repositorio_paises import obtener_pais_nombre

def buscar_pais(tabla: PrettyTable,nombre):
    paises = obtener_pais_nombre(nombre)
    tabla.field_names = ['Id','Nombre','Nacionalidad','ISO 2','ISO 3']

    if paises:
        for pais in paises:
            tabla.add_row([pais.id_pais, pais.nombre, pais.nacionalidad, pais.iso_2, pais.iso_3])

    return tabla