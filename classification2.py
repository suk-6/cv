# 이미지와 라벨링 파일을 비율에 맞게 분류 (개선버전)

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

if not os.path.exists(f"{rootDir}/images/train"):
    os.mkdir(f"{rootDir}/images/train")
if not os.path.exists(f"{rootDir}/images/val"):
    os.mkdir(f"{rootDir}/images/val")
if not os.path.exists(f"{rootDir}/images/test"):
    os.mkdir(f"{rootDir}/images/test")

if not os.path.exists(f"{rootDir}/labels/train"):
    os.mkdir(f"{rootDir}/labels/train")
if not os.path.exists(f"{rootDir}/labels/val"):
    os.mkdir(f"{rootDir}/labels/val")
if not os.path.exists(f"{rootDir}/labels/test"):
    os.mkdir(f"{rootDir}/labels/test")


def move(file, dir):
    shutil.move(
        f"{rootDir}/images/{file}",
        f"{rootDir}/images/{dir}",
    )
    shutil.move(
        f"{rootDir}/labels/{file.split('.')[0]}.txt",
        f"{rootDir}/labels/{dir}",
    )


for i in range(trainCount):
    FileName = imageList[num[i]]
    move(imageList[num[i]], "train")
    train.append(FileName)

for i in range(valCount):
    i += trainCount
    FileName = imageList[num[i]]
    move(imageList[num[i]], "train")
    val.append(FileName)

for i in range(testCount):
    i += trainCount + valCount
    FileName = imageList[num[i]]
    move(imageList[num[i]], "train")
    test.append(FileName)


print(train)
print(val)
print(test)

print(len(train))
print(len(val))
print(len(test))
