import numpy as np
import cv2

if __name__ == "__main__":
    import video_operations.applier as applier
    import frame_operations.feature as feature
    import sys

    if len(sys.argv) < 3:
        print "Cannot continue because video and example arguments are empty. Use this command like: python query_by_example.py VIDEO_FILE EXAMPLE_IMAGE_FILE [MIN_MATCH_COUNT]"
        exit(-1)
    else:
        minMatchCount = 50

        if len(sys.argv) > 3:
            minMatchCount = int(sys.argv[3])


        videoFile = sys.argv[1]
        exampleFile = sys.argv[2]

        print "Searching",exampleFile,"in",videoFile, "with options: ", "\nMinimum Feature Match Count Per Frame =",minMatchCount
        query = cv2.imread(exampleFile, 0)

        video = cv2.VideoCapture(videoFile)
        video_frames = []
        while video.isOpened():
            ret, frame = video.read()
            if frame is None:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            video_frames.append(gray)
            if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
                break
        video.release()

        video = cv2.VideoCapture(videoFile)

        query_features = feature.extract(query)

        def matcher(out):
            for index, f in enumerate(out):
                frameNumber = f['frameNumber']
                f = f['data']
                good = feature.match(query_features[1], f[1])
                if len(good) > minMatchCount:
                    src_pts = np.float32([query_features[0][m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                    dst_pts = np.float32([f[0][m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

                    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                    matchesMask = mask.ravel().tolist()

                    h, w = query.shape
                    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                    dst = cv2.perspectiveTransform(pts, M)

                    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                                       singlePointColor=None,
                                       matchesMask=matchesMask,  # draw only inliers
                                       flags=2)

                    img3 = cv2.drawMatches(query, query_features[0], video_frames[frameNumber], f[0], good, None, **draw_params)

                    cv2.imshow("Frame - " + str(frameNumber), img3)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

        applier.apply(video, feature.extract,
                      {"frameSkipInterval": 2, "periodicallyCall": matcher, "periodicallyCallInterval": 1})

    print ""
    exit(0)
