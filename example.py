#!/usr/bin/env python

import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Define the text to be displayed
TEXT = "Counting Time!"
font_scale = 4
font_thickness = 8
font_color = (0, 0, 255)  # Red color in BGR format
# Get the size of the text
text_size = cv2.getTextSize(TEXT, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]

# For webcam input:
cap = cv2.VideoCapture(0)

# Calculate the position to place the text at the top of the screen
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
text_x = (width - text_size[0]) // 2
text_y = text_size[1] + 10  # Some padding from the top

def is_finger_pinch(results):
    """pinchy pinchy"""
    # Get the coordinates of the landmarks
    landmarks = results.multi_hand_landmarks[0].landmark
    # Get the tip of the index finger
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    # Get the tip of the thumb
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    # Get the distance between the two tips
    distance = np.sqrt((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)
    # Use the distance to determine if the finger is extended
    if distance > 0.05:
        return 1
    else:
        return 0

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:  
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.putText(cv2.flip(image, 1), TEXT, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()