import cv2

video = cv2.VideoCapture('./video.mp4')

length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

print("length :", length)
print("width :", width)
print("height :", height)
print("fps :", fps)

count = 0

while (video.isOpened()):
    ret, image = video.read()

    if (int(video.get(1)) % 10 == 0):
        print('Saved frame number : ' + str(int(video.get(1))))
        count_str = format(count, '06')
        cv2.imwrite("./images/frame_%s.PNG" % count_str, image)
        count += 1

video.release()
