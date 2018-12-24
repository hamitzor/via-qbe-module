import cv2


def extract(frame, options=None):
    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(frame, None)
    return kp, des


def match(des1, des2,options=None):
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)
    return good