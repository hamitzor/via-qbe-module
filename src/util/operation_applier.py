"""Module contains a method for applying operations to videoso"""

import cv2
from .logger import Logger


def apply(video_cap, total_frame, fps, skip_amount=5, operation=lambda x, y: None, begin=0, end=None, info_function=lambda x: None, info_skip_amount=3):
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
      skip_amount {int} -- Number of iterations to skip before calling info function again
    """

    logger = Logger("/var/log/via/qbe")

    if begin > total_frame/fps:
        begin = total_frame/fps

    if end is None:
        end = total_frame/fps

    if end > total_frame/fps:
        end = total_frame/fps

    # forward to specified time in terms of fps.
    current_frame_no = begin * fps + 1

    iteration_count = 0

    temp_results = []

    while True:
        # if it has reached the specified ending second or last frame, break.

        if current_frame_no > end * fps or current_frame_no > total_frame:
            break
        frame = None
        if video_cap is not None:
            video_cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame_no)
            _, frame = video_cap.read()

        result = operation(current_frame_no, frame)
        if result is not None:
            temp_results.append(result)

        # call info function with progress percentage
        if (iteration_count % (info_skip_amount + 1) is 0):
            percentage = round((current_frame_no - begin*fps) /
                               (end*fps - begin*fps), 2) * 100
            if percentage > 2:
                percentage = percentage - 1
            info_function(percentage, temp_results)
            temp_results = []

        current_frame_no = current_frame_no + skip_amount + 1
        iteration_count = iteration_count + 1

    info_function(100, [])
    if video_cap is not None:
        video_cap.release()
