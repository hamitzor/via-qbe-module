if __name__ == "__main__":
    from search_modules.args import parser

    parser.add_argument("video_id", type=int, help="VideoId of the video that example will search inside")
    parser.add_argument("example_file", help="Example image file to search inside the video")
    parser.add_argument("-m", "--min", type=float, help="minimum good features to reckon as match percentage: [0,1]", default=0.33)
    parser.add_argument("-w", "--wait", type=float, help="duration of showing successful matches in seconds", default=1.0)
    parser.add_argument("-db", "--database", action="store_true", help="use database")

    # load command line arguments
    args = parser.parse_args()

    from search_modules import util
    import cv2
    import numpy as np
    import ujson
    from search_modules import video
    from search_modules import frame as frame_operations
    from search_modules import database
    from operator import itemgetter
    from itertools import groupby

    start_time = util.get_time()

    util.write("Searching \"" + args.example_file + "\" in the video with VideoId=" + str(args.video_id))

    # read query image
    query_image = cv2.imread(args.example_file, 0)

    # extract features from query image
    query_features = frame_operations.extract(query_image)

    # read video file to be used in video.apply function
    video_file = cv2.VideoCapture(database.get_video_path(args.video_id))

    # read video for display purposes
    video_file_display = cv2.VideoCapture(database.get_video_path(args.video_id))

    # list that holds matches
    find = []


    # function to be used as operation parameter in video.apply function
    def display_matches(frame, frame_no):

        # get features between specied frame_no and frame_no + specified skip number
        features = database.get_video_features(frame_no, frame_no + int(args.skip) - 2)

        # group features by frame no
        sort_key = itemgetter(3)

        result = []
        for key, value in groupby(features, key=sort_key):
            result.append(dict(frame_no=key, result=list((v[0], v[1], v[2]) for v in value)))

        global video_file_display

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
            good = frame_operations.match(query_features[1], feature_set[1])

            # if number of good matches is greater than specified percentage of total number of features consider them as real match
            if len(good) > int(len(query_features[0]) * args.min):
                global find
                # save frame no and coordinates for api usage purposes
                # @TODO extract coordinates
                find.append({"frame_number": frame_no, "top_left": 0, "bottom_right": 0})

                # if command wasn't executed for api usage, display matches individually
                if not args.api:
                    # format points from good matches for finding homography
                    query_points = np.float32([query_features[0][m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                    train_points = np.float32([feature_set[0][m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

                    # find homography using RANSAC algorithm and collect the mask that specifies inliers and outliers
                    mask = cv2.findHomography(query_points, train_points, cv2.RANSAC, 5.0)[1]

                    matches_mask = mask.ravel().tolist()

                    draw_params = dict(matchColor=(20, 255, 20),
                                       singlePointColor=None,
                                       matchesMask=matches_mask,  # draw only inliers
                                       flags=2)

                    # skip video file to the frame that match was found
                    video_file_display.set(cv2.CAP_PROP_POS_FRAMES, frame_no)

                    # read the frame
                    ret, frame = video_file_display.read()

                    # draw matches with calculated parameters above
                    img3 = cv2.drawMatches(query_image, query_features[0], frame, feature_set[0], good, None, **draw_params)

                    # show frame
                    cv2.imshow("Frame - " + str(frame_no), img3)
                    cv2.waitKey(int(args.wait * 1000))
                    cv2.destroyAllWindows()

        return True


    # call video.apply with specified video file with specified parameters
    video.apply(video_file, operation=display_matches, skip_amount=args.skip, begin=args.begin, end=args.end, info_function=util.info_function)

    # if command was executed for api usage print json encoded find list
    if args.api:
        import json

        print json.dumps(find)

    util.passed_time(start_time, "Process finished in")

    exit(0)