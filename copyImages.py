import os
import glob
from shutil import copyfile

path = "/Volumes/T7/230728/export/images"
folders = glob.glob(path + '/*')

exportPath = "/Volumes/T7/230728/images"

for folder in folders:
    files = glob.glob(folder + '/*')
    for f in files:
        copyfile(f, os.path.join(exportPath, f'{folder.split("/")[-1]}_' + os.path.basename(f)))