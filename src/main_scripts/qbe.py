"""Script to be used for query by example."""
if __name__ == "__main__":
    import time
    start_time = time.time() * 1000

    from ..core import feature as feature_module
    from ..util import load_cli_args, operation_applier, stdout
    from ..models import video_model, feature_model, operation_model
    import cv2
    import numpy as np
    import ujson
    import json
    import websocket
    from math import ceil

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
                        type=int,
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

    stdout = stdout.Stdout(args.api or args.quiet)

    database_config = dict(
        db_host=args.db_host,
        db_username=args.db_username,
        db_password=args.db_password,
        db_name=args.db_name
    )

    video_model = video_model.VideoModel(database_config)
    feature_model = feature_model.FeatureModel(database_config)
    operation_model = operation_model.OperationModel(database_config)

    operation = operation_model.get(args.operation_id)

    if operation["start_time"]:
        raise Exception("This operation had already started to execute")

    video_meta_data = video_model.get(args.video_id)
    video_path = video_meta_data["path"]
    video_fps = video_meta_data["fps"]
    video_frame_count = video_meta_data["frame_count"]

    # read query image
    query_image = cv2.imread(args.example_file, 0)

    # extract features from query image
    query_features = feature_module.extract(query_image)

    # list that holds matches
    find = []

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

                x_coordinates = [pts[i][0][0] for i in range(4)]
                y_coordinates = [pts[i][0][1] for i in range(4)]

                top_left = [int(np.amin(x_coordinates)),
                            int(np.amax(y_coordinates))]
                bottom_right = [int(np.amax(x_coordinates)),
                                int(np.amin(y_coordinates))]

                # save frame no and top left and right bottom points
                find.append(dict(frameNo=int(frame_no),
                                 boundary=dict(left=top_left[0],
                                               top=top_left[1],
                                               width=(
                                                   bottom_right[0] - top_left[0]),
                                               height=top_left[1] - bottom_right[1])))

    stdout.write("Searching %s in video with id = %s" %
                 (args.example_file, args.video_id))

    watch_id = (operation_model.get(args.operation_id))["watch_id"]

    def info_function(value):
        if use_ws:
            data = dict(route=args.ws_route,
                        data=dict(id=watch_id,
                                  value=ceil(value)))
            ws.send(json.dumps(data, indent=2))

    apply_params = dict(
        operation=find_matches,
        skip_amount=args.skip,
        begin=args.begin,
        end=args.end,
        info_function=info_function
    )



    operation_model.update(args.operation_id, dict(
        start_time=time.strftime("%Y-%m-%d %H:%M:%S")))
    # call operation_applier.apply with specified video file with specified parameters
    operation_applier.apply(None, video_frame_count, video_fps, **apply_params)

    if args.operation_id:
        result = json.dumps(find, indent=4)
        operation_model.update(args.operation_id,
                               dict(end_time=time.strftime("%Y-%m-%d %H:%M:%S"),
                                    result=result))

    if use_ws:
        ws.close()

    if not args.api:
        print "\n"
    print json.dumps(find, indent=4)

    stdout.passed_time(start_time, "Finished in")
    exit(0)
