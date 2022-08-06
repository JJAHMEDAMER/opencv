import cv2
import random

img = cv2.imread("img.jpg")
img = cv2.resize(img,(0,0),fx = 0.5, fy = 0.5)

x, y, z = img.shape
print(x,y)
for i in range(x):
    for j in range(y):
        img[i][j] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

cv2.imshow("win", img)


cv2.waitKey(0)
cv2.destroyAllWindows()