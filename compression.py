from PIL import Image
import os


def compressImages(inputFolder, outputFolder, quality=60):
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    for filename in os.listdir(inputFolder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            path = os.path.join(inputFolder, filename)
            img = Image.open(path)

            img = img.convert("RGB")

            output_path = os.path.join(outputFolder, filename)
            img.save(output_path, quality=quality, optimize=True)

            print(f"Compressed {filename} and saved to {output_path}")


inputFolder = "images"
outputFolder = "compressed_images"

compressImages(inputFolder, outputFolder)
