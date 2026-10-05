# IEC_N2_C2_POO
Desarrollo de Proyecto de Programación Orientada a Objetos

Clase 07/09/2026
___

El desarrollo modular es una técnica de diseño de software que consiste en dividir un programa en partes independientes más pequeñas llamadas módulos. Cada módulo se encarga de una funcionalidad específica y se puede comunicar con los demás a través de interfaces bien definidas.

## Beneficios clave

- Facilidad de mantenimiento: Si hay un error, sabes exactamente en qué módulo buscar y puedes arreglarlo sin romper el resto del sistema.
- Reutilización de código: Un mismo módulo (por ejemplo, el sistema de autenticación de usuarios o la conexión a la base de datos) puede usarse en diferentes partes del proyecto o en proyectos futuros.
- Trabajo en equipo: Permite que varios programadores trabajen simultáneamente en diferentes partes del código sin pisarse el trabajo de los demás.
- Escalabilidad: Añadir nuevas funciones es tan fácil como crear un módulo nuevo e integrarlo en el flujo existente.

## Control DataBase
- Para controlar la base de datos necesitamos tener un usuario específico, con permisos explícitos para trabajar sobre una base de datos definida. Esto lo lograremos ejecutando las siguientes sentencias SQL:
```
CREATE USER 'nombre_usuario'@'nombre_servidor' IDENTIFIED WITH caching_sha2_password BY 'contraseña_usuario';
```

- Le asignamos los permisos a nuestra base de datos completa ejecutando la siguiente sentencia SQL:
```
GRANT ALL PRIVILEGES ON mi_base_datos.* TO 'nombre_usuario'@'nombre_servidor';
```

- Finalmente debemos grabar esos privilegios con la siguiente sentencia SQL:
```
FLUSH PRIVILEGES;
```

Para conectarnos a la base de datos desde nuestra aplicación usaremos el ORM *Pewee* y el driver de base de datos *Pymysql*.
- *ORM*: Un ORM (Object-Relational Mapping o mapeo objeto-relacional) es una técnica de programación que permite conectar una base de datos relacional con el código de una aplicación *POO*, traduciendo las tablas en clases y los registros en objetos.
- Teniendo compeltamente creada nuestra estructura de datos, usaremos una herramienta automatizada de Peewee para crear nuestras clases, ejecutando el siguiente comando por terminal:
```
python -m pwiz -e mysql -H localhost -p 3306 -u your_username -P your_database_name > models.py
```

## Control de dependencias
Para tener un mejor control de las dependencias de nuestros proyectos, es conveniente crear un archivo *requirements.txt* que contendrá la lista de dependencias con sus números de versión, lo que permitirá además hacer una isntalación rápida de todas las librerías que contiene.
Si ya tenemos un archivo *requirements.txt* en el directorio principal de nuestro proyecto, ejecutaremos la instalación mediante el siguiente comando por terminal:
```
pip install -r requirements.txt
```

Si no tenemos un archivo, pero ya hemos instalado las librerías, podemos crearlo con el siguiente comando por terminal:
```
pip freeze > requirements.txt
```
