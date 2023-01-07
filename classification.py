import os
import shutil
import random

num = random.sample(range(1001), 1001)

train = []
val = []
test = []

for i in range(700):
    num_str = format(num[i], '06')
    shutil.move('/home/dyserver/yolo-train/data/images/frame_%s.PNG' %
                num_str, '/home/dyserver/yolo-train/data/images/train')
    shutil.move('/home/dyserver/yolo-train/data/labels/frame_%s.txt' %
                num_str, '/home/dyserver/yolo-train/data/labels/train')
    train.append(num[i])

for i in range(200):
    i += 700
    num_str = format(num[i], '06')
    shutil.move('/home/dyserver/yolo-train/data/images/frame_%s.PNG' %
                num_str, '/home/dyserver/yolo-train/data/images/val')
    shutil.move('/home/dyserver/yolo-train/data/labels/frame_%s.txt' %
                num_str, '/home/dyserver/yolo-train/data/labels/val')
    val.append(num[i])

for i in range(101):
    i += 900
    num_str = format(num[i], '06')
    shutil.move('/home/dyserver/yolo-train/data/images/frame_%s.PNG' %
                num_str, '/home/dyserver/yolo-train/data/images/test')
    shutil.move('/home/dyserver/yolo-train/data/labels/frame_%s.txt' %
                num_str, '/home/dyserver/yolo-train/data/labels/test')
    test.append(num[i])


print(train)
print(val)
print(test)

print(len(train))
print(len(val))
print(len(test))
