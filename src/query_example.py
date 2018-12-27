import cv2
import numpy as np
import time

from search_modules.args import parser

parser.add_argument("video_id", type=int, help="VideoId of the video that example will search inside")
parser.add_argument("example_file", help="Example image file to search inside the video")
parser.add_argument("-m", "--min", type=float, help="minimum good features to reckon as match percentage: [0,1]", default=0.33)
parser.add_argument("-db", "--database", action="store_true", help="use database")

args = parser.parse_args()

if __name__ == "__main__":
    from search_modules import video
    from search_modules import frame as feature
    from search_modules import database

    min_match_percentage = args.min
    video_id = args.video_id
    example_file_path = args.example_file

    if not args.quiet and not args.api:
        print "Searching \"" + example_file_path + "\" in the video with VideoId=" + str(video_id)

    query_image = cv2.imread(example_file_path, 0)

    query_features = feature.extract(query_image)

    video_file = cv2.VideoCapture(database.get_video_path(video_id))

    find = []

    def display_matches(frame, frame_number):
        if args.database:
            start_time = int(round(time.time() * 1000))
            features = database.get_video_features(frame_number)

            kp = []
            des = []
            for j in range(len(features)):
                key_point = cv2.KeyPoint()
                key_point.pt = (features[j][2], features[j][3])
                kp.append(key_point)
                des_array = []

                for i in range(128):
                    des_array.append(features[j][i + 4])

                des.append(des_array)

            des = np.asarray(des, np.float32)
            feature_set = (kp, des)
            elapsed_time = int(round(time.time() * 1000)) - start_time
            print len(des)
            print "Frame features ready in " + str(elapsed_time) + "ms  --database"
            exit(0)

        else:
            start_time = int(round(time.time() * 1000))
            feature_set = feature.extract(frame)
            elapsed_time = int(round(time.time() * 1000)) - start_time
            print "Frame features ready in " + str(elapsed_time) + "ms  --non-database"

        good = feature.match(query_features[1], feature_set[1])

        min_match_count = int(len(query_features[0]) * min_match_percentage)

        if len(good) > min_match_count:
            global find
            find.append({"frame_number": frame_number})

            if not args.api:
                src_pts = np.float32([query_features[0][m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                dst_pts = np.float32([feature_set[0][m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

                m, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                matches_mask = mask.ravel().tolist()

                h, w = query_image.shape
                pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, m)

                frame = cv2.polylines(frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

                draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                                   singlePointColor=None,
                                   matchesMask=matches_mask,  # draw only inliers
                                   flags=2)

                img3 = cv2.drawMatches(query_image, query_features[0], frame, feature_set[0], good, None,
                                       **draw_params)

                cv2.imshow("Frame - " + str(frame_number), img3)
                cv2.waitKey(1500)
                cv2.destroyAllWindows()


    meta = video.apply(video_file, operation=display_matches)

    if not args.quiet and not args.api:
        if len(find) > 0:
            print "Image exists in seconds:"
            for i in range(len(find)):
                print round(find[i]["frame_number"] / meta["fps"], 2)
        else:
            print ""

    if args.api:
        import json

        print json.dumps(find)

    exit(0)
