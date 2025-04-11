from PIL import ImageFilter

FILTERS = {
    "BLUR": ImageFilter.BLUR,
    "CONTOUR": ImageFilter.CONTOUR,
    "SMOOTH": ImageFilter.SMOOTH,
    "FIND_EDGES": ImageFilter.FIND_EDGES,
    "EMBOSS": ImageFilter.EMBOSS,
    "DETAIL": ImageFilter.DETAIL,
    "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
    "BOX_BLUR_50": ImageFilter.BoxBlur(50),
    "BOX_BLUR_60": ImageFilter.BoxBlur(60),
    "BOX_BLUR_70": ImageFilter.BoxBlur(70),
    "BOX_BLUR_80": ImageFilter.BoxBlur(80),
    "BOX_BLUR_90": ImageFilter.BoxBlur(90),
    "BOX_BLUR_100": ImageFilter.BoxBlur(100)
}
