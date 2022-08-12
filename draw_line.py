import cv2

webcam = cv2.VideoCapture(0)

while True:
    ignore, frame = webcam.read()
    width = int(webcam.get(3))  # Get the Width return float
    height = int(webcam.get(4))  # Get the width return float

    frame = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)  # Coordinates must be Int
    frame = cv2.line(frame, (width,0), (0, height), (0,0,255), 10)
    cv2.imshow("Webcam",frame)

    if cv2.waitKey(1) == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()