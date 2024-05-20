# 이미지와 라벨링 파일을 비율에 맞게 분류 (YOLO버전)

import os
import shutil
import math
import random

rootDir = "."

imageDir = f"{rootDir}/images"

imageList = [
    file
    for file in os.listdir(imageDir)
    if file.lower().endswith(".jpg")
    or file.lower().endswith(".png")
    or file.lower().endswith(".jpeg")
]

imageCount = len(imageList)

num = random.sample(range(imageCount), imageCount)

trainCount = math.floor(imageCount * 0.7)
valCount = math.floor(imageCount * 0.2)
testCount = imageCount - trainCount - valCount

train = []
val = []
test = []

if not os.path.exists(f"{rootDir}/train"):
    os.mkdir(f"{rootDir}/train")
if not os.path.exists(f"{rootDir}/val"):
    os.mkdir(f"{rootDir}/val")
if not os.path.exists(f"{rootDir}/test"):
    os.mkdir(f"{rootDir}/test")

if not os.path.exists(f"{rootDir}/train/images"):
    os.mkdir(f"{rootDir}/train/images")
if not os.path.exists(f"{rootDir}/val/images"):
    os.mkdir(f"{rootDir}/val/images")
if not os.path.exists(f"{rootDir}/test/images"):
    os.mkdir(f"{rootDir}/test/images")

if not os.path.exists(f"{rootDir}/train/labels"):
    os.mkdir(f"{rootDir}/train/labels")
if not os.path.exists(f"{rootDir}/val/labels"):
    os.mkdir(f"{rootDir}/val/labels")
if not os.path.exists(f"{rootDir}/test/labels"):
    os.mkdir(f"{rootDir}/test/labels")


def move(file, dir):
    shutil.move(
        f"{rootDir}/images/{file}",
        f"{rootDir}/{dir}/images",
    )
    shutil.move(
        f"{rootDir}/labels/{file.split('.')[0]}.txt",
        f"{rootDir}/{dir}/labels",
    )


for i in range(trainCount):
    FileName = imageList[num[i]]
    move(imageList[num[i]], "train")
    train.append(FileName)

for i in range(valCount):
    i += trainCount
    FileName = imageList[num[i]]
    move(imageList[num[i]], "val")
    val.append(FileName)

for i in range(testCount):
    i += trainCount + valCount
    FileName = imageList[num[i]]
    move(imageList[num[i]], "test")
    test.append(FileName)


print(train)
print(val)
print(test)

print(len(train))
print(len(val))
print(len(test))
