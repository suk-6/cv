import os
import glob
import csv
import matplotlib.pyplot as plt

path = "/Volumes/T7/230728/labels"

labelFiles = glob.glob(path + '/*')

labels = ["tree", "car", "person", "pole", "fence", "utility_pole", "bollard", "bicycle", "motorcycle", "flower_bed", "dog", "bus_stop", "traffic_cone", "truck", "bench", "bus", "kickboard", "streetlamp", "telephone_booth", "trash", "fire_plug", "plant", "sign_board", "fire_hydrant", "corner", "opened_door", "mailbox", "unknown", "banner"]
readLabels = []

def saveCSV(countLabels):
    with open("label_counts.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Total Images", len(labelFiles)])
        writer.writerow(["Total Instances", len(readLabels)])
        for label, count in countLabels.items():
            writer.writerow([label, count])
            print(f"{label}: {count}")

def readLabelFiles():
    for labelFile in labelFiles:
        with open(labelFile, "r") as f:
            lines = f.readlines()
            for line in lines:
                label = labels[int(line.split()[0])]
                readLabels.append(label)
                print(label)
    countLabels = {label: readLabels.count(label) for label in labels}
    printLabelCounts()
    saveCSV(countLabels)
    saveGraph(countLabels)

def printLabelCounts():
    for label in labels:
        print(f"{label}: {readLabels.count(label)}")

    print(f"총 인스턴스 개수: {len(readLabels)}")

def saveGraph(countLabels):
    plt.bar(countLabels.keys(), countLabels.values())
    plt.xlabel('Label')
    plt.ylabel('Instance Count')
    plt.title('Label Distribution')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # plt.ylim(0, 1000)

    plt.savefig("label_distribution.png")

readLabelFiles()
