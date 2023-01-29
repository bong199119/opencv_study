import sys
import numpy as np
import cv2

path = r'D:\project\opencv_study\Lecture_materials\ch07\rice.png'
path = r'D:\project\opencv_study\Lecture_materials\ch08\circuit.bmp'
src = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("otsu's threshold:", th)  # 131

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
