from presentacion import menu_principal
from datos.modelos.autor import Autor
from datos.repositorio.repositorio_autores import guardar_autor

from prettytable import PrettyTable

# menu_principal()

# autor = Autor(
#         nombre='Arthur Frederick Hailey',
#         pseudonimo='',
#         nacionalidad=143,
#         fecha_nacimiento='1920-4-5',
#         fecha_defuncion='2004-11-24',)

# guardar_autor(autor)

from datos.repositorio import repositorio_paises

listado_paises = repositorio_paises.listado_paises()
tabla_paises = PrettyTable()
tabla_paises.field_names = ['Id','País','Nacionalidad','ISO 2','ISO 3']

if listado_paises:
    for pais in listado_paises:
        tabla_paises.add_row([pais.id_pais, pais.nombre, pais.nacionalidad, pais.iso_2, pais.iso_3])

print(tabla_paises)