import cv2
import sys
import numpy as np

img = np.ones((480, 480, 3), dtype = np.uint8) * 255

oldx = oldy = -1
def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print(f'EVENT_LBUTTONDOWN : {x}, {y}')
    elif event == cv2.EVENT_LBUTTONUP:
        print(f'EVENT_LBUTTONUP : {x}, {y}')
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON: # flags는 event와 함께 활용되는 역할로 특수한 상태를 확인하는 용도입니다.
            print(f'EVENT_MOUSEMOVE : {x}, {y}')
            # cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 5, cv2.LINE_AA)
            cv2.imshow('image', img) # 업데이트
            oldx, oldy = x, y

cv2.imshow('image', img)
cv2.setMouseCallback('image', on_mouse)
cv2.waitKey()

cv2.destroyAllWindows()