import os

images_dir = "/home/woosuk/230205-train/images"
labels_dir = "/home/woosuk/230205-train/labels"

image_list = os.listdir(images_dir)
label_list = os.listdir(labels_dir)


image_list_1 = []
label_list_1 = []

for s in image_list:
    image_list_1.append(s[:-4])

for s in label_list:
    label_list_1.append(s[:-4])

image_list_2 = set(image_list_1)
label_list_2 = set(label_list_1)

print(image_list_2.difference(label_list_2))
