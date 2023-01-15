import numpy as np
import cv2

path_video = r'D:\project\opencv_study\Lecture_materials\ch10\PETS2000.avi'
cap = cv2.VideoCapture(path_video)

_, back = cap.read()
back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
# 잡음을 가우시안 블러로 잡고 차영상 구하는방법 사용
# 다른방법으로는 차영상에 threshold를 주고 morphology 연산을 취할 수 있음. 강의에서는 전자를 사용
back = cv2.GaussianBlur(back, (0, 0), 1) 

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (0, 0), 1) 

    diff = cv2.absdiff(back, frame)
    _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    cv2.imshow('frame', frame)
    cv2.imshow('diff', diff)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllwindows()