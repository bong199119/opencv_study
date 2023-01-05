import cv2

path = r'D:\project\opencv_study\data\reindeer.jpg'

im_color = cv2.imread(path, cv2.IMREAD_COLOR)

im_b, im_g, im_r  = cv2.split(im_color)

cv2.imshow('b', im_b)
cv2.imshow('g', im_g)
cv2.imshow('r', im_r)

cv2.waitKey(0)

cv2.destroyAllWindows()