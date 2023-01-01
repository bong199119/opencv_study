import sys
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

path = r'D:\project\opencv_study\Lecture_materials\ch03'
path_img = os.path.join(path, 'lenna256.bmp')
path_img2 = os.path.join(path, 'square.bmp')

src1 = cv2.imread(path_img, cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread(path_img2, cv2.IMREAD_GRAYSCALE)

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0) # 5번째 인자 -> gamma: 결과 영상에 추가적으로 더할 값
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2) #  정적 배경 차분 방법

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()