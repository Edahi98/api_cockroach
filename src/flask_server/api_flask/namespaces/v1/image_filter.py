from flask_restx import Resource, Namespace, fields
from src.pillow.image import Image
from src.utilerias.AuthJWT import AuthJWT
from flask import request

api_image = Namespace("image", description="Apartado para colocar un filtro a una imagen")

image = api_image.model("Image",{
    "bs64": fields.String(required=True, description="Base64 de la imegen"),
    "filter": fields.String(required=True, description="Filtro"),
    "format_image": fields.String(required=True, description="Formato de imagen"),
    "token": fields.String(required=True, description="Token de acceso")
})

@api_image.route("/image_filter")
class ImageFilter_(Resource):
    @api_image.doc(body=image)
    @api_image.doc("get-filter")
    @api_image.response(400, "No se pudo hacer la acción")
    def post(self):
        datos = request.get_json()
        if AuthJWT.verify_token(datos["token"]):
            return {
                "code": 200,
                "message": Image.add_filter(datos["bs64"], datos["filter"], datos["format_image"])
            }
        else:
            api_image.abort(400)