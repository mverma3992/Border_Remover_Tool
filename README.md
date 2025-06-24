Border Detection and Removal Tool
A Python-based utility to detect and remove image borders efficiently using OpenCV. This tool is useful for pre-processing scanned documents, datasets, or any images where unwanted borders need to be cropped out cleanly.
Project Structure

detect_borders.py        - Detects borders and logs analysis to CSV
remove_borders.py        - Crops borders based on detection logic
border_report.csv        - Report of detected borders for each image

How It Works
1. detect_borders.py

- Loads all images from a specified folder.
- Converts each image to grayscale.
- Applies edge detection and contour analysis.
- Identifies possible border areas based on color similarity and position.
- Logs findings to border_report.csv.

2. remove_borders.py

- Processes the same images again.
- Uses the border detection logic to crop the unwanted outer areas.
- Saves cleaned images to a separate output directory.

Usage
Step 1: Detect Borders

python detect_borders.py --input_dir path/to/images --output_csv border_report.csv
- --input_dir: Folder containing your input images.
- --output_csv: Name of the CSV file to store detection results.

Step 2: Remove Borders

python remove_borders.py --input_dir path/to/images --output_dir path/to/output
- --input_dir: Same folder of original images.
- --output_dir: Folder where cropped (border-free) images will be saved.

Requirements

- Python 3.13.1
- Required libraries:
    pip install opencv-python
    pip install numpy

Output: border_report.csv

The CSV file contains:
- filename: Name of the image.
- top, bottom, left, right: Pixel values of detected border margins.
- status: Whether a border was successfully detected.

Notes

- Works best with images that have a clear contrast between content and borders.
- You can fine-tune border detection by adjusting thresholds or tolerance levels in the script.
- Supports PNG, JPG, JPEG formats by default.

Author
Mann Verma
