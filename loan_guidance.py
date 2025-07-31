import re

CRITICAL_KEYWORDS = [
    "interest rate", "late payment", "late fee", "prepayment penalty",
    "terms and conditions", "collateral", "default", "arbitration"
]

def analyze_loan_application(text):
    """Analyzes text from OCR to find critical sections and action items."""
    guidance = {
        "critical_sections": set(),
        "action_items": []
    }
    
    lower_text = text.lower()
    
    for keyword in CRITICAL_KEYWORDS:
        if keyword in lower_text:
            guidance["critical_sections"].add(keyword.title())
            
    matches = re.findall(r"submit by (\w+\s\d{1,2},\s\d{4})", lower_text)
    for date in matches:
        guidance["action_items"].append(f"Application submission deadline found: {date}")
        
    return guidance