#!/usr/bin/env python

import numpy as np
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

DIST_FACTOR = 1.5   # Threshold for 3D vector mean comparison as a factor of TIP vs MCP


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
text_x = abs((width - text_size[0]) // 2)
text_y = text_size[1] + 10  # Some padding from the top

def is_finger_pinch(results):           # Deprecated
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
    if distance < 0.05:
        return "0"
    else:
        return f"{distance:.2f}"

def count_fingers(results):
    """county county"""
    thumb = is_thumb_extended(results)
    index = is_index_extended(results)
    middle = is_middle_extended(results)
    ring = is_ring_extended(results)
    pinky = is_pinky_extended(results)
    count = sum([thumb, index, middle, ring, pinky])
    return count

def is_thumb_extended(results):
    """thumby thumby"""
    # Get the coordinates of the landmarks
    landmarks = results.multi_hand_landmarks[0].landmark
    # Get the tip of the thumb
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    # Get the tip of the thumb
    mcp = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    # Get the distance between tip and mcp
    distance = np.sqrt((thumb_tip.x - mcp.x)**2 + (thumb_tip.y - mcp.y)**2)
    # Use the distance to determine if the finger is extended
    if distance < 0.06:
        return 0
    else:
        return 1

def is_index_extended(results):
    """pointy pointy"""
    # Get the coordinates of the landmarks
    landmarks = results.multi_hand_landmarks[0].landmark
    # Get the wrist
    wrist = landmarks[mp_hands.HandLandmark.WRIST]
    # Get the tip of the ring finger
    tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    # Get the pinger MCP
    mcp = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    # Get the distance between wrist and tip
    dist_wrist_tip = np.sqrt((tip.x - wrist.x)**2 + (tip.y - wrist.y)**2 + (tip.z - wrist.z)**2)
    # Get the distance between wrist and mcp
    dist_wrist_mcp = np.sqrt((mcp.x - wrist.x)**2 + (mcp.y - wrist.y)**2 + (mcp.z - wrist.z)**2)
    # Use the distance to determine if the finger is extended
    distance_factor = dist_wrist_tip / dist_wrist_mcp
    if distance_factor < DIST_FACTOR:
        return 0
    else:
        return 1

def is_middle_extended(results):
    """flippy flippy"""
    # Get the coordinates of the landmarks
    landmarks = results.multi_hand_landmarks[0].landmark
    # Get the wrist
    wrist = landmarks[mp_hands.HandLandmark.WRIST]
    # Get the tip of the ring finger
    tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    # Get the pinger MCP
    mcp = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
    # Get the distance between wrist and tip
    dist_wrist_tip = np.sqrt((tip.x - wrist.x)**2 + (tip.y - wrist.y)**2 + (tip.z - wrist.z)**2)
    # Get the distance between wrist and mcp
    dist_wrist_mcp = np.sqrt((mcp.x - wrist.x)**2 + (mcp.y - wrist.y)**2 + (mcp.z - wrist.z)**2)
    # Use the distance to determine if the finger is extended
    distance_factor = dist_wrist_tip / dist_wrist_mcp
    if distance_factor < DIST_FACTOR:
        return 0
    else:
        return 1

def is_ring_extended(results):
    """ringy ringy"""
    # Get the coordinates of the landmarks
    landmarks = results.multi_hand_landmarks[0].landmark
    # Get the wrist
    wrist = landmarks[mp_hands.HandLandmark.WRIST]
    # Get the tip of the ring finger
    tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    # Get the pinger MCP
    mcp = landmarks[mp_hands.HandLandmark.RING_FINGER_MCP]
    # Get the distance between wrist and tip
    dist_wrist_tip = np.sqrt((tip.x - wrist.x)**2 + (tip.y - wrist.y)**2 + (tip.z - wrist.z)**2)
    # Get the distance between wrist and mcp
    dist_wrist_mcp = np.sqrt((mcp.x - wrist.x)**2 + (mcp.y - wrist.y)**2 + (mcp.z - wrist.z)**2)
    # Use the distance to determine if the finger is extended
    distance_factor = dist_wrist_tip / dist_wrist_mcp
    if distance_factor < DIST_FACTOR:
        return 0
    else:
        return 1
    

def is_pinky_extended(results):
    """pinky pinky"""
    # Get the coordinates of the landmarks
    landmarks = results.multi_hand_landmarks[0].landmark
    # Get the wrist
    wrist = landmarks[mp_hands.HandLandmark.WRIST]
    # Get the tip of the ring finger
    tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    # Get the pinger MCP
    mcp = landmarks[mp_hands.HandLandmark.PINKY_MCP]
    # Get the distance between wrist and tip
    dist_wrist_tip = np.sqrt((tip.x - wrist.x)**2 + (tip.y - wrist.y)**2 + (tip.z - wrist.z)**2)
    # Get the distance between wrist and mcp
    dist_wrist_mcp = np.sqrt((mcp.x - wrist.x)**2 + (mcp.y - wrist.y)**2 + (mcp.z - wrist.z)**2)
    # Use the distance to determine if the finger is extended
    distance_factor = dist_wrist_tip / dist_wrist_mcp
    if distance_factor < DIST_FACTOR:
        return 0
    else:
        return 1

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

    pingers = 0

    if results.multi_hand_landmarks:
        #print(len(results.multi_hand_landmarks))
        #print(f"{results.multi_hand_landmarks=}")
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
            pingers += count_fingers(results)
        #TEXT = is_finger_pinch(results)
    TEXT = str(pingers)
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.putText(cv2.flip(image, 1), TEXT, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness))
    if cv2.waitKey(5) & 0xFF == 27:
      break

cap.release()