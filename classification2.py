import os
import shutil
import random

num = random.sample(range(2636), 2636)

images_dir = "/home/woosuk/230205-train/data/images"

image_list = os.listdir(images_dir)

image_list_1 = [file for file in image_list if file.endswith(".PNG")]

target_list = []

for s in image_list_1:
    target_list.append(s[:-4])

train = []
val = []
test = []

for i in range(1900):
    FileName = target_list[num[i]]
    shutil.move(
        "/home/woosuk/230205-train/data/images/%s.PNG" % FileName,
        "/home/woosuk/230205-train/data/images/train",
    )
    shutil.move(
        "/home/woosuk/230205-train/data/labels/%s.txt" % FileName,
        "/home/woosuk/230205-train/data/labels/train",
    )
    train.append(FileName)

for i in range(500):
    i += 1900
    FileName = target_list[num[i]]
    shutil.move(
        "/home/woosuk/230205-train/data/images/%s.PNG" % FileName,
        "/home/woosuk/230205-train/data/images/val",
    )
    shutil.move(
        "/home/woosuk/230205-train/data/labels/%s.txt" % FileName,
        "/home/woosuk/230205-train/data/labels/val",
    )
    val.append(FileName)

for i in range(236):
    i += 2400
    FileName = target_list[num[i]]
    shutil.move(
        "/home/woosuk/230205-train/data/images/%s.PNG" % FileName,
        "/home/woosuk/230205-train/data/images/test",
    )
    shutil.move(
        "/home/woosuk/230205-train/data/labels/%s.txt" % FileName,
        "/home/woosuk/230205-train/data/labels/test",
    )
    test.append(FileName)


print(train)
print(val)
print(test)

print(len(train))
print(len(val))
print(len(test))
