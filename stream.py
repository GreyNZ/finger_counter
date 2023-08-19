#!/usr/bin/env python

import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 indicates the default webcam

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the frame
    cv2.imshow("Video Stream", frame)

    # Check for user input to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
