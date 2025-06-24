import cv2
import numpy as np
import os
import csv

def detect_borders(image):
    h, w, _ = image.shape
    tolerance = 15
    max_scan = min(h, w) // 4

    def is_similar(c1, c2):
        return np.linalg.norm(np.array(c1) - np.array(c2)) < tolerance

    top, bottom, left, right = 0, 0, 0, 0
    top_left = image[0, 0]
    top_right = image[0, -1]
    bottom_left = image[-1, 0]
    bottom_right = image[-1, -1]

    for y in range(max_scan):
        if all(is_similar(image[y, x], top_left) for x in range(w)):
            top += 1
        else:
            break

    for y in range(h - 1, h - max_scan, -1):
        if all(is_similar(image[y, x], bottom_left) for x in range(w)):
            bottom += 1
        else:
            break

    for x in range(max_scan):
        if all(is_similar(image[y, x], top_left) for y in range(h)):
            left += 1
        else:
            break

    for x in range(w - 1, w - max_scan, -1):
        if all(is_similar(image[y, x], top_right) for y in range(h)):
            right += 1
        else:
            break

    sides = []
    if top > 0: sides.append("top")
    if bottom > 0: sides.append("bottom")
    if left > 0: sides.append("left")
    if right > 0: sides.append("right")

    return top, bottom, left, right, ', '.join(sides)

input_dir = 'input'
output_csv = 'border_report.csv'

os.makedirs(input_dir, exist_ok=True)

with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Filename', 'Top', 'Bottom', 'Left', 'Right', 'Detected Borders'])

    for fname in os.listdir(input_dir):
        if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            path = os.path.join(input_dir, fname)
            img = cv2.imread(path)
            top, bottom, left, right, sides = detect_borders(img)
            writer.writerow([fname, top, bottom, left, right, sides])
