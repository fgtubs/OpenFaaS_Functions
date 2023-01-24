from function import load_image


def handle(req):
    buf = ""
    for line in str(req):
        buf = buf + line
    return load_image.download_and_resize_image(buf, 1280, 856, False)
