import cv2

webcam = cv2.VideoCapture(0)

'''
    1. Every loop the window overwrite the prevues window
    because all the window has the same title
    
    2. The Windows will be picture 
    because they are not updated
    
    3. cv2.destroyAllWindows Will close all the windows 
'''

x = 0
while True:
    x = x + 1
    ignore, frame = webcam.read()

    cv2.imshow("Webcam", frame)

    cv2.imshow(f"Webcam{x}", frame)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()

cv2.destroyAllWindows()