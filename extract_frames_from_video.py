#!/usr/bin/env python3

# Extracts and saves all frames from video.

import cv2

cap = cv2.VideoCapture('/path/to/video.mp4')

if not cap.isOpened(): 
    print("Error opening file")

frame_num = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f'frame_{frame_num:04}.png', frame)
        frame_num += 1
    else:
        break

cap.release()

print("Frame extraction is complete.")