import os
import glob
from shutil import copyfile

path = "/Users/woosuk/Downloads/images"
folders = glob.glob(path + '/*')

exportPath = path

for folder in folders:
    files = glob.glob(folder + '/*')
    for f in files:
        copyfile(f, os.path.join(exportPath, f'0_{folder.split("/")[-1]}_{files.index(f)}.jpg'))