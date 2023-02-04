import os
import glob

path = "./testdir"
files = glob.glob(path + '/*')

for f in files:
    os.rename(f, os.path.join(path, 'videoname_' + os.path.basename(f)))