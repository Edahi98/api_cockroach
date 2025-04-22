from flask_restx import Resource, Namespace, fields
from src.utilerias.AuthJWT import AuthJWT

api_login_query = Namespace("login_query", description="Apartado para consulta de login")

login_query = api_login_query.model("LoginQuery", {
    "request": fields.Boolean(description="Devuelve true o false")
})

@api_login_query.param("token", "Código A2F")
@api_login_query.route("/login_query/<string:token>")
class QueryLogin(Resource):
    @api_login_query.marshal_with(login_query)
    @api_login_query.response(401, "Se agoto la sesión")
    @api_login_query.response(200, "La sesión sige activa")
    @api_login_query.doc("get-query-login")
    def get(self, token):
        if AuthJWT.verify_token(token):
            return {
                "request": True
            }
        else:
            api_login_query.abort(401)