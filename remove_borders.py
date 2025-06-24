import cv2
import numpy as np
import os
import csv

def crop_image(image, top, bottom, left, right):
    h, w = image.shape[:2]
    return image[top:h - bottom, left:w - right]

input_dir = 'input'
output_dir = 'output'
report_file = 'border_report.csv'

os.makedirs(output_dir, exist_ok=True)

with open(report_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        fname = row['Filename']
        top = int(row['Top'])
        bottom = int(row['Bottom'])
        left = int(row['Left'])
        right = int(row['Right'])

        path = os.path.join(input_dir, fname)
        img = cv2.imread(path)

        if img is not None:
            cropped = crop_image(img, top, bottom, left, right)
            cv2.imwrite(os.path.join(output_dir, fname), cropped)
