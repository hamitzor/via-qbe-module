if __name__ == "__main__":
    from modules.args import parser

    parser.add_argument(
        "video_id", help="VideoId value of the tupple that is going to be used for feature extraction")

    args = parser.parse_args()

    import cv2
    from modules import util
    from modules import video as applier
    from modules import frame
    from modules import database

    start_time = util.get_time()

    video_file_path = database.get_video_path(args.video_id)

    util.write("Extracting features from " + str(video_file_path))

    # read video file to be used in video.apply function
    video = cv2.VideoCapture(video_file_path)

    # call video.apply with specified video file, specified parameters and a lambda expression consist of database.insert_feature and frame.extract.
    # return value of frame.extract supplied to database.insert_feature which inserts features to database
    applier.apply(video, operation=lambda x, y: (database.insert_feature(frame.extract(x), y)), skip_amount=args.skip, begin=args.begin,
                  end=args.end, info_function=util.info_function)

    util.passed_time(start_time, "Finished in")

    exit(0)
