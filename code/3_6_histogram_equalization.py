import cv2
import os
import numpy as np


# 히스토그램 평활화는 이미지의 대비를 향상시키는 데 사용
# 히스토그램 정규화는 이미지의 다이나믹 레인지(최대, 최소간의 비)를 조정하는 데 사용

# gray스케일 영상 히스토그램 평활화(histogram equalization)
# path = r'D:\project\opencv_study\data\Hawkes.jpg'
# src = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# dst = cv2.equalizeHist(src)

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()


# 컬러 영상 히스토그램 평활화
# 컬러는 RGB를 각각 평활화 하면 색감이 달라짐
# 따라서, Ycrcb공간으로 바꾸고 Y값만 평활화를 해주면 됨.
# Y -> 밝기정보
# cr, cb -> 색상정보
path = r'D:\project\opencv_study\data\field.bmp'

src = cv2.imread(path)
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
planes = cv2.split(src_ycrcb)
array_planes = np.array(planes)
array_planes[0] = cv2.equalizeHist(planes[0])
dst_ycrcb = cv2.merge(array_planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()