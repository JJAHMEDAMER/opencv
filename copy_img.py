import cv2

img = cv2.imread("img.jpg")
img = cv2.resize(img, (0,0), fx = 0.5, fy= 0.5)

cv2.imshow("win",img)
print(img.shape)

img[0:100, 0:100] = img[250:350, 250:350] 
cv2.imshow("win",img)

cv2.waitKey(0)
cv2.destroyAllWindows
