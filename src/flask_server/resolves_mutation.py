from .context_db import UserModel
from ..pillow.image import Image
from ..utilerias.AuthJWT import AuthJWT
from ..utilerias.HasherPWD import HasherPWD
from uuid import uuid4


def resolve_addfilter(_, info, bs64, filter, format_image, token):
    if AuthJWT.verify_token(token):
        return Image.add_filter(bs64, filter, format_image)
    else:
        return "Token no valido"


def resolve_adduser(_, info, pwd, nick):
    try:
        user = UserModel()
        user.id = uuid4()
        user.nickname = nick
        user.password = HasherPWD.encode(pwd)
        user.save(force_insert=True)
        return "Se registro"
    except:
        return "No se registro"