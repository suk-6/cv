import os
import shutil

rootDir = "/Volumes/Make/230506-files/labels"

labelDir_list = [
    name for name in os.listdir(rootDir) if name != ".DS_Store" and name != "export"
]

labelName_list = [name[9:13] for name in labelDir_list]

print(labelName_list)

count = 0

for f in range(len(labelName_list)):
    pathOrigin = f"{rootDir}/{labelDir_list[f]}/obj_train_data"
    for filename in os.listdir(pathOrigin):
        path = os.path.join(pathOrigin, filename)
        if filename.endswith(".txt") and os.path.getsize(path) > 0:
            pathExport = os.path.join(
                f"{rootDir}/export", labelName_list[f] + "_" + filename
            )
            shutil.copy(path, pathExport)
            count += 1

print(count)
