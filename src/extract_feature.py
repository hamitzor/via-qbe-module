"""Script to extract features from video."""
if __name__ == "__main__":
    from modules import args, stdout, video as applier, feature, database
    import cv2
    import time

    parser = args.parser

    parser.add_argument(
        "video_id", help="VideoId value of the tupple that is going to be used for feature extraction")
    args = parser.parse_args()
    stdout = stdout.Stdout(args.api or args.quiet)
    start_time = time.time() * 1000
    database = database.Database()
    video_file_path = database.get_video(args.video_id, 'FilePath')

    stdout.write("Extracting features from " + str(video_file_path))

    # read video file to be used in video.apply function
    video = cv2.VideoCapture(video_file_path)

    # call video.apply with specified video file, specified parameters and a lambda expression uses database.insert_feature and feature.extract.
    # return value of feature.extract supplied to database.insert_feature which inserts features to database
    applier.apply(video, operation=lambda x, y: database.insert_features(1, feature.extract(x), y), skip_amount=args.skip, begin=args.begin,
                  end=args.end, info_function=stdout.progres_info)

    stdout.passed_time(start_time, "Finished in")

    exit(0)
