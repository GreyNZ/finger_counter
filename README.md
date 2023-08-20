# finger_counter
finger mafs

playing around with mediapipe to make a finger counting game

# Dependancies
Python 3.11
conda create --name hands python=3.11
Mediapipe Hand Landmarker https://developers.google.com/mediapipe/solutions/vision/hand_landmarker#models

# Concept
Demo of open-source ML CV
Users present a number of fingers, displays number of fingers total.

# Method
Mediapipe Hand Landmarker returns array of 20 locations for each hand land mark, Marks of interest are WRIST (0), MCP and TIP for each finger, and TIP of thumb.
Finger curls are assesed by comparing geometric mean of 3D vectors from wrist to both MCP and TIP for each finger.

# TODO
Change thumb to consider distance from thumb TIP to pinky MCP, relative to distance from MCP of index and pinky, comparitively. May not be needed.
