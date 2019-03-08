"""Script to be used for query by example."""
if __name__ == "__main__":
    from modules import args, stdout, video, feature, database
    import cv2
    import numpy as np
    import ujson
    import time
    from operator import itemgetter
    from itertools import groupby
    import json
    import os

    parser = args.parser

    parser.add_argument(
        "video_id", type=int, help="VideoId of the video that example will search inside")
    parser.add_argument(
        "example_file", help="Example image file to search inside the video")
    parser.add_argument("-m", "--min", type=float,
                        help="minimum good features to reckon as match percentage: [0,1]", default=0.33)
    parser.add_argument("-w", "--wait", type=float,
                        help="duration of showing successful matches in seconds", default=1.0)

    # load command line arguments
    args = parser.parse_args()

    stdout = stdout.Stdout(args.api or args.quiet)
    database = database.Database()

    video_meta = database.get_video(args.video_id)
    video_format = video_meta[4]
    video_blob = video_meta[7]

    # read video file to be used in video.apply function
    video_file_path = video.write_base64(video_blob, video_format)

    start_time = time.time() * 1000

    stdout.write("Searching %s in video with id = %s" %
                 (args.example_file, args.video_id))

    # read query image
    query_image = cv2.imread(args.example_file, 0)

    # extract features from query image
    query_features = feature.extract(query_image)

    # read video file to be used in video.apply function
    video_file = cv2.VideoCapture(video_file_path)

    video_file_display = None

    if args.display:
        # read video for display purposes
        video_file_display = cv2.VideoCapture(video_file_path)

    # list that holds matches
    find = []

    def display_matches(_, frame_no):
        # get features between specied frame_no and frame_no + specified skip number
        features = database.get_features(args.video_id, frame_no)

        # group features by frame no
        sort_key = itemgetter(3)

        result = []
        for key, value in groupby(features, key=sort_key):
            result.append(dict(frame_no=key, result=list(
                (v[0], v[1], v[2]) for v in value)))

        # iterate over features that grouped by frame no
        for frame_result in result:

            # extract frame no
            frame_no = frame_result["frame_no"]

            # extract features that located in frame no extracted above
            frame_result = frame_result["result"]

            # container for formatted key points
            kp = []
            # container for formatted descriptors
            des = []

            # iterate over these features for formatting purposes
            for frame_feature in frame_result:
                key_point = cv2.KeyPoint()
                key_point.pt = (frame_feature[0], frame_feature[1])
                kp.append(key_point)
                # decode json encoded list and append to des container
                des.append(ujson.loads(frame_feature[2]))

            # cast list to numpy array for matching purposes
            des = np.asarray(des, np.float32)

            # create a tuple of key points and descriptor with corresponding indices for matching
            feature_set = (kp, des)

            # use frame.match function for matching and collect good matches
            good = feature.match(query_features[1], feature_set[1])

            # if number of good matches is greater than specified percentage of total number of features consider them as real match

            if len(good) > int(len(query_features[0]) * args.min):
                # format points from good matches for finding homography
                query_points = np.float32(
                    [query_features[0][m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                train_points = np.float32(
                    [feature_set[0][m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

                # find homography using RANSAC algorithm and collect the mask that specifies inliers and outliers
                M, mask = cv2.findHomography(
                    query_points, train_points, cv2.RANSAC, 5.0)

                h, w = query_image.shape
                pts = np.float32(
                    [[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, M)

                # save frame no and coordinates
                find.append(
                    {"frame_no": frame_no, "corners": (dst[0][0].tolist(), dst[1][0].tolist(), dst[2][0].tolist(), dst[3][0].tolist())})

                if args.display:
                    # skip video file to the frame that match was found
                    video_file_display.set(cv2.CAP_PROP_POS_FRAMES, frame_no)

                    # read the frame
                    _, frame = video_file_display.read()

                    matchesMask = mask.ravel().tolist()

                    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                                       singlePointColor=None,
                                       matchesMask=matchesMask,  # draw only inliers
                                       flags=2)

                    frame = cv2.polylines(
                        frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
                    # draw matches with calculated parameters above
                    if args.display_features:
                        frame = cv2.drawMatches(
                            query_image, query_features[0], frame, feature_set[0], good, None, **draw_params)

                    # show frame
                    cv2.imshow("Frame - " + str(frame_no), frame)
                    cv2.waitKey(int(args.wait * 1000))
                    cv2.destroyAllWindows()

    # call video.apply with specified video file with specified parameters
    video.apply(video_file, operation=display_matches, skip_amount=args.skip,
                begin=args.begin, end=args.end, info_function=stdout.progres_info)

    if not args.display:
        print json.dumps(find, indent=3)

    os.remove(video_file_path)
    stdout.passed_time(start_time, "Finished in")

    exit(0)
