from ..datos.DBConnection import init
from .UserModel import UserModel

def run_db():
    init().connect()
    init().create_tables([UserModel])