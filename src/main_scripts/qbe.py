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
    import websocket
    from math import ceil
    import sys
    import traceback
    import signal

    def sigusr1_handler(signum, frame):
        sys.exit(20)

    signal.signal(signal.SIGUSR1, sigusr1_handler)

    def sigusr2_handler(signum, frame):
        sys.exit(21)

    signal.signal(signal.SIGUSR2, sigusr2_handler)

    parser = load_cli_args.parser

    parser.add_argument("video_id",
                        type=int,
                        help="VideoId of the video that example will search inside")

    parser.add_argument("example_file",
                        help="Example image file to search inside the video")

    parser.add_argument("-m",
                        "--min",
                        type=float,
                        help="minimum good features to reckon as match percentage: [0,1]",
                        default=0.1)

    parser.add_argument("-W",
                        "--websocket",
                        action="store_true",
                        help="use websocket to inform")

    parser.add_argument("-WH",
                        "--ws-host",
                        type=str,
                        help="web socket host to be used in informing",
                        default="localhost")

    parser.add_argument("-WP",
                        "--ws-port",
                        type=int,
                        help="web socket port to be used in informing",
                        default=3000)

    parser.add_argument("-WR",
                        "--ws-route",
                        type=str,
                        help="web socket route to be used in informing",
                        default="update-qbe-progress")

    parser.add_argument("-OI",
                        "--operation-id",
                        type=str,
                        help="operation id to be used in informing purposes")

    # load command line arguments
    args = parser.parse_args()

    min_good = args.min
    if min_good < 0:
        min_good = 0

    if min_good > 1.0:
        min_good = 1.0

    use_ws = args.websocket

    if use_ws:
        ws_host = """ws://%s:%s""" % (args.ws_host, args.ws_port)
        ws = websocket.create_connection(ws_host)

    database_config = dict(
        db_host=args.db_host,
        db_username=args.db_username,
        db_password=args.db_password,
        db_name=args.db_name
    )

    video_model = video_model.VideoModel(database_config)
    feature_model = feature_model.FeatureModel(database_config)


    video_meta_data = video_model.get(args.video_id)
    video_path = video_meta_data["path"]
    video_fps = video_meta_data["fps"]
    video_frame_count = video_meta_data["frame_count"]

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
                    height=top_left[1] - bottom_right[1]))
        return result

    def info_function(value, results):
        if use_ws:
            data = dict(route=args.ws_route,
                        data=dict(operationId=args.operation_id,
                                  progress=ceil(value),
                                  results=results))
            ws.send(json.dumps(data, indent=2))

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

    if use_ws:
        ws.close()

    sys.exit(0)
