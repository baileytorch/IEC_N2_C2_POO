from negocio.negocio_comunas import cargar_comunas,crear_comuna,buscar_comunas
from datos.repositorio.repositorio_comunas import comuna_por_id
from prettytable import PrettyTable

def mostrar_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas = cargar_comunas(tabla_comunas)
    print(tabla_comunas)

def datos_comuna():
    codigo = input('Ingrese Código de Comuna: ')
    nombre = input('Ingrese Nombre de Comuna: ')
    crear_comuna(codigo,nombre)

def buscar_comuna_nombre(nombre):
    tabla_comunas = PrettyTable()
    tabla_comunas = buscar_comunas(tabla_comunas,nombre)
    print(tabla_comunas)

def datos_actualizar_comuna():
    nombre = input('Ingrese Nombre de Comuna: ')
    buscar_comuna_nombre(nombre)
    id = input('Ingrese Id de Comuna para modificar: ')
    comuna = comuna_por_id(id)
    nombre_nuevo = input('Ingrese Nuevo Nombre de Comuna (o ENTER para conservar): ')
    codigo_nuevo = input('Ingrese Nuevo Código de Comuna (o ENTER para conservar): ')
    