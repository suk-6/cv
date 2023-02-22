import cv2
import os

root_dir = "/Volumes/Make"

videos_dir = root_dir + "/MP4"

video_list = os.listdir(videos_dir)

video_name = [name.split(".")[0] for name in video_list]

print(video_name)

for name in video_name:

    video = cv2.VideoCapture(root_dir + "/MP4/" + name + ".mp4")

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
            cv2.imwrite(
                "{root}/images/{video_name}_frame_{frame_num}.png".format(
                    root=root_dir, video_name=name[4:], frame_num=count_str
                ),
                image,
            )

            count += 1
