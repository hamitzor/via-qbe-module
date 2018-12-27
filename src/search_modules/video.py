from args import parser
import cv2

args = parser.parse_args()


def apply(video, operation=lambda x, y: None):
    """A function that extracts frames and applies specified operations on them

        This function extracts the specified video into frames, converts those frames to gray color and exclusively initiates given operation
        function with two parameters, frame and frame number:

        Args:
            video (:obj:`cv2.VideoCapture`): Video to be used.
            operation (:obj:`function`): Operation to be applied on frames.

        Returns:
            :obj:`dict`: A dictionary of meta data of the video. This data consists of fps,
        """
    import sys


    fps = video.get(cv2.CAP_PROP_FPS)

    frame_rate = args.rate


    while video.isOpened():
        ret, frame = video.read()

        frame_number = int(video.get(cv2.CAP_PROP_POS_FRAMES))

        # if frame is None or it has reached the specified ending second, break.
        if (frame is None) or (frame_number > fps * args.end):
            break

        # if it has not yet reached the specified beginning second, skip.
        if frame_number < fps * args.begin:
            continue

        # this section provides frame rate flexibility. if frame number is divisible with frame rate skip that frame.
        if 0 != frame_number % frame_rate:
            if frame_number == video.get(cv2.CAP_PROP_FRAME_COUNT):
                break
            else:
                continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if not args.quiet and not args.api:
            sys.stdout.write("\r" + str(frame_number) + ". frame processed. ")
            sys.stdout.flush()
        operation(gray, frame_number)

        if frame_number == video.get(cv2.CAP_PROP_FRAME_COUNT):
            break

    video.release()

    return {"fps": fps}
