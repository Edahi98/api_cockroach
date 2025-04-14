from src.flask_server.context_db import UserModel
from src.utilerias.HasherPWD import HasherPWD
from ..utilerias.AuthJWT import AuthJWT


def login(_, info, pwd, nickname):
        print(f"LOGIN: PWD {pwd}")
        print(f"LOGIN: NICK {nickname}")
        resultado = UserModel.select().where(UserModel.nickname == nickname).get()
        print(f"RESULT BD: PWD {resultado.password}")
        if HasherPWD.check(resultado.password, pwd):
            return {
                "token": AuthJWT.generate_token(nickname),
                "code": 200
            }
        
def islogged(_, info, token):
    if AuthJWT.verify_token(token):
        return 200
    else:
        return 401