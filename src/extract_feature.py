import cv2
import time

from search_modules.args import parser

parser.add_argument("video_file", help="Video file path that will be used for feature extraction")

args = parser.parse_args()

start_time = time.time()

if __name__ == "__main__":
    from search_modules import video as applier
    import search_modules.frame as feature
    import search_modules.database as db

    video_file = args.video_file

    if not args.quiet and not args.api:
        print "Extracting features from ", video_file

    video = cv2.VideoCapture(video_file)

    applier.apply(video, operation=lambda x, y: (db.insert_feature(feature.extract(x), y)))

    elapsed_time = time.time() - start_time
    if not args.quiet and not args.api:
        print "Finished in " + str(int(elapsed_time)) + "s"

    exit(0)
