from secrets import token_hex
from uuid import uuid4
from flask_restx import Resource, Namespace, fields
from pyotp import random_base32, TOTP
from src.flask_server.context_db import UserModel
from src.utilerias.HasherPWD import HasherPWD


api_user = Namespace("user", description="Apartado para usuario")
user = api_user.model("User", {
    "nick": fields.String(required=True, description="Nombre de usuario"),
    "pwd": fields.String(required=True, description="Contraseña de usuario")
})

@api_user.route("/user")
class User(Resource):
    @api_user.doc(body=user)
    @api_user.response(401, description="No se pudo hacer el registro")
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
            api_user.abort(401)