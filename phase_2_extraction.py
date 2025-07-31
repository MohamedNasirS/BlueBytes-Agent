# phase_2_extraction.py
# Implements Phase 2: Parallel Information Extraction

import pytesseract
from pyzbar.pyzbar import decode
from PIL import Image
import pandas as pd

# You need to have Tesseract installed on your system for this to work
# For Windows: https://github.com/tesseract-ocr/tessdoc
# For Mac/Linux: use brew install tesseract or sudo apt-get install tesseract-ocr

def ocr_extraction(standardized_image_path):
    """
    Reads and extracts key text fields from the document using OCR. [cite: 13]
    """
    try:
        text = pytesseract.image_to_string(Image.open(standardized_image_path))
        print(f"\n--- OCR Extracted Text from '{standardized_image_path}' ---")
        print(text)
        print("--------------------------------------------------")
        # In a real application, you would parse this text to find specific fields.
        return {"raw_text": text}
    except Exception as e:
        print(f"Error during OCR extraction: {e}")
        return {"raw_text": ""}

def qr_code_validation(standardized_image_path):
    """
    Scans for QR codes or barcodes present on the certificates. [cite: 14]
    """
    try:
        decoded_objects = decode(Image.open(standardized_image_path))
        if not decoded_objects:
            print("No QR code or barcode found.")
            return None

        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            print(f"Found QR Code. Data: {qr_data}")
            # The agent would then cross-verify these details against government databases. [cite: 15]
            return qr_data
        return None
    except Exception as e:
        print(f"Error during QR code validation: {e}")
        return None


def cross_reference_data(form_data, ocr_data):
    """
    Compares data from OCR with applicant's form data. [cite: 16]
    Any mismatch is immediately flagged. [cite: 17]
    """
    print("\n--- Cross-Referencing Data ---")
    mismatches = []
    # This is a simplified example.
    if 'name' in form_data and 'name' in ocr_data:
        if form_data['name'].lower() not in ocr_data['raw_text'].lower():
            mismatches.append("Name mismatch")
            print("FLAG: Name mismatch detected. [cite: 17]")

    if not mismatches:
        print("Data cross-referencing successful. No mismatches found.")

    return mismatches