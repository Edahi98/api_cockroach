from flask import request
from flask_restx import Namespace, Resource, fields
from pyotp import TOTP
from src.flask_server.context_db import UserModel
from src.utilerias.AuthJWT import AuthJWT
from src.utilerias.HasherPWD import HasherPWD

api_login = Namespace("login", description="Apartado para login")

user = api_login.model("Login", {
    "pwd": fields.String(required=True, description="Contraseña"),
    "nick": fields.String(required=True, description="Nombre"),
    "code": fields.String(required=True, description="Código A2F")
})

@api_login.route("/login_usuario")
class Login(Resource):
    @api_login.doc(body=user)
    @api_login.doc("get-usuario")
    @api_login.response(400, "Usuario no encontrado")
    def get(self):
        try:
            datos = request.get_json()
            resultado = UserModel.select().where(UserModel.nickname == datos["nick"]).get()
            if HasherPWD.check(resultado.password, datos["pwd"]):
                totp_object = TOTP(resultado.t2f)
                if totp_object.verify(datos["code"]):
                    return {
                        "token": AuthJWT.generate_token(datos["nick"]),
                        "code": 200
                    }
                else:
                    api_login.abort(400)
        except Exception as e:
            api_login.abort(400)