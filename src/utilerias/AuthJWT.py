from jwt import encode, decode, InvalidSignatureError
from datetime import datetime, timedelta
from pytz import timezone
from os import environ
from src.flask_server.context_db import UserModel


class AuthJWT:
   TZ = timezone("America/Mexico_City")
   KEY = environ.get("SECRET")

   @staticmethod
   def generate_token(nickname):
       INIF = datetime.now(tz=AuthJWT.TZ).strftime("%Y-%m-%dT%H:%M:%S%z")
       resultado = UserModel.select().where(UserModel.nickname == nickname).get()
       finf = (datetime.now(tz=AuthJWT.TZ)+timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S%z")
       payload = {
           "iusr": str(resultado.id),
           "usr": nickname,
           "inif": INIF,
           "finf": finf
       }
       return encode(payload, key=AuthJWT.KEY, algorithm="HS256")

   @staticmethod
   def verify_token(token):
        try:
            pyload = decode(token, key=AuthJWT.KEY, algorithms=["HS256"])
            finf = datetime.strptime(pyload["finf"], "%Y-%m-%dT%H:%M:%S%z")
            fecha_actual = datetime.now(tz=AuthJWT.TZ)
            if fecha_actual < finf:
                usr = pyload["usr"]
                iusr = pyload["iusr"]
                resultado = UserModel.select().where(UserModel.nickname == usr).get()
                if str(resultado.id) == str(iusr):
                    return True
                else:
                    return False
            else:
                return False
        except InvalidSignatureError as e:
            return e



