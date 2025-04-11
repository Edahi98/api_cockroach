from base64 import b64decode, b64encode
from io import BytesIO
from PIL import Image
from PIL.ImageFile import ImageFile


class Bs64Image:
    @staticmethod
    def decode(bs: str) -> ImageFile:
        return Image.open(BytesIO(b64decode(bs)))

    @staticmethod
    def encode(img: ImageFile, format_image: str) -> str:
        buffer = BytesIO()
        img.save(buffer, format_image)
        return b64encode(buffer.getvalue()).decode("utf-8")


