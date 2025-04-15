from .context_db import UserModel
from ..pillow.image import Image
from ..utilerias.AuthJWT import AuthJWT
from ..utilerias.HasherPWD import HasherPWD
from uuid import uuid4
from secrets import token_hex
from pyotp import random_base32, TOTP


def resolve_addfilter(_, info, bs64, filter, format_image, token):
    if AuthJWT.verify_token(token):
        return Image.add_filter(bs64, filter, format_image)
    else:
        return "Token no valido"


def resolve_adduser(_, info, pwd, nick):
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
        return qr_text
    except:
        return "No se registro"