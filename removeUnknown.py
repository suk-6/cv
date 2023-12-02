import os
import sys
from glob import glob


class app:
    def __init__(self, labelsPath):
        self.labelsPath = labelsPath

        self.run()

    def read(self, path):
        with open(path, "r") as f:
            return f.read()

    def write(self, path, data):
        with open(path, "w") as f:
            f.write(data)

    def processing(self, path):
        objects = self.read(path).split("\n")

        data = ""
        for obj in objects:
            if obj == "":
                continue

            obj = obj.split(" ")

            if obj[0] == "27":
                continue

            if obj[0] == "28":
                obj[0] = "27"

            data += " ".join(obj) + "\n"

        self.write(path, data)

    def run(self):
        if type(self.labelsPath) == list:
            for path in self.labelsPath:
                self.processing(path)
            return

        self.processing(self.labelsPath)


if __name__ == "__main__":
    path = sys.argv[1]

    if os.path.isdir(path):
        path = glob(os.path.join(path, "*.txt"))

    app(path)
