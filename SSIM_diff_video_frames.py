#!/usr/bin/env python3

"""
Calculates structural similarity index (SSIM) between frames of a video, and saves the difference between frames as images for easy visual check (and sometimes flags).

If the SSIM score is very close to 1, the differences are likely compression artifacts or noise. If the score is significantly less than 1, it means there are substantial differences between the frames.
"""

import cv2
import numpy as np
import glob
from skimage.metrics import structural_similarity as ssim

# Get a sorted list of all frame filenames
frames = sorted(glob.glob('frame_*.png'))

previous_frame = None

for i, frame_filename in enumerate(frames):
    current_frame = cv2.imread(frame_filename)
    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    if previous_frame is not None:
        
        # Compute SSIM, print and save a visual diff between the two frames
        score = ssim(previous_frame, current_frame_gray)
        if score < 1:
            print(f'{frame_filename}: SSIM {score}')
            diff = cv2.absdiff(previous_frame, current_frame_gray)
            diff_normalized = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)
            cv2.imwrite(f'diff_{i:04}.png', diff_normalized)

    previous_frame = current_frame_gray
