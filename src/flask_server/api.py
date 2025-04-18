from secrets import token_hex
from uuid import uuid4
from src.flask_server.context_db import UserModel
from src.utilerias.HasherPWD import HasherPWD
from ..libSQl.LibQLHttp import LibSQLHttp
from ..pillow.image import Image
from ..utilerias.AuthJWT import AuthJWT
from pyotp import TOTP, random_base32
from flask import Blueprint
from flask_restx import Api, Resource

api = Blueprint("api", __name__)
_api = Api(
    api,
    title="Cockroach Api",
    description="Api con acceso restringido"
)

@_api.route("/login_usuario/<string:pwd>/<string:nickname>/<string:code>")
class LoginUsuario(Resource):
    def get(self, pwd, nickname, code):
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

@_api.route("/login_usuario_query/<string:token>")
class LoginUsuarioQuery(Resource):
    def get(self, token):
        if AuthJWT.verify_token(token):
            return {
                "code": 200
            }
        else:
            return {
                "code": 401
            }

@_api.route("/image_filter/<string:bs64>/<string:filter>/<string:format_image>/<string:token>")
class ImageFilter_(Resource):
    def post(self, bs64, filter, format_image, token):
        if AuthJWT.verify_token(token):
            return {
                "code": 200,
                "message": Image.add_filter(bs64, filter, format_image)
            }
        else:
            return {
                "code": 400,
                "message": "Token no valido"
            }

@_api.route("/user/<string:pwd>/<string:nick>")
class User(Resource):
    def post(self, pwd: str, nick: str):
        try:
            secret = random_base32()
            totp_object = TOTP(secret)
            qr_text = totp_object.provisioning_uri(name=nick, issuer_name=f"CockroachApi{token_hex(10)}")

            user = UserModel()
            user.id = uuid4()
            user.nickname = nick
            user.password = HasherPWD.encode(pwd)
            user.t2f = secret
            user.save(force_insert=True)
            return {
                "code": 200,
                "qr_code": qr_text
            }
        except:
            return {
                "code": 401
            }

@_api.route("/libSQL/getAll/TipoArticulo/<string:token>")
class LibSQLGetAllTipoArticulo(Resource):
    def get(self, token):
        if AuthJWT.verify_token(token):
            return LibSQLHttp.excute("SELECT * FROM TipoArticulo", "execute", "GetAll")
        else:
            return {
                "code": 401
            }