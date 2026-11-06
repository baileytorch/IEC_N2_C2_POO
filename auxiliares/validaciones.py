import re

def validar_rut(rut):
    rut_limpio = rut.replace('.', '').replace('-', '')
    dig_ver = rut_limpio[-1]
    num_rut = rut_limpio[:-1]
    rut_invertido = num_rut[::-1]
    
    multiplicador = 2
    suma = 0
    
    for num in rut_invertido:
        suma += int(num) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
            
    resto = suma % 11
    final = 11 - resto
    
    digito_calculado = ''
    if final == 11:
        digito_calculado = '0'
    elif final == 10:
        digito_calculado = 'k'
    else:
        digito_calculado = str(final)
        
    if digito_calculado.upper() == dig_ver.upper():
        return True
    else:
        return False

def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron_correo, correo):
        return False
    else:
        return True

def validar_contrasenia_segura(contrasenia):
    patron_contrasenia = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){8,15}$'
    if not re.match(patron_contrasenia, contrasenia):
        return False
    else:
        return True
    
def validar_genero(genero):
    if genero not in ['1','2','3']:
        return False
    else:
        return True