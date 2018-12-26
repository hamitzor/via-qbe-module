import cv2
import time

from search_modules.args import parser

parser.add_argument("VIDEO_FILE", help="Video file path that will be used for feature extraction")
parser.add_argument("-s", "--skip", type=int, help="number of frames to skip before processing next frame", default=1)

args = parser.parse_args()

start_time = time.time()

if __name__ == "__main__":
    from search_modules import video as applier
    import search_modules.frame as feature
    import search_modules.db as db

    video_file = args.VIDEO_FILE

    if not args.quiet:
        print "Extracting features from ", video_file

    video = cv2.VideoCapture(video_file)
    applier.apply(video, feature.extract,
                  {"frame_skip_interval": args.skip + 1, "periodically_call": db.insert_feature})

    elapsed_time = time.time() - start_time
    if not args.quiet:
        print "Finished in " + str(int(elapsed_time)) + "s"

    exit(0)
