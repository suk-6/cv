import os
import os.path as osp
import shutil
import random


class app:
    def __init__(self, root, length, count):
        self.root = root
        self.length = length
        self.count = count

        self.images = os.listdir(osp.join(self.root, "images"))
        self.images = random.sample(self.images, len(self.images))

        self.run()

    def makeDir(self, idx):
        path = osp.join(self.root, "exports", str(idx))
        os.makedirs(path, exist_ok=True)

    def run(self):
        for i in range(self.count):
            self.makeDir(i)
            for _ in range(self.length):
                image = self.images.pop()
                label = osp.splitext(image)[0] + ".txt"
                shutil.copy(
                    osp.join(self.root, "images", image),
                    osp.join(self.root, "exports", str(i), image),
                )
                shutil.copy(
                    osp.join(self.root, "labels", label),
                    osp.join(self.root, "exports", str(i), label),
                )


if __name__ == "__main__":
    root = "/Users/woosuk/data/4000/dataset"
    length = 1000
    count = 3

    app(root, length, count)
