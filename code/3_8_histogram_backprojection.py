import sys
import numpy as np
import cv2

# path = r'D:\project\opencv_study\Lecture_materials\ch03\cropland.png'
# src = cv2.imread(path)

# x, y, w, h = cv2.selectROI(src)

# src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# crop = src_ycrcb[y:y+h, x:x+w]

# channels = [1, 2]
# cr_bins = 128
# cb_bins = 128
# histsize = [cr_bins, cb_bins]
# cr_range = [0, 256]
# cb_range = [0, 256]
# ranges = cr_range + cb_range

# hist = cv2.calcHist([crop], channels, None, histsize, ranges)
# hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
# dst = cv2.copyTo(src, backproj)

# cv2.imshow('backproj', backproj)
# cv2.imshow('hist_norm', hist_norm)
# cv2.imshow('dst', dst)
# cv2.waitKey()


path_ref = r'D:\project\opencv_study\Lecture_materials\ch03\kids1.png'
path_src = r'D:\project\opencv_study\Lecture_materials\ch03\kids2.png'
path_mask = r'D:\project\opencv_study\Lecture_materials\ch03\kids1_mask.bmp'

ref = cv2.imread(path_ref, cv2.IMREAD_COLOR)
mask = cv2.imread(path_mask, cv2.IMREAD_GRAYSCALE)
ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]
# 영상에서 특정부분의 histogram을 출력하고 싶으면 calcHist에 mask를 넣어주면됨
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, 
                          cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상에 히스토그램 역투영 적용
src = cv2.imread(path_src, cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
dst = cv2.copyTo(src, backproj)

cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
