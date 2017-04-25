# Requirements:
#     pip install numpy
#     sudo apt-get install python-openCV

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = cap.read()
 return im

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    image = get_image();
    file = "";
    cv2.imwrite(file, image);

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
