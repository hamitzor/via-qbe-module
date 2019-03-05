import cv2


def apply(video, operation=lambda x, y: None, skip_amount=1, begin=0, end=2147483646, info_function=lambda x: None):
    """A function that extracts frames and applies specified operations on them

        This function extracts the specified video into frames, converts those frames to gray color and exclusively initiates given operation
        function with two parameters, frame and frame number:

        Args:
            video (:obj:`cv2.VideoCapture`): Video to be used.
            operation (:obj:`function`): Operation function to be applied on frames.
            skip_amount: (int): Amount of frames to skip before executing the next frame.
            info_function: (:obj:`function`): The function to be used in inform purposes. A number between 0 and 100 that specifies progress
            percentage will be supplied to this function on every iteration.
            begin: (int): The first second to process
            end: (int): The last second to process(Excluded)

        Returns:
            :obj:`dict`: A dictionary of meta data of the video. This data consists of fps,
        """
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    # forward to specified time.
    video.set(cv2.CAP_PROP_POS_MSEC, begin * 1000)

    while video.isOpened():
        ret, frame = video.read()

        frame_number = int(video.get(cv2.CAP_PROP_POS_FRAMES))

        # call info function with progress percentage
        info_function(round(frame_number / frame_count, 2) * 100)

        # if frame is None or it has reached the specified ending second, break.
        if (frame is None) or (int(video.get(cv2.CAP_PROP_POS_MSEC) / 1000) > end):
            break

        # call specified operation function, if it returns False, stop execution.
        if not operation(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), frame_number):
            break

        # if it has reached the last frame, stop execution.
        if frame_number >= frame_count - 1:
            break

        # skip next frame according to specified skip amount. if sum of current frame number and skip amount is greater than total frame number, skip
        # to the last frame, which will stop execution in next iteration
        if frame_number + skip_amount > frame_count - 1:
            video.set(cv2.CAP_PROP_POS_FRAMES, frame_count - 1)
        else:
            video.set(cv2.CAP_PROP_POS_FRAMES, frame_number + skip_amount)

    video.release()