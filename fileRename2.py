import os
from glob import glob
from shutil import move

path = "/Volumes/T7/230728/export/images/GX010158"

files = glob(path + '/*')

for file in files:
    move(file, os.path.join(path, f"frame{format(int(os.path.basename(file)[-10:-4])+1, '06')}.jpg"))