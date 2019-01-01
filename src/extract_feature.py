if __name__ == "__main__":
    from search_modules.args import parser

    parser.add_argument("video_file", help="Video file path that will be used for feature extraction")

    args = parser.parse_args()

    import cv2
    from search_modules import util
    from search_modules import video as applier
    from search_modules import frame
    from search_modules import database

    start_time = util.get_time()

    video_file = args.video_file

    util.write("Extracting features from " + str(video_file))

    # read video file to be used in video.apply function
    video = cv2.VideoCapture(video_file)

    # call video.apply with specified video file, specified parameters and a lambda expression consist of database.insert_feature and frame.extract.
    # return value of frame.extract supplied to database.insert_feature which inserts features to database
    applier.apply(video, operation=lambda x, y: (database.insert_feature(frame.extract(x), y)), skip_amount=args.skip, begin=args.begin,
                  end=args.end, info_function=util.info_function)

    util.passed_time(start_time, "Finished in")

    exit(0)