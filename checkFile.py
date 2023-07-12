# 이미지와 라벨링 파일 개수 확인

import os

rootDir = "/Volumes/Make/230506-files"

imagesDir = f"{rootDir}/images"
labelsDir = f"{rootDir}/labels"

imagesList = os.listdir(imagesDir)
labelsList = os.listdir(labelsDir)

imagesName = [s[:-4] for s in imagesList]
labelsName = [s[:-4] for s in labelsList]

dif = set(imagesName).difference(set(labelsName))

for s in dif:
    file = f"{imagesDir}/{s}.jpg"
    print(file)
    if os.path.isfile(file):
        os.remove(file)

print(len(dif))
