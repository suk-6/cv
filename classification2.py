import os
import shutil
import math
import random

root_dir = "/home/woosuk/230222-train/data"

images_dir = "{root_dir}/images".format(root_dir=root_dir)

image_list = os.listdir(images_dir)

image_list_1 = [file for file in image_list if file.endswith(".png")]

target_list = []

for s in image_list_1:
    target_list.append(s[:-4])

image_count = len(target_list)

num = random.sample(range(image_count), image_count)

train_count = math.floor(image_count * 0.7)
val_count = math.floor(image_count * 0.2)
test_count = math.floor(image_count * 0.1)

train = []
val = []
test = []

for i in range(train_count):
    FileName = target_list[num[i]]
    shutil.move(
        "{root_dir}/images/{FileName}.png".format(root_dir=root_dir, FileName=FileName),
        "{root_dir}/images/train".format(root_dir=root_dir),
    )
    shutil.move(
        "{root_dir}/labels/{FileName}.txt".format(root_dir=root_dir, FileName=FileName),
        "{root_dir}/labels/train".format(root_dir=root_dir),
    )
    train.append(FileName)

for i in range(val_count):
    i += train_count
    FileName = target_list[num[i]]
    shutil.move(
        "{root_dir}/images/{FileName}.png".format(root_dir=root_dir, FileName=FileName),
        "{root_dir}/images/val".format(root_dir=root_dir),
    )
    shutil.move(
        "{root_dir}/labels/{FileName}.txt".format(root_dir=root_dir, FileName=FileName),
        "{root_dir}/labels/val".format(root_dir=root_dir),
    )
    val.append(FileName)

for i in range(test_count):
    i += train_count + val_count
    FileName = target_list[num[i]]
    shutil.move(
        "{root_dir}/images/{FileName}.png".format(root_dir=root_dir, FileName=FileName),
        "{root_dir}/images/test".format(root_dir=root_dir),
    )
    shutil.move(
        "{root_dir}/labels/{FileName}.txt".format(root_dir=root_dir, FileName=FileName),
        "{root_dir}/labels/test".format(root_dir=root_dir),
    )
    test.append(FileName)


print(train)
print(val)
print(test)

print(len(train))
print(len(val))
print(len(test))
