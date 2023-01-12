from function import decide


def handle(req):
    buf = ""
    for line in str(req):
        buf = buf + line
    return decide.preprocess_image(buf)
