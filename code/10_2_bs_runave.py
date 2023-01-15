import sys
import numpy as np
import cv2

path_video = r'D:\project\opencv_study\Lecture_materials\ch10\PETS2000.avi'
cap = cv2.VideoCapture(path_video)

# 배경영상 등록
ret, back = cap.read()
back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)
back = cv2.GaussianBlur(back, (0, 0), 1.0)
Fback = back.astype(np.float32)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (0, 0), 1.0)

    cv2.accumulateWeighted(gray, Fback, 0.01) # 현재 프래임과 배경 영상의 가중치 합을 이용해서 배경 영상을 업데이트
    back = Fback.astype(np.uint8)

    diff = cv2.absdiff(gray, back) # 받는인자 두개의 형이 같아야함
    _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    cnt, _, stats, _ = cv2.connectedComponentsWithStats(diff)

    for i in range(1, cnt):
        x, y, w, h, s = stats[i]

        if s < 100:
            continue

        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('diff', diff)
    cv2.imshow('back', back)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
