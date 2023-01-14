# 명암비(contrast)

import cv2
import numpy as np


def getGrayHistImage(hist):
    histimage_width = 256
    histimage_height = 100

    imgHist = np.full((histimage_height, histimage_width), 255, dtype = np.uint8)
    
    histMax = np.max(hist)
    for x in range(histimage_width):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x,0] * 100 / histMax))
        cv2.line(imgHist, pt1,  pt2, 0)

    return imgHist

# path = r'D:\project\opencv_study\data\lenna.bmp'
# src = cv2.imread(path, cv2.IMREAD_COLOR)
# src = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# alpha = 1.0
# dst = np.clip((1 + alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()

# histogram stretching (명암비 자동 조절)
path = r'D:\project\opencv_study\data\Hawkes.jpg'
src = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 아래는 함수 설명
# normalize(src, dst, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=None, mask=None)
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

# 4번째 인자 : histsize는 histtogram의 bins를 나타냄 막대의 개수로 보면됨.
# cv2.calcHist -> 0~255사이의 값의 분포를 반환함
hist = cv2.calcHist([src], [0], None, [256], [0, 256]) 
histImg = getGrayHistImage(hist)

hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])
histImg2 = getGrayHistImage(hist2)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('histImg', histImg)
cv2.imshow('histImg2', histImg2)
cv2.waitKey()

# min-max normalize 공식
# ( (f(x,y) - Gmin) / (Gmax - Gmin) ) * 255

gmin = np.min(src)
gmax = np.max(src)

dst = np.clip((src - gmin) * 255. / (gmax - gmin), 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('histImg', histImg)
cv2.imshow('histImg2', histImg2)
cv2.waitKey()
