from datos.conexion import base_datos
from peewee import Model, AutoField, CharField, IntegerField, DateField, TextField

database = base_datos()

class BaseModel(Model):
    class Meta:
        database = database

class Autor(BaseModel):
    id_autor = AutoField()
    nombre = CharField(max_length=50,null=True)
    pseudonimo = CharField(max_length=50,null=True)
    nacionalidad = IntegerField(index=True,null=True)
    fecha_nacimiento = DateField(null=True)
    fecha_defuncion = DateField(null=True)
    biografia = TextField(null=True)

    class Meta:
        table_name = 'autores'