#!/usr/bin/env python

import cv2
import numpy as np

# Create a blank image canvas
canvas_height = 480
canvas_width = 640
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# Define the text to be displayed
text = "Hello, OpenCV!"
font_scale = 1
font_thickness = 2
font_color = (0, 0, 255)  # Red color in BGR format

# Get the size of the text
text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]

# Calculate the position to place the text at the top of the screen
text_x = (canvas_width - text_size[0]) // 2
text_y = text_size[1] + 10  # Some padding from the top

# Add the red text to the image
cv2.putText(canvas, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness)

# Display the image
cv2.imshow("Red Text at Top", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
