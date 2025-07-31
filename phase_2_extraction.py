import pytesseract
from PIL import Image

def ocr_extraction(standardized_image_path):
    """Reads text from the document using OCR."""
    try:
        text = pytesseract.image_to_string(Image.open(standardized_image_path))
        return {"raw_text": text}
    except Exception as e:
        print(f"Error during OCR extraction: {e}")
        return {"raw_text": ""}

def identify_document_type(text):
    """Identifies document type based on keywords in the OCR text."""
    text_lower = text.lower()
    if "income tax department" in text_lower and "permanent account number" in text_lower:
        return "PAN Card"
    if "loan application" in text_lower or "interest rate" in text_lower:
        return "Loan Application"
    return "Unknown Document"