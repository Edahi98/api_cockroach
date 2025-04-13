from peewee import PostgresqlDatabase
from os import environ

def init():
    return PostgresqlDatabase(
        database=environ.get("DATABASE"),
        user=environ.get("USER"),
        password=environ.get("PASSWORD"),
        host=environ.get("HOST"),
        port=environ.get("PORT")
    )