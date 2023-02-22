import os

images = os.listdir("./")

for s in images:
    os.rename(s, s.lower())
