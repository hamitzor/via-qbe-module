import numpy as np
import cv2

if __name__ == "__main__":
    import video_operations.applier as applier
    import frame_operations.feature as feature
    import sys

    if len(sys.argv) < 3:
        print "Cannot continue because video and example arguments are empty. Use this command like: python qbe.py VIDEO_ID EXAMPLE_IMAGE_FILE [MIN_MATCH_COUNT]"
        exit(-1)
    else:
        minMatchCount = 50

        if len(sys.argv) > 3:
            minMatchCount = int(sys.argv[3])


        videoId = sys.argv[1]
        exampleFile = sys.argv[2]

        print "Searching",exampleFile,"in VideoId=",videoId,"with options: ","\nMinimum Feature Match Count Per Frame =",minMatchCount
        query = cv2.imread(exampleFile, 0)

        out = ''

        query_features = feature.extract(query)

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

                video_frames[index] = cv2.polylines(video_frames[index], [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

                draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                                   singlePointColor=None,
                                   matchesMask=matchesMask,  # draw only inliers
                                   flags=2)

                img3 = cv2.drawMatches(query, query_features[0], video_frames[index], f[0], good, None, **draw_params)

                cv2.imshow("Frame - " + str(frameNumber), img3)
                cv2.waitKey(0)
                cv2.destroyAllWindows()



    print ""
    exit(0)
