from flask import Blueprint
from flask_restx import Api
from .namespaces.v1.login import api_login
from .namespaces.v1.user import api_user
from .namespaces.v1.query_login import api_login_query
from .namespaces.v1.libsql_get_all import api_libsql_get_all_v1
from .namespaces.v1.image_filter import api_image
api = Blueprint("api", __name__, url_prefix="/api")
apis = Api(
    api,
    title="Cockroach Api",
    description="Api con acceso restringido"
)
apis.add_namespace(api_user)
apis.add_namespace(api_login)
apis.add_namespace(api_login_query)
apis.add_namespace(api_libsql_get_all_v1)
apis.add_namespace(api_image)