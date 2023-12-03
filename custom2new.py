# COCO 라벨과 Custom 라벨을 매칭시켜주는 코드

new_labels = {
    0: "person",
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    4: "airplane",
    5: "bus",
    6: "train",
    7: "truck",
    8: "boat",
    9: "traffic light",
    10: "fire hydrant",
    11: "stop sign",
    12: "parking meter",
    13: "bench",
    14: "bird",
    15: "cat",
    16: "dog",
    17: "horse",
    18: "sheep",
    19: "cow",
    20: "elephant",
    21: "bear",
    22: "zebra",
    23: "giraffe",
    24: "backpack",
    25: "umbrella",
    26: "handbag",
    27: "tie",
    28: "suitcase",
    29: "frisbee",
    30: "skis",
    31: "snowboard",
    32: "sports ball",
    33: "kite",
    34: "baseball bat",
    35: "baseball glove",
    36: "skateboard",
    37: "surfboard",
    38: "tennis racket",
    39: "bottle",
    40: "wine glass",
    41: "cup",
    42: "fork",
    43: "knife",
    44: "spoon",
    45: "bowl",
    46: "banana",
    47: "apple",
    48: "sandwich",
    49: "orange",
    50: "broccoli",
    51: "carrot",
    52: "hot dog",
    53: "pizza",
    54: "donut",
    55: "cake",
    56: "chair",
    57: "couch",
    58: "potted plant",
    59: "bed",
    60: "dining table",
    61: "toilet",
    62: "tv",
    63: "laptop",
    64: "mouse",
    65: "remote",
    66: "keyboard",
    67: "cell phone",
    68: "microwave",
    69: "oven",
    70: "toaster",
    71: "sink",
    72: "refrigerator",
    73: "book",
    74: "clock",
    75: "vase",
    76: "scissors",
    77: "teddy bear",
    78: "hair drier",
    79: "toothbrush",
    80: "tree",
    81: "pole",
    82: "fence",
    83: "utility_pole",
    84: "bollard",
    85: "flower_bed",
    86: "bus_stop",
    87: "traffic_cone",
    88: "kickboard",
    89: "streetlamp",
    90: "telephone_booth",
    91: "trash",
    92: "fire_plug",
    93: "plant",
    94: "sign_board",
    95: "corner",
    96: "opened_door",
    97: "mailbox",
    98: "banner",
}

cus2new = {
    0: 80,
    1: 2,
    2: 0,
    3: 81,
    4: 82,
    5: 83,
    6: 84,
    7: 1,
    8: 3,
    9: 85,
    10: 16,
    11: 86,
    12: 87,
    13: 7,
    14: 13,
    15: 5,
    16: 88,
    17: 89,
    18: 90,
    19: 91,
    20: 92,
    21: 93,
    22: 94,
    23: 10,
    24: 95,
    25: 96,
    26: 97,
    27: 98,
}

import os

# train_list = os.listdir("./labels/train")
# val_list = os.listdir("./labels/val")
# test_list = os.listdir("./labels/test")
root = "/Users/woosuk/data/4000/dataset"
labelPath = os.path.join(root, "labels")
newPath = os.path.join(root, "new")

os.makedirs(newPath, exist_ok=True)

labels = [file for file in os.listdir(labelPath) if file.endswith(".txt")]


# tmp = []

# for listname in train_list, val_list, test_list:
#     for filename in listname:
#         if listname == train_list:
#             target_class = "train"
#         if listname == val_list:
#             target_class = "val"
#         if listname == test_list:
#             target_class = "test"
# for listname in lists:
#     labels = os.listdir("./labels/{l}".format(l=listname))
for filename in labels:
    new_lines = ""
    path = os.path.join(labelPath, filename)
    new_path = os.path.join(newPath, filename)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            new_line = ""
            idx = line.split()[0]
            idx = cus2new[int(idx)]
            new_line += str(idx)
            new_line += " "
            new_line += line.split()[1]
            new_line += " "
            new_line += line.split()[2]
            new_line += " "
            new_line += line.split()[3]
            new_line += " "
            new_line += line.split()[4]
            new_line += "\n"
            new_lines += new_line
        # print(new_lines)
    with open(new_path, "w") as f:
        f.write(new_lines)
