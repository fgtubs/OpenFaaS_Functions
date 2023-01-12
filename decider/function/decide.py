def preprocess_image(body):
    img_path = ""
    if body.startswith("https://") or body.startswith("http://"):
        print("Case 1")
        return "Case 1"
    else:
        print("Case 2")
        return "Case 2"

if __name__ == "__main__":
    preprocess_image("https://www.pixelstalk.net/wp-content/uploads/2016/03/Animal-wallpapers-HD-desktop.jpg")
