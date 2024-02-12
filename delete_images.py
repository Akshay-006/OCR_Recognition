import os

for image in os.listdir():
    if image.endswith(".jpeg") or image.endswith(".png"):
        os.remove(image)
        print("Files removed")
else:
    print("No files removed")