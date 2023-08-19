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


Mediapipe Hand Landmarker returns array of 20 locations for each hand land mark, Marks of interest are WRIST (0), MCP and TIP for each finger, and TIP of thumb.
Idea is to assess finger curl by taking absolute distance from MCP to TIP for each finger. For thumb, will consider distance from thumb TIP to MCP of pinky finger, relative to distance from MCP of index and pinky
