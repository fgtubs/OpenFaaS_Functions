from function import preprocess


def handle(req):
    buf = ""
    for line in str(req):
        buf = buf + line
    return preprocess.download_and_resize_image(buf, 1280, 856, False)
