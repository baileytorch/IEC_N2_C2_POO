from negocio.negocio_comunas import cargar_comunas
from prettytable import PrettyTable

def mostrar_comunas():
    tabla_comunas = PrettyTable()
    tabla_comunas = cargar_comunas(tabla_comunas)
    print(tabla_comunas)