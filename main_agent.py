import phase_1_ingestion
import phase_2_extraction
import phase_3_analysis
import loan_guidance

def process_document_batch(file_paths):
    """
    Processes a list of uploaded documents, identifies each one,
    and runs the correct analysis.
    """
    results = []

    for file_path in file_paths:
        print(f"--- Processing: {file_path} ---")
        
        # Ingestion and OCR
        is_quality_ok, _ = phase_1_ingestion.check_image_quality(file_path)
        if not is_quality_ok:
            results.append({"file": file_path, "type": "Unknown", "status": "Rejected", "summary": "Image quality is too poor."})
            continue
            
        standardized_doc_path = phase_1_ingestion.standardize_document(file_path)
        ocr_data = phase_2_extraction.ocr_extraction(standardized_doc_path)
        
        # Identify document type
        doc_type = phase_2_extraction.identify_document_type(ocr_data.get("raw_text", ""))
        
        # --- Dispatch to appropriate workflow based on type ---
        if doc_type == "PAN Card":
            is_genuine = phase_3_analysis.predict_authenticity(standardized_doc_path)
            status = "Verified" if is_genuine else "Manual Review"
            summary = "PAN Card appears authentic." if is_genuine else "PAN Card failed authenticity check."
            results.append({"file": file_path, "type": doc_type, "status": status, "summary": summary})
            
        elif doc_type == "Loan Application":
            is_genuine = phase_3_analysis.predict_authenticity(standardized_doc_path)
            guidance = loan_guidance.analyze_loan_application(ocr_data.get("raw_text", ""))
            status = "Analysis Complete"
            summary = "Loan application analyzed."
            results.append({"file": file_path, "type": doc_type, "status": status, "summary": summary, "guidance": guidance})

        else:
            results.append({"file": file_path, "type": doc_type, "status": "Unknown", "summary": "Could not identify the document type."})

    return results