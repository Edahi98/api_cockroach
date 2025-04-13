from ..datos.DBConnection import init
from peewee import Model, TextField

class UserModel(Model):
    nickname = TextField(null=False)
    password = TextField(null=False)

    class Meta:
        database = init()
