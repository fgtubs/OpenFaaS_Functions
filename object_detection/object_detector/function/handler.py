from function import load_model


def handle(req):
    buf = ""
    for line in str(req):
        buf = buf + line
    image_path = load_model.download_and_resize_image_and_load(buf, 1280, 856, False)
    return detector.run_detector(image_path)
