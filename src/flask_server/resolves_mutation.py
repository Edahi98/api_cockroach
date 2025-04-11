from ..pillow.image import Image

def resolve_addfilter(_, info, bs64, filter, format_image):
    return Image.add_filter(bs64, filter, format_image)