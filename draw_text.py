import cv2

webcam = cv2.VideoCapture(0)

while True:
    ignore, frame = webcam.read()
    cv2.imshow("Webcam", frame)
    width, heigth = int(webcam.get(3)), int(webcam.get(4))


    font = cv2.FONT_HERSHEY_SIMPLEX  # Set Font
    frame = cv2.putText(frame, "WEBCAM", (0, heigth), font, 2, (0,0,255))
    cv2.imshow("Webcam", frame)


    if cv2.waitKey(1) == ord('q'):
        break

webcam.release
cv2.destroyAllWindows()