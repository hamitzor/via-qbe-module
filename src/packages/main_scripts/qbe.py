"""Script to be used for query by example."""
if __name__ == "__main__":
    import time
    start_time = time.time() * 1000

    from ..core import feature as feature_module
    from ..util import load_cli_args, operation_applier
    from ..models import video_model, feature_model
    import cv2
    import numpy as np
    import ujson
    import json
    from math import ceil
    import sys

    parser = load_cli_args.parser

    parser.add_argument("video_id",
                        type=int,
                        help="VideoId of the video that example will in inside")

    parser.add_argument("example_file",
                        help="Example image file to query in the video")

    parser.add_argument("-m",
                        "--min",
                        type=float,
                        help="minimum good features to reckon as match percentage: [0,1]",
                        default=0.1)

    # load command line arguments
    args = parser.parse_args()

    min_good = args.min
    if min_good < 0:
        min_good = 0

    if min_good > 1.0:
        min_good = 1.0

    database_config = dict(
        db_host=args.db_host,
        db_username=args.db_username,
        db_password=args.db_password,
        db_name=args.db_name
    )

    video_model = video_model.VideoModel(database_config)
    feature_model = feature_model.FeatureModel(database_config)
    video_info = video_model.get(args.video_id)
    video_path = video_info["path"]
    video_fps = video_info["fps"]
    video_frame_count = video_info["frame_count"]

    # read query image
    query_image = cv2.imread(args.example_file, 0)

    # extract features from query image
    query_features = feature_module.extract(query_image)

    def find_matches(frame_no, _):
        result = None
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

                x_coordinates = [pts[i][0][0] for i in range(4)]
                y_coordinates = [pts[i][0][1] for i in range(4)]

                top_left = [int(np.amin(x_coordinates)),
                            int(np.amax(y_coordinates))]
                bottom_right = [int(np.amax(x_coordinates)),
                                int(np.amin(y_coordinates))]

                # save frame no and top left and right bottom points
                result = dict(frameNo=int(frame_no),
                              boundary=dict(left=top_left[0],
                                            top=top_left[1],
                                            width=(
                                  bottom_right[0] - top_left[0]),
                    height=bottom_right[1] - top_left[1]))
        return result

    def info_function(value, results):
        data = dict(progress=ceil(value),
                    results=results)
        sys.stdout.write(json.dumps(data, indent=2))
        sys.stdout.flush()

    apply_params = dict(
        operation=find_matches,
        skip_amount=args.skip,
        begin=args.begin,
        end=args.end,
        info_function=info_function
    )

    # call operation_applier.apply with specified video file with specified parameters
    operation_applier.apply(None, video_frame_count,
                            video_fps, **apply_params)

    sys.exit(0)
