from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Comuna(BaseModel):
    id_comuna = AutoField()
    codigo_comuna = CharField(max_length=5)
    comuna = CharField(max_length=60)

    class Meta:
        table_name = 'comunas'