import cv2


def extract(frame, options=None):
    sift = cv2.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(frame, None)
    return kp, des


def match(des1, des2):
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    return good
