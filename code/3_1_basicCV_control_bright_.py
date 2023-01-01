import sys
import numpy as np
import cv2
import os

# grayscale
# path = r'D:\project\opencv_study\Lecture_materials\ch03'
# path_img = os.path.join(path, 'lenna.bmp')

# src = cv2.imread(path_img, cv2.IMREAD_GRAYSCALE)
# dst = cv2.add(src, 100)
# #dst = np.clip(src + 100., 0, 255).astype(np.uint8)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()


# color
path = r'D:\project\opencv_study\Lecture_materials\ch03'
path_img = os.path.join(path, 'lenna.bmp')

src = cv2.imread(path_img)
dst = cv2.add(src, (100, 100, 100, 0))
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()