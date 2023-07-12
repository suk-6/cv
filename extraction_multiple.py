# 여러개의 영상을 한번에 프레임 단위로 추출하는 코드

import cv2
import os

rootDir = "/Volumes/Make"

videosDir = rootDir + "/videos"

videoName_list = [name.split(".")[0] for name in os.listdir(videosDir)]

print(videoName_list)

for name in videoName_list:

    video = cv2.VideoCapture(f"{videosDir}/" + name + ".mp4")

    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    frame = 30 #프레임 단위

    print("video: ", name)
    print("length: ", length)
    print("width: ", width)
    print("height: ", height)
    print("fps: ", fps)

    count = 0

    while video.isOpened():
        if count >= int((length - (length % frame)) / frame):
            video.release()
            print("break")
            break

        ret, image = video.read()

        if int(video.get(1)) % frame == 0:
            print("Saved frame number : " + str(int(video.get(1))))
            count_str = format(count, "06")
            outputDir = f"{rootDir}/images/{name}"
            if not os.path.exists(outputDir):
                os.makedirs(outputDir)
            # cv2.imwrite(f"{rootDir}/images/{name[4:]}_frame_{count_str}.png", image)
            cv2.imwrite(
                f"{outputDir}/frame_{count_str}.jpg",
                image,
                [cv2.IMWRITE_JPEG_QUALITY, 60],
            )

            count += 1
