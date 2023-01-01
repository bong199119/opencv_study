import cv2
import numpy as np


def on_level_changed(pos):
    global img

    level = pos * 16
    level = np.clip(level, 0, 255)
    img[ : , : ] = level
    cv2.imshow('image', img)
    print(pos)

img = np.zeros((480, 640), dtype = np.uint8)

cv2.imshow('image', img)
cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)
cv2.waitKey()

cv2.destroyAllWindows()