def apply(video, operation):
    import cv2, sys
    return_value = []
    while video.isOpened():
        ret, frame = video.read()
        if frame is None:
            continue
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return_value.append(operation(gray))
        # cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frameNumber = video.get(cv2.CAP_PROP_POS_FRAMES)
        sys.stdout.write("\r" + str(frameNumber) + " frame processed...")
        sys.stdout.flush()
        if frameNumber == video.get(cv2.CAP_PROP_FRAME_COUNT):
            break
    video.release()
    cv2.destroyAllWindows()
    return return_value
