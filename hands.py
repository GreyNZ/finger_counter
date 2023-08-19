#!/usr/bin/env python

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'hand_landmarks.task'

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 indicates the default webcam

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# video
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a hand landmarker instance with the video mode:
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.VIDEO)
with HandLandmarker.create_from_options(options) as landmarker:
    # Process video frames one by one, until the video is completed.

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame
        # cv2.imshow("Video Stream", frame)

        results = landmarker.process(frame)
        annotated_image = frame.copy()
        mp.solutions.drawing_utils.draw_landmarks(
            annotated_image, results.multi_hand_landmarks[0],
            mp.solutions.hands.HAND_CONNECTIONS)
        cv2.imshow('MediaPipe Hands', annotated_image)

        # Check for user input to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()




if __name__ == "__main__":
    print("nope")