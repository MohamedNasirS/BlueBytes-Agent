import cv2
from PIL import Image
import os

OUTPUT_DIR = "processed_images"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def standardize_document(image_path):
    """Converts any image into a standard, high-quality PNG format."""
    try:
        img = Image.open(image_path).convert("RGB")
        standardized_path = os.path.join(OUTPUT_DIR, os.path.basename(image_path).split('.')[0] + '.png')
        img.save(standardized_path, 'PNG')
        print(f"Standardized '{image_path}' to '{standardized_path}'")
        return standardized_path
    except Exception as e:
        print(f"Error standardizing {image_path}: {e}")
        return None

def check_image_quality(image_path):
    """Performs a basic blur check."""
    try:
        image = cv2.imread(image_path)
        if image is None:
            return False, 0
        
        laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
        if laplacian_var < 100:
            return False, laplacian_var
        else:
            return True, laplacian_var
    except Exception as e:
        print(f"Error in quality check for {image_path}: {e}")
        return False, 0