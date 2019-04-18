"""Script to extract features from video."""
if __name__ == "__main__":
    import time
    start_time = time.time() * 1000

    from ..util import load_cli_args, stdout, operation_applier
    from ..core import feature
    from ..models import feature_model, video_model
    import cv2
    import json
    from websocket import create_connection

    parser = load_cli_args.parser

    parser.add_argument("video_id",
                        help="video_id of the video that is going to be used for feature extraction")
    
    args = parser.parse_args()

    stdout = stdout.Stdout(args.api or args.quiet)

    database_config = dict(
        db_host=args.db_host,
        db_username=args.db_username,
        db_password=args.db_password,
        db_name=args.db_name
    )

    video_model = video_model.VideoModel(database_config)
    feature_model = feature_model.FeatureModel(database_config)

    video_meta = video_model.get(args.video_id)
    video_path = video_meta["path"]
    video_fps = video_meta["fps"]
    video_frame_count = video_meta["frame_count"]

    # read video file to be used in video.apply function
    video_cap = cv2.VideoCapture(video_path)

    def apply_operation(frame_no, frame):
        """Extract features from frame and insert. This function will be passed to video.apply as operation argument"""

        if frame is not None:
            features = feature.extract(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
            data = []
            # Iterate over features format and append to data
            for i in range(len(features[0])):
                data.append((
                    features[0][i].pt[0],
                    features[0][i].pt[1],
                    str(features[1][i].astype(int).tolist()).replace(" ", ""),
                    frame_no
                ))
            feature_model.insert_multiple(args.video_id, data)

    stdout.write("Extracting features...")

    apply_params = dict(
        skip_amount=args.skip,
        operation=apply_operation,
        begin=args.begin,
        end=args.end,
        info_function=stdout.progres_info
    )

    # call operation_applier.apply with specified video file, specified parameters and a function named apply_operation uses database.insert_feature and feature.extract.
    operation_applier.apply(video_cap,
                            video_frame_count,
                            video_fps,
                            **apply_params)

    stdout.passed_time(start_time, "Finished in")
    exit(0)
