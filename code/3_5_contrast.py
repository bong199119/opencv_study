# 명암비(contrast)

import cv2
import numpy as np

path = r'D:\project\opencv_study\data\lenna.bmp'
src = cv2.imread(path, cv2.IMREAD_COLOR)
src = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

alpha = 1.0
dst = np.clip((1 + alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()


# histogram stretching (명암비 자동 조절)
