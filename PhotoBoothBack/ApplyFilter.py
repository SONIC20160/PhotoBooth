from PIL import Image, ImageEnhance

def apply_filter(image , filter):
    if filter:
        return image.convert("L")   #Black and white
    else:
        image = image.convert("RGB")
        image = ImageEnhance.Color(image).enhance(0.4)      # desaturate
        image = ImageEnhance.Contrast(image).enhance(1.2)   # contrast
        r, g, b = image.split()
        r = r.point(lambda i: min(255, i + 30))
        b = b.point(lambda i: max(0, i - 20))
        return Image.merge("RGB", (r, g, b))