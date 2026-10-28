import sys
from datos import nombre_app,version_app,main_menu
from presentacion.presentacion_comunas import mostrar_comunas,datos_comuna,eliminar_comuna
from presentacion.presentacion_usuarios import datos_usuario

def menu_principal():
    print(f'{nombre_app} {version_app}')
    print('='*len(nombre_app) + "=" + '='*len(version_app))

    while True:
        for clave,valor in main_menu.items():
            print(f'[{clave}] - {valor}')

        opcion_usuario = input('Ingrese una opción [1-4]: ')

        match opcion_usuario:
            case '1':
                mostrar_comunas()
            case '2':
                datos_usuario()
            case '3':
                eliminar_comuna()
            case '4':
                print('Saliendo de Sistema')
                sys.exit()
            case _:
                print('Opción Ingresada NO corresponde...\nIngrese nuevamente.')