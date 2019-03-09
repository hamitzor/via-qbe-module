"""Module contains frame operation methods."""

import cv2


def extract(frame):
    """Extract features from supplied frame.

    Arguments:
      frame {:obj:`numpy.ndarray`} -- Frame to extract features from

    Returns:
      :obj:`tuple` -- A tuple contains of list of key points and descriptors with corresponding indexes, respectively

    """
    sift = cv2.xfeatures2d.SIFT_create()  # pylint: disable=no-member
    kp, des = sift.detectAndCompute(frame, None)
    return kp, des


def match(des1, des2):
    """Match features using flann based matcher.

    Arguments:
      des1 {:obj:`numpy.ndarray`} -- First descriptor to compare
      des2 {:obj:`numpy.ndarray`} -- Second descriptor to compare

    Returns:
      :obj:`list` of :obj:`cv2.DMatch` -- List of good matches

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


def get_homography_points(query_keypoints, train_keypoints, good, image):
    """Find homograpy and return masked points.

    Arguments:
      query_keypoints {:obj:`list` of :obj:`cv2.KeyPoint`} -- Query keypoints
      train_keypoints {:obj:`list` of :obj:`cv2.KeyPoint`} -- Train keypoints
      good {:obj:`list` of :obj:`cv2.DMatch`} -- List of good matches
      image {:obj:`numpy.ndarray`} -- Train frame
    Returns:
      :obj:`tuple` -- Tuple of masked points and mask

    """
    import numpy as np
    # format points from good matches for finding homography
    query_points = np.float32(
        [query_keypoints[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    train_points = np.float32(
        [train_keypoints[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    # find homography using RANSAC algorithm and collect the mask that specifies inliers and outliers
    M, mask = cv2.findHomography(
        query_points, train_points, cv2.RANSAC, 5.0)

    h, w = image.shape
    pts = np.float32(
        [[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
    pts = cv2.perspectiveTransform(pts, M)

    return (pts, mask)
