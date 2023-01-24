# Preprocess and download image

faas deploy --image anyfin/download-and-resize:v0.0.1 --name download-and-resize --fprocess "python index.py"
