from datos.repositorio.repositorio_comunas import listado_comunas,guardar_comuna
from prettytable import PrettyTable
from datos.modelos.comuna import Comuna

def cargar_comunas(tabla: PrettyTable):
    comunas = listado_comunas()
    tabla.field_names = ['Id','Código','Comuna']

    if comunas:
        for comuna in comunas:
            tabla.add_row([comuna.id_comuna, comuna.codigo_comuna, comuna.comuna])

    return tabla

def crear_comuna(codigo,nombre):
    nueva_comuna = Comuna()
    nueva_comuna.codigo_comuna = codigo
    nueva_comuna.comuna = nombre
    comuna = guardar_comuna(nueva_comuna)
    print(f'Se ha guardado la comuna {comuna.comuna}')
