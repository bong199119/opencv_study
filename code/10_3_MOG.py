# mog : mixture of gaussian 
# gmm : gaussian mixture model
# 둘은 같은의미로 많이 쓰임

import sys
import numpy as np
import cv2


path_video = r'D:\project\opencv_study\Lecture_materials\ch10\PETS2000.avi'
cap = cv2.VideoCapture(path_video)

# 배경차분 알고리즘 객체 생성
bs = cv2.createBackgroundSubtractorMOG2()
# bs = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = bs.apply(gray)
    back = bs.getBackgroundImage()

    cnt, _, stats, _ = cv2.connectedComponentsWithStats(fgmask)

    for i in range(1, cnt):
        x, y, w, h, s = stats[i]

        if s < 100:
            continue

        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('back', back)
    cv2.imshow('fgmask', fgmask)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()