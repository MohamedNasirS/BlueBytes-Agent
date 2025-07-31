# phase_1_ingestion.py
# Implements Phase 1: Automated Ingestion & Pre-processing 

import cv2
from PIL import Image
import os

# Define output directory for processed images
OUTPUT_DIR = "processed_images"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def standardize_document(image_path):
    """
    Converts any image into a standard, high-quality PNG format. [cite: 8]
    """
    try:
        img = Image.open(image_path)
        standardized_path = os.path.join(OUTPUT_DIR, os.path.basename(image_path).split('.')[0] + '.png')
        img.save(standardized_path, 'PNG')
        print(f"Standardized '{image_path}' to '{standardized_path}'")
        return standardized_path
    except Exception as e:
        print(f"Error standardizing {image_path}: {e}")
        return None

def check_image_quality(image_path):
    """
    Performs a real-time analysis to detect issues like blurriness. [cite: 9]
    This is a basic blur check.
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Could not read image for quality check: {image_path}")
        return False, 0

    # Calculate the variance of the Laplacian to detect blur
    laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
    print(f"Image: {image_path}, Laplacian Variance: {laplacian_var}")

    # A low variance suggests a blurry image. The threshold may need tuning.
    if laplacian_var < 100:
        print(f"Quality Insufficient: Image '{image_path}' is likely blurry. [cite: 10]")
        return False, laplacian_var
    else:
        print(f"Quality Sufficient: Image '{image_path}' is clear enough.")
        return True, laplacian_var