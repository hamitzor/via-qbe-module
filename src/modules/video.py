"""Module contains methods for video operations."""

import cv2


def apply(video_cap, total_frame, fps, skip_amount=5, operation=lambda x, y: None, begin=0, end=2147483646, info_function=lambda x: None):
    """Extract frames and apply specified operation on them.

    This function extracts the specified video into frames, converts those frames to gray color and exclusively initiates given operation
    function with two parameters, frame and frame number.

    Arguments:
      video_cap {:obj:`cv2.VideoCapture`} -- Video capture to be used. If it is supplied, operation will be invoked with frame along with frame number
      total_frame {float} -- Total frame number of video
      fps {float} -- FPS value of video

    Keyword Arguments:
      skip_amount {int} -- Number of frames to skip before processing next frame
      operation {:obj:`function`} -- Operation function to be applied on frames (default: {lambda x, y: None})
      begin {int} -- First second to process (default: {0})
      end {int} -- Last second to process(Included) (default: {2147483646})
      info_function {:obj:`function`} -- The function to be used for inform purposes. An integer between 0 and 100 that specifies progress is supplied to this function (default: {lambda x, y: None})

    """

    # forward to specified time in terms of fps.
    current_frame_no = begin * fps + 1

    while True:
        # if it has reached the specified ending second or last frame, break.

        if current_frame_no > end * fps or current_frame_no > total_frame:
            break
        frame = None
        if video_cap is not None:
            video_cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame_no)
            _, frame = video_cap.read()

        operation(
            current_frame_no,
            frame
        )

        # call info function with progress percentage
        info_function(round(current_frame_no / total_frame, 2) * 100)

        current_frame_no = current_frame_no + skip_amount + 1

    if video_cap is not None:
        video_cap.release()
