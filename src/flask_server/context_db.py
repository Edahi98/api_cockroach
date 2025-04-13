from os import environ
from peewee import Model, TextField, PostgresqlDatabase, BinaryUUIDField

data = PostgresqlDatabase(
        database=environ.get("DATABASE"),
        user=environ.get("USER"),
        password=environ.get("PASSWORD"),
        host=environ.get("HOST"),
        port=environ.get("PORT")
    )

class UserModel(Model):
    id = BinaryUUIDField(primary_key=True)
    nickname = TextField(null=False)
    password = TextField(null=False)

    class Meta:
        database = data
        db_table = "user"

def run_db():
    data.connect()
    data.create_tables([UserModel])