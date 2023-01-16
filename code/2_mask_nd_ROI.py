import os 
import sys
import cv2

path_img = r'D:\project\opencv_study\Lecture_materials\ch02\airplane.bmp'
path_mask = r'D:\project\opencv_study\Lecture_materials\ch02\mask_plane.bmp'
path_grass = r'D:\project\opencv_study\Lecture_materials\ch02\field.bmp'

src = cv2.imread(path_img, cv2.IMREAD_COLOR)
# cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다.
# src = cv2.imread(path_img, cv2.IMREAD_UNCHANGED)
mask = cv2.imread(path_mask, cv2.IMREAD_GRAYSCALE)
dst = cv2.imread(path_grass, cv2.IMREAD_COLOR)

# cv2.copyTo(src, mask, dst)

# src에서 mask부분을 따서 return. mask이외의 부분의 값은 0(검정)
dst = cv2.copyTo(src, mask)

# boolean indexing
# dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()

cv2.destroyAllWindows()


# ### 알파체널을 이용해 합성
# src = cv2.imread(path_img, cv2.IMREAD_UNCHANGED)
# mask = src[:, :, -1]
# src = src[:, :, 0:3]
# dst = cv2.imread(path_grass, cv2.IMREAD_COLOR)

# h, w = src.shape[:2]
# crop = dst[0:h, 0:w]
# cv2.copyTo(src, mask, crop) 

# # src에서 mask부분을 따서 return. mask이외의 부분의 값은 0(검정)
# # dst = cv2.copyTo(src, mask)

# # boolean indexing
# dst[mask > 0] = src[mask > 0]

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('mask', mask)

# cv2.waitKey()
# cv2.destroyAllWindows()