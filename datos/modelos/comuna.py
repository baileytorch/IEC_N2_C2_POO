from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, BooleanField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Comuna(BaseModel):
    id_comuna = AutoField()
    codigo_comuna = CharField(max_length=5)
    nombre_comuna = CharField(max_length=60)
    habilitado = BooleanField()

    class Meta:
        table_name = 'comunas'