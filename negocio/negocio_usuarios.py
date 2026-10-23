from datos.repositorio.repositorio_usuarios import listado_usuarios_habilitados
from prettytable import PrettyTable
from datos.modelos.usuario import Usuario

def cargar_usuarios(tabla: PrettyTable):
    usuarios = listado_usuarios_habilitados()
    tabla.field_names = ['Id','RUT','Nombre Completo','Correo','Origen','Fecha Nacimiento','Género','Fecha Incorporación']

    if usuarios:
        for usuario in usuarios:
            nombre_completo = f'{usuario.nombre} {usuario.apellido}'
            genero_usuario = ''
            match usuario.genero:
                case 184:
                    genero_usuario = 'Masculino'
                case 185:
                    genero_usuario = 'Femenino'
                case 186:
                    genero_usuario = 'Otro'
    
            tabla.add_row([
                usuario.id_usuario, 
                usuario.rut, 
                nombre_completo, 
                usuario.correo, 
                usuario.pais,
                usuario.fecha_nacimiento,
                genero_usuario,
                usuario.fecha_incorporacion])

    return tabla