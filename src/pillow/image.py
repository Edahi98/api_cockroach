from .filters_const import FILTERS
from ..utilerias.bs64Image import Bs64Image

class Image:
    @staticmethod
    def add_filter(bs64: str, fiter: str, format_image: str):
        for k, v in FILTERS.items():
            if fiter.upper() == k:
                return Bs64Image.encode(Bs64Image.decode(bs64).filter(v),format_image)
        return "No se pudo aplicar el filtro"