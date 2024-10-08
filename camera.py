import cv2
from threshholding import *

# Open the default camera (usually the webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert the frame to grayscale
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    tresh = thresholding(image)



    # Display the resulting frame
    cv2.imshow('actual', frame)
    cv2.imshow('frame', image)
    cv2.imshow('tresh', tresh)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
