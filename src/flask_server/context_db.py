from os import environ
from peewee import Model, TextField, PostgresqlDatabase

data = PostgresqlDatabase(
        database=environ.get("DATABASE"),
        user=environ.get("USER"),
        password=environ.get("PASSWORD"),
        host=environ.get("HOST"),
        port=environ.get("PORT")
    )

class UserModel(Model):
    nickname = TextField(null=False)
    password = TextField(null=False)

    class Meta:
        database = data

def run_db():
    data.connect()
    data.create_tables([UserModel])