import cv2

webcam = cv2.VideoCapture(0)
x = 0
while True:
    ignore, frame = webcam.read()
    width = int(webcam.get(3))
    heigth = int(webcam.get(4))

    center = (int(width/2), int(heigth/2))  # Must be tuple and integers to work for all webcams
    
    frame = cv2.rectangle(frame, (0, 0), (width, heigth), (0,0,255), 10)
    frame = cv2.circle(frame, center, 80, (255,0,0), 10)
    frame = cv2.circle(frame, center, 80, (0,0,255), -1)  # -1 will fill the shape ()
    
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()

cv2.destroyAllWindows()