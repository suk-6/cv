import os
import os.path as osp


def convertPngToJpg(inputFolder, outputFolder):
    if not osp.exists(outputFolder):
        os.makedirs(outputFolder)

    for filename in os.listdir(inputFolder):
        if filename.lower().endswith(".png"):
            path = osp.join(inputFolder, filename)
            outputPath = f"{outputFolder}/{filename.split('.')[0]}.jpg"
            os.system(f"ffmpeg -i {path} -preset ultrafast {outputPath}")

            print(f"Converted {filename} and saved to {outputPath}")


inputFolder = "images"
outputFolder = "converted_images"

convertPngToJpg(inputFolder, outputFolder)
