from flask_restx import Resource, Namespace
from src.libSQl.LibQLHttp import LibSQLHttp
from src.utilerias.AuthJWT import AuthJWT

api_libsql_get_all_v1 = Namespace("libsql-get-all", description="Apartado para colocar un filtro a una imagen")

@api_libsql_get_all_v1.param("token", "Token de sesión")
@api_libsql_get_all_v1.route("/getAll/TipoArticulo/<string:token>")
class LibSQLGetAllTipoArticulo(Resource):
    @api_libsql_get_all_v1.doc("get-tipos-articulos")
    @api_libsql_get_all_v1.response(401, "No se pudieron obtener los tipos de articulos")
    def get(self, token):
        if AuthJWT.verify_token(token):
            return LibSQLHttp.excute("SELECT * FROM TipoArticulo", "execute", "GetAll")
        else:
            api_libsql_get_all_v1.abort(401)