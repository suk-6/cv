# 이미지와 라벨링 파일을 비율에 맞게 분류 (개선버전)

import os
import shutil
import math
import random

rootDir = "/home/woosuk/230506-files"

imageDir = f"{rootDir}/images"

imageList = os.listdir(imageDir)

targetList = [file[:-4] for file in imageList if file.endswith(".jpg")]

imageCount = len(targetList)

num = random.sample(range(imageCount), imageCount)

trainCount = math.floor(imageCount * 0.7)
valCount = math.floor(imageCount * 0.2)
testCount = math.floor(imageCount * 0.1)

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

for i in range(trainCount):
    FileName = targetList[num[i]]
    shutil.move(
        f"{rootDir}/images/{FileName}.jpg",
        f"{rootDir}/images/train",
    )
    shutil.move(
        f"{rootDir}/labels/{FileName}.txt",
        f"{rootDir}/labels/train",
    )
    train.append(FileName)

for i in range(valCount):
    i += trainCount
    FileName = targetList[num[i]]
    shutil.move(
        f"{rootDir}/images/{FileName}.jpg",
        f"{rootDir}/images/val",
    )
    shutil.move(
        f"{rootDir}/labels/{FileName}.txt",
        f"{rootDir}/labels/val",
    )
    val.append(FileName)

for i in range(testCount):
    i += trainCount + valCount
    FileName = targetList[num[i]]
    shutil.move(
        f"{rootDir}/images/{FileName}.jpg",
        f"{rootDir}/images/test",
    )
    shutil.move(
        f"{rootDir}/labels/{FileName}.txt",
        f"{rootDir}/labels/test",
    )
    test.append(FileName)


print(train)
print(val)
print(test)

print(len(train))
print(len(val))
print(len(test))
