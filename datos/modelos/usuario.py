from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, DateField, BooleanField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    id_usuario = AutoField()
    rut = CharField(max_length=12)
    nombre = CharField(max_length=25,null=False)
    apellido = CharField(max_length=25,null=False)
    correo = CharField(max_length=255,null=False)
    pais = IntegerField(index=True,null=True)
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField(null=False)
    fecha_incorporacion = DateField(null=False)
    habilitado = BooleanField(default=True)
    password = CharField(max_length=60, null=True)

    class Meta:
        table_name = 'usuarios'