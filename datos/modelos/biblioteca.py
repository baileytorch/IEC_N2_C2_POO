from datos.conexion import base_datos
from datos.modelos.direccion import Direccion
from peewee import Model, AutoField, CharField, ForeignKeyField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Biblioteca(BaseModel):
    id_biblioteca = AutoField()
    nombre = CharField(max_length=30)
    correo = CharField(null=True)
    telefono = CharField(max_length=20,null=True)
    web = CharField(null=True)
    direccion = ForeignKeyField(Direccion)

    class Meta:
        table_name = 'bibliotecas'