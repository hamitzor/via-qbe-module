import numpy as np
import cv2
import time

start_time = time.time()

if __name__ == "__main__":
    import video_operations.applier as applier
    import frame_operations.feature as feature
    import database_operations.db as db
    import sys

    if len(sys.argv) < 1:
        print "Cannot continue because video argument is empty. Use this command like: python extract_feature_from_video.py VIDEO_FILE [OPTIONS]"
        exit(-1)
    else:
        videoFile = sys.argv[1]

        print "Extracting features from ", videoFile, "with no options."

        video = cv2.VideoCapture(videoFile)
        applier.apply(video, feature.extract,
                            {"frameSkipInterval": 2, "periodicallyCall": db.insertFeature, "periodicallyCallInterval": 1})


    elapsed_time = time.time() - start_time
    print "Finished in " + str(int(elapsed_time)) + "s"

    exit(0)
