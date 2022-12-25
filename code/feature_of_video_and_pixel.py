import cv2

img1 = cv2.imread(r'D:\project\opencv_study\data\reindeer.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'D:\project\opencv_study\data\reindeer.jpg', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('ok')
    sys.exit()

print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)

h, w = img1.shape
print(f'w x h = {w} x {h}')

h, w, c = img2.shape
print(f'w x h = {w} x {h}')
print(h, w, c)

'''
for y in range(h):
    for x in range(w):
        img1[y, x] = 0
        img2[y, x] = (0, 255, 255)
'''

img1[:,:] = 0
img2[:,:] = (0, 255, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey()

cv2.destroyAllWindows()