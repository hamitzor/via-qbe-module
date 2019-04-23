"""Script to be used for query by example."""
if __name__ == "__main__":
    import time
    start_time = time.time() * 1000

    from ..core import feature as feature_module
    from ..util import load_cli_args, operation_applier, stdout
    from ..models import feature_model, video_model
    import cv2
    import numpy as np
    import ujson

    parser = load_cli_args.parser

    parser.add_argument("video_id",
                        type=str,
                        help="id of the video file which example will be queried in")

    parser.add_argument("example_file_path",
                        type=str,
                        help="Example image file to be queried in the video")

    parser.add_argument("-m",
                        "--min",
                        type=float,
                        help="minimum good features to reckon as match percentage: [0,1]",
                        default=0.1)

    parser.add_argument("-w",
                        "--wait",
                        type=float,
                        help="duration of showing successful matches in seconds",
                        default=1.0)

    # load command line arguments
    args = parser.parse_args()

    min_good = args.min
    if min_good < 0:
        min_good = 0

    if min_good > 1.0:
        min_good = 1.0

    stdout = stdout.Stdout(args.api or args.quiet)

    database_config = dict(
        db_host=args.db_host,
        db_username=args.db_username,
        db_password=args.db_password,
        db_name=args.db_name
    )

    feature_model = feature_model.FeatureModel(database_config)
    video_model = video_model.VideoModel(database_config)
    # read query image
    query_image = cv2.imread(args.example_file_path, 0)

    # extract features from query image
    query_features = feature_module.extract(query_image)

    video_meta_data = video_model.get(args.video_id)
    video_file_path = video_meta_data["path"]
    video_fps = video_meta_data["fps"]
    video_total_frame_count = video_meta_data["total_frame_count"]

    video_cap = cv2.VideoCapture(video_file_path)

    def find_matches(frame_no, _):
        # get features in specied frame_no
        features = feature_model.get_multiple(args.video_id, frame_no)
        if features:
            # container for formatted key points
            kp = []
            # container for formatted descriptors
            des = []

            # iterate over these features for formatting purposes
            for feature in features:
                key_point = cv2.KeyPoint()
                key_point.pt = (feature[0], feature[1])
                kp.append(key_point)
                # decode json encoded list and append to des container
                des.append(ujson.loads(feature[2]))

            # cast list to numpy array for matching purposes
            des = np.asarray(des, np.float32)

            # create a tuple of key points and descriptor with corresponding indices for matching
            feature_set = (kp, des)

            # use frame.match function for matching and collect good matches
            good = feature_module.match(query_features[1], feature_set[1])

            # if number of good matches is greater than specified percentage of
            # total number of features consider them as real match
            if len(good) > int(len(query_features[0]) * min_good):
                pts, mask = feature_module.get_homography_points(query_features[0],
                                                                 feature_set[0],
                                                                 good,
                                                                 query_image)

                # skip video file to the frame that match was found
                video_cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)

                # read the frame
                _, frame = video_cap.read()

                matchesMask = mask.ravel().tolist()

                draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                                   singlePointColor=None,
                                   matchesMask=matchesMask,  # draw only inliers
                                   flags=2)

                frame = cv2.polylines(frame,
                                      [np.int32(pts)],
                                      True,
                                      255,
                                      3,
                                      cv2.LINE_AA)
                # draw matches with calculated parameters above

                frame = cv2.drawMatches(query_image,
                                        query_features[0],
                                        frame,
                                        feature_set[0],
                                        good,
                                        None,
                                        **draw_params)

                # show frame
                cv2.imshow("Frame - " + str(frame_no), frame)
                cv2.waitKey(int(args.wait * 1000))
                cv2.destroyAllWindows()

    stdout.write("Querying %s in video with id = %s" %
                 (args.example_file_path, args.video_id))

    apply_params = dict(
        operation=find_matches,
        skip_amount=args.skip,
        begin=args.begin,
        end=args.end,
        info_function=stdout.progres_info
    )

    # call operation_applier.apply with specified video file with specified parameters
    operation_applier.apply(None,
                            video_total_frame_count,
                            video_fps,
                            **apply_params)

    stdout.passed_time(start_time, "Finished in")
    exit(0)
