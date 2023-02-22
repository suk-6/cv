import os

images_dir = "/Volumes/Make/images"
labels_dir = "/Volumes/Make/230222-train/labels"

image_list = os.listdir(images_dir)
label_list = os.listdir(labels_dir)

image_list_1 = []
label_list_1 = []

for s in image_list:
    image_list_1.append(s[:-4])

for s in label_list:
    file = os.listdir(labels_dir + "/" + s)
    for t in file:
        label_list_1.append(t[:-4])

image_list_2 = set(image_list_1)
label_list_2 = set(label_list_1)

dif = image_list_2.difference(label_list_2)

for s in dif:
    file = images_dir + "/" + s + ".png"
    print(file)
    if os.path.isfile(file):
        os.remove(file)

print(len(dif))
