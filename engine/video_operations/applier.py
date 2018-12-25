def apply(video, operation, options={}):
    import cv2, sys, gc
    returnValue = []

    def periodicallyCall():
        pass

    if "periodicallyCall" in options:
        periodicallyCall = options["periodicallyCall"]

    periodicallyCallInterval = 1000
    frameSkipInterval = 10

    if "periodicallyCallInterval" in options:
        periodicallyCallInterval = options["periodicallyCallInterval"]

    if "frameSkipInterval" in options:
        frameSkipInterval = options["frameSkipInterval"]

    while video.isOpened():
        ret, frame = video.read()
        if frame is None:
            break

        frameNumber = int(video.get(cv2.CAP_PROP_POS_FRAMES))

        if frameNumber % frameSkipInterval != 0:
            if frameNumber == video.get(cv2.CAP_PROP_FRAME_COUNT):
                break
            else:
                continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        returnValue.append({"data": operation(gray), "frameNumber": frameNumber})

        sys.stdout.write("\r" + str(frameNumber) + ". frame processed. ")
        sys.stdout.flush()

        if frameNumber % periodicallyCallInterval == 0:
            periodicallyCall(returnValue)
            returnValue = []
            gc.collect()

        if frameNumber == video.get(cv2.CAP_PROP_FRAME_COUNT):
            break

    if len(returnValue) > 0:
        periodicallyCall(returnValue)
        returnValue = []
        gc.collect()

    video.release()
    return returnValue
