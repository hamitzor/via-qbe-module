from search_modules.args import parser

args = parser.parse_args()


def apply(video, operation, options=None):
    if options is None:
        options = {}

    import cv2
    import sys
    import gc

    return_value = []

    def periodically_call(arg):
        pass

    if "periodically_call" in options:
        periodically_call = options["periodically_call"]

    frame_skip_interval = 2

    if "frame_skip_interval" in options:
        frame_skip_interval = options["frame_skip_interval"]

    while video.isOpened():
        ret, frame = video.read()
        if frame is None:
            break

        frame_number = int(video.get(cv2.CAP_PROP_POS_FRAMES))

        if 0 != frame_number % frame_skip_interval:
            if frame_number == video.get(cv2.CAP_PROP_FRAME_COUNT):
                break
            else:
                continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return_value.append({"data": operation(gray), "frame_number": frame_number})

        if not args.quiet:
            sys.stdout.write("\r" + str(frame_number) + ". frame processed. ")
            sys.stdout.flush()

        periodically_call(return_value)
        return_value = []
        gc.collect()

        if frame_number == video.get(cv2.CAP_PROP_FRAME_COUNT):
            break

    if len(return_value) > 0:
        periodically_call(return_value)

    video.release()
    return 0
