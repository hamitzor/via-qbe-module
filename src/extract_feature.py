"""Script to extract features from video."""
if __name__ == "__main__":
    from modules import args, stdout, video, feature, database
    import cv2
    import time
    import os

    parser = args.parser

    parser.add_argument(
        "video_id", help="VideoId value of the tupple that is going to be used for feature extraction")
    args = parser.parse_args()
    stdout = stdout.Stdout(args.api or args.quiet)
    start_time = time.time() * 1000
    database = database.Database()
    video_meta = database.get_video(args.video_id)
    video_format = video_meta[4]
    video_blob = video_meta[7]

    # read video file to be used in video.apply function
    temp_file_path = video.write_base64(video_blob, video_format)
    video_cap = cv2.VideoCapture(temp_file_path)

    def apply_operation(frame, frame_no):
        """Extract features from frame and insert. This method will be passed to video.apply as operation argument"""

        features = feature.extract(frame)
        data = []
        # Iterate over features format and append to data
        for i in range(len(features[0])):
            data.append((
                frame_no,
                features[0][i].pt[0],
                features[0][i].pt[1],
                str(features[1][i].astype(int).tolist()).replace(" ", "")
            ))
        database.insert_features(args.video_id, data)

    stdout.write("Extracting features...")
    # call video.apply with specified video file, specified parameters and a method named apply_operation uses database.insert_feature and feature.extract.
    video.apply(video_cap,
                operation=apply_operation,
                skip_amount=args.skip,
                begin=args.begin,
                end=args.end,
                info_function=stdout.progres_info)

    os.remove(temp_file_path)
    stdout.passed_time(start_time, "Finished in")

    exit(0)
