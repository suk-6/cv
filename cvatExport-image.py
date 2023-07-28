import os
from glob import glob
from shutil import move

taskName = "task_sillim_3-2023_07_07_19_38_41-yolo 1.1"

path = f"/Volumes/T7/230728/export/export-origin/{taskName}/obj_train_data"

files = glob(path + '/*')

labels = [f for f in files if f.endswith('.txt')]
images = [f for f in files if f.endswith('.PNG')]

if not os.path.exists(os.path.join(path, 'images')):
    os.makedirs(os.path.join(path, 'images'))

if not os.path.exists(os.path.join(path, 'labels')):
    os.makedirs(os.path.join(path, 'labels'))

for label in labels:
    move(label, os.path.join(path, 'labels', os.path.basename(label)))

for image in images:
    move(image, os.path.join(path, 'images', os.path.basename(image)))