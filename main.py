import cv2

img = cv2.imread("img.png")
img = cv2.resize(img,(0,0),fx = 0.1, fy = 0.1)

img = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("win", img)

cv2.waitKey(0)
cv2.destroyAllWindows()