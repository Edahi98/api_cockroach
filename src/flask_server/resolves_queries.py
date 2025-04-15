from src.flask_server.context_db import UserModel
from src.utilerias.HasherPWD import HasherPWD
from ..utilerias.AuthJWT import AuthJWT
from pyotp import TOTP

def login(_, info, pwd, nickname, code):
    try:
        resultado = UserModel.select().where(UserModel.nickname == nickname).get()
        if HasherPWD.check(resultado.password, pwd):
            totp_object = TOTP(resultado.t2f)
            if totp_object.verify(code):
                return {
                    "token": AuthJWT.generate_token(nickname),
                    "code": 200
                }
            else:
                return {
                    "message": "El usuario no fue encontrado",
                    "code": 402
                }
    except Exception as e:
        print(e)
        return {
            "message": "El usuario no fue encontrado",
            "code": 402
        }

def islogged(_, info, token):
    if AuthJWT.verify_token(token):
        return 200
    else:
        return 401