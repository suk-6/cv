import os
import os.path as osp
import shutil
import glob
import xml.etree.ElementTree as ET


def convert(imageSize, bbox):
    xtl, ytl, xbr, ybr = bbox
    image_width, image_height = imageSize

    yolo_x = round(((xtl + xbr) / 2) / image_width, 6)
    yolo_y = round(((ytl + ybr) / 2) / image_height, 6)
    yolo_w = round((xbr - xtl) / image_width, 6)
    yolo_h = round((ybr - ytl) / image_height, 6)

    return yolo_x, yolo_y, yolo_w, yolo_h


def convertXML(inputPath, outputPath):
    if not osp.exists(outputPath):
        os.makedirs(outputPath)
    if not osp.exists(osp.join(outputPath, "images")):
        os.makedirs(osp.join(outputPath, "images"))
    if not osp.exists(osp.join(outputPath, "labels")):
        os.makedirs(osp.join(outputPath, "labels"))

    in_file = open(glob.glob(inputPath + "/*.xml")[0])
    tree = ET.parse(in_file)
    root = tree.getroot()
    labels = sorted(
        [
            label.find("./name").text
            for label in root.find("./meta/task/labels").findall("label")
        ]
    )

    with open(osp.join(outputPath, "classes.txt"), "w") as f:
        f.write("\n".join(labels))

    for image in root.iter("image"):
        imageFile = image.attrib["name"]
        size = (int(image.attrib["width"]), int(image.attrib["height"]))
        shutil.copy(
            osp.join(inputPath, imageFile),
            osp.join(outputPath, "images", imageFile),
        )
        for box in image.iter("box"):
            label = labels.index(box.attrib["label"])
            x, y, w, h = convert(
                size,
                (
                    float(box.attrib["xtl"]),
                    float(box.attrib["ytl"]),
                    float(box.attrib["xbr"]),
                    float(box.attrib["ybr"]),
                ),
            )
            with open(
                osp.join(
                    outputPath,
                    "labels",
                    imageFile.replace(".png", ".txt").replace(".jpg", ".txt"),
                ),
                "a",
            ) as f:
                f.write(f"{label} {x} {y} {w} {h}\n")


if __name__ == "__main__":
    datasPath = osp.join(os.getcwd(), "datas")
    inputPaths = os.listdir(datasPath)
    for inputPath in inputPaths:
        if osp.isdir(osp.join(datasPath, inputPath)):
            convertXML(
                osp.join(datasPath, inputPath),
                osp.join(os.getcwd(), "export"),
            )
