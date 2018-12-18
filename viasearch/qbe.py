import numpy as np
import cv2

if __name__ == "__main__":
    import video_operations.applier as applier
    import frame_operations.feature as feature

    query = cv2.imread('tiger.jpg', 0)
    video = cv2.VideoCapture('tiger.mp4')
    video_frames = []

    while video.isOpened():
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        video_frames.append(gray)
        if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
            break
    video.release()
    video = cv2.VideoCapture('tiger.mp4')
    out = applier.apply(video, feature.extract)

    query_features = feature.extract(query)

    for index, f in enumerate(out):
        good = feature.match(query_features[1], f[1])
        if len(good) > 160:
            print len(good)
            img3 = cv2.drawMatchesKnn(query, query_features[0], video_frames[index], f[0], good, None, flags=2)
            cv2.imshow('Frame - ' + str(index), img3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
