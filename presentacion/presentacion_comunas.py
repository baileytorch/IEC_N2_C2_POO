from negocio.negocio_comunas import cargar_comunas,crear_comuna,buscar_comunas
from datos.repositorio.repositorio_comunas import comuna_por_id,guardar_comuna
from datos.modelos.comuna import Comuna
from prettytable import PrettyTable

def mostrar_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas = cargar_comunas(tabla_comunas)
    print(tabla_comunas)

def datos_comuna():
    codigo = input('Ingrese Código de Comuna: ')
    nombre = input('Ingrese Nombre de Comuna: ')
    crear_comuna(codigo,nombre.title())

def buscar_comuna_nombre(nombre):
    tabla_comunas = PrettyTable()
    tabla_comunas = buscar_comunas(tabla_comunas,nombre)
    print(tabla_comunas)

def actualizar_comuna():
    nombre = input('Ingrese Nombre de Comuna: ')
    buscar_comuna_nombre(nombre)
    id_ingresado = input('Ingrese Id de Comuna para modificar: ')
    comuna = comuna_por_id(id_ingresado)
    nombre_nuevo = input('Ingrese Nuevo Nombre de Comuna (o ENTER para conservar): ')
    codigo_nuevo = input('Ingrese Nuevo Código de Comuna (o ENTER para conservar): ')

    if nombre_nuevo != '':
        comuna.nombre_comuna = nombre_nuevo.title()
    if codigo_nuevo != '':
        comuna.codigo_comuna = codigo_nuevo
    respuesta = guardar_comuna(comuna)
    if respuesta ==1:
        print(f'Comuna {comuna.nombre_comuna} actualizada con éxito')

def eliminar_comuna():
    nombre = input('Ingrese Nombre de Comuna: ')
    buscar_comuna_nombre(nombre)
    id_ingresado = input('Ingrese Id de Comuna para eliminar: ')
    comuna = comuna_por_id(id_ingresado)
    comuna.habilitado = False
    respuesta = guardar_comuna(comuna)
    if respuesta ==1:
        print(f'Comuna {comuna.nombre_comuna} eliminada con éxito')