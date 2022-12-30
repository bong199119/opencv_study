import os
import sys
import cv2
import numpy as np

img = np.full((400, 400, 3), 255, np.uint8)

cv2.line(img, (50, 50), (200, 50), (0,255,0), 5)
cv2.line(img, (70, 220), (180, 280), (0, 0, 128))

cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

cv2.circle(img, (300, 100), 90, (0, 255, 255), 3, cv2.LINE_8) # LINE_8이 기본
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA) # LINE_AA를 사용하면 경계가 부드러워짐
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

pts = np.array([[250, 200],[300, 200],[350, 300],[250,300]])
pts1 = np.array([[150, 100],[200, 100],[250, 200],[150,200]])
cv2.polylines(img, [pts, pts1], True, (255, 0, 255), 2) # 3번째인자 : 폐곡선 여부

text = 'opencv version : ' + cv2.__version__
cv2.putText(img, text, (50, 350) , cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()

