from peewee import PostgresqlDatabase
from ..flask_server.run_server import app
from os import environ

def prepare_connection(key_db, key_host, key_user):
    return PostgresqlDatabase(
            database=environ.get(key_db),
            host=environ.get(key_host))

def init():
    db: PostgresqlDatabase
    if app.debug:
        db = PostgresqlDatabase(
            database=environ.get(""),
            host="")