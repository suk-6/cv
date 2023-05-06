import cv2
import os

rootDir = "/Volumes/Make"

videosDir = rootDir + "/videos"

videoFile_list = os.listdir(videosDir)

videoName_list = [name.split(".")[0] for name in videoFile_list]

print(videoName_list)

for name in videoName_list:

    video = cv2.VideoCapture(f"{videosDir}/" + name + ".mp4")

    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    print("video: ", name)
    print("length: ", length)
    print("width: ", width)
    print("height: ", height)
    print("fps: ", fps)

    count = 0

    while video.isOpened():
        if count >= int((length - (length % 10)) / 10):
            video.release()
            print("break")
            break

        ret, image = video.read()

        if int(video.get(1)) % 10 == 0:
            print("Saved frame number : " + str(int(video.get(1))))
            count_str = format(count, "06")
            # cv2.imwrite(f"{rootDir}/images/{name[4:]}_frame_{count_str}.png", image)
            cv2.imwrite(
                f"{rootDir}/images/{name[4:]}_frame_{count_str}.jpg",
                image,
                [cv2.IMWRITE_JPEG_QUALITY, 60],
            )

            count += 1
