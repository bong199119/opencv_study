import numpy as np
import cv2

#### np.empty, zeros, ones, full
# img1 = np.empty((240, 320), dtype = np.uint8) #랜덤숫자로 채워짐
# img2 = np.zeros((240, 320, 3), dtype = np.uint8)
# img3 = np.ones((240, 320, 3), dtype = np.uint8)
# img4 = np.full((240, 320), 128, dtype = np.uint8)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.imshow('img4', img4)


#### 레퍼런스
# img1 = cv2.imread(r'D:\project\opencv_study\data\reindeer.jpg')
# img2 = img1
# img3 = img1.copy() #복사본을 새롭게 제작

# img1[:,:] = (0, 255, 255)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)


#### 레퍼런스2
img1 = cv2.imread(r'D:\project\opencv_study\data\reindeer.jpg')

img2 = img1[40:120, 30:150]
img3 = img1[40:120, 30:150].copy() 

img1[:,:] = (0, 255, 255)
img2.fill(0)
cv2.circle(img2, (50,50), 20, (0,0,255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destroyAllWindows()