from os import environ
from requests import post
from re import search
from typing import Literal

class LibSQLHttp:
    HEADERS = headers={
                "Authorization": f"Bearer {str(environ.get('TURSO_TOKEN'))}",
                "Content-Type": "application/json",
            }

    getQuerySQLSinArgs = lambda sql, type_exc: {"type": type_exc, "stmt": {"sql": sql}}
    getQuerySQLConArgs = lambda sql, type_exc, args: {"type": type_exc, "stmt": {"sql": sql, "args": args}}

    getAll = lambda datos: [[v for jj in x for k, v in jj.items() if search("value", k)] for x in datos.json()["results"][0]["response"]["result"]["rows"]]

    @staticmethod
    def excute(sql, type_execute, type_result: Literal["GetAll"], args=None):
        datos = post(environ.get("TURSO_URL"), headers=LibSQLHttp.HEADERS, json={
            "requests": [
                LibSQLHttp.getQuerySQLSinArgs(sql, type_execute) if args is None else LibSQLHttp.getQuerySQLConArgs(sql, type_execute, args),
                {"type": "close"}
            ]
        },
                     )
        match type_result:
            case "GetAll": return LibSQLHttp.getAll(datos)
            case _: return datos.json()