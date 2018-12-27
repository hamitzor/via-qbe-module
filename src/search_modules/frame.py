import cv2
import numpy as np


def extract(frame):
    """Extracts sift features
            Args:
                frame (:obj:`numpy.ndarray`): Frame to extract features from.
            Returns:
                :obj:`tuple`: A tuple consist of list of key points and descriptors with corresponding indexes, respectively
            """
    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(frame, None)
    return kp, des


def match(des1, des2):
    """Matches features using flann based matcher
                Args:
                    des1 (:obj:`numpy.ndarray`): First descriptor to compare
                    des2 (:obj:`numpy.ndarray`): Second descriptor to compare
                Returns:
                    :obj:`list` of :obj:`cv2.DMatch`: List of good matches
                """
    flann_index_kdtree = 0
    index_params = dict(algorithm=flann_index_kdtree, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)
    return good
