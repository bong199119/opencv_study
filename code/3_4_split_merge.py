import cv2
import numpy as np

path = r'D:\project\opencv_study\data\candies.png'

im_color = cv2.imread(path, cv2.IMREAD_COLOR)

im_b, im_g, im_r  = cv2.split(im_color)

cv2.imshow('b', im_b)
cv2.imshow('g', im_g)
cv2.imshow('r', im_r)

cv2.waitKey(0)

cv2.destroyAllWindows()

zeros = np.zeros((im_b.shape[0],im_b.shape[1]), dtype = 'uint8')
img_b = cv2.merge([im_b, zeros, zeros])
img_g = cv2.merge([zeros, im_g, zeros])
img_r = cv2.merge([zeros, zeros, im_r])

cv2.imshow('b', img_b)
cv2.imshow('g', img_g)
cv2.imshow('r', img_r)

cv2.waitKey(0)

cv2.destroyAllWindows()

img_color = cv2.merge([im_b, im_g, im_r])

cv2.imshow('color', img_color)

cv2.waitKey(0)

cv2.destroyAllWindows()

# 참고 (RGB to gray)
# Y = 0.299R + 0.587G + 0.114B