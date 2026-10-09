from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField,BooleanField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Direccion(BaseModel):
    id_direccion = AutoField()
    parametro = IntegerField(index=True,null=True)
    comuna = IntegerField(index=True,null=True)
    calle = CharField(max_length=50,null=True)
    numero = CharField(max_length=5,null=True)
    departamento = CharField(max_length=5,null=True)
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = 'direcciones'