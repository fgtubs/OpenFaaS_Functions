from function import load_model


def handle(req):
    buf = ""
    for line in str(req):
        buf = buf + line
    return load_model.download_and_resize_image_and_load(buf, 1280, 856, False)
