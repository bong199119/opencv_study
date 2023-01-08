import cv2
import os
import numpy as np

# rgb는 컬러추출에 적합하지 않는 경우가 있음

# path = r'D:\project\opencv_study\data\candies2.png'

# src = cv2.imread(path)
# src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
# dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()


# color extract with trackbar
path = r'D:\project\opencv_study\data\candies2.png'
src = cv2.imread(path)
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'dst')
    hmax = cv2.getTrackbarPos('H_max', 'dst')

    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')

cv2.createTrackbar('H_min', 'dst', 50, 179, on_trackbar)
cv2.createTrackbar('H_max', 'dst', 80, 179, on_trackbar)
on_trackbar(0)

cv2.waitKey(0)