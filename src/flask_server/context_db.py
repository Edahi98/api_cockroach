from os import environ
from peewee import Model, TextField, PostgresqlDatabase, BinaryUUIDField

data = PostgresqlDatabase(
        database=environ.get("DATABASE"),
        user=environ.get("USER"),
        password=environ.get("PASSWORD"),
        host=environ.get("HOST"),
        port=environ.get("PORT"),
        sslmode='require',
    )

class UserModel(Model):
    id = BinaryUUIDField(primary_key=True)
    nickname = TextField(null=False, unique=True)
    password = TextField(null=False, unique=True)

    class Meta:
        database = data
        db_table = "usuario"

def run_db():
    data.connect()
    data.create_tables([UserModel])