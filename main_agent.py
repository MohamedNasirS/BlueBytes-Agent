# main_agent.py
# Main script to run the autonomous AI verification agent workflow. [cite: 1]

import phase_1_ingestion
import phase_2_extraction
import phase_3_analysis
import phase_4_routing

# --- CONFIGURATION ---
DOCUMENT_TO_PROCESS = "uploads/image.png"
DOCUMENT_TEMPLATE = "templates/image.png"

# Mock applicant data that would be submitted with the form [cite: 16]
APPLICANT_FORM_DATA = {
    "name": "John Doe",
    "income": 150000,
    "community": "SC"
}

def run_agent():
    """
    Executes the sequential pipeline of tasks automatically. 
    """
    print("Blueprint for an Autonomous AI Verification Agent for ADCL")
    print("========================================================\n")

    # --- Phase 1: Ingestion & Pre-processing ---
    print("### STARTING PHASE 1: INGESTION & PRE-PROCESSING ### ")
    is_quality_ok, score = phase_1_ingestion.check_image_quality(DOCUMENT_TO_PROCESS)
    if not is_quality_ok:
        print("\nWorkflow Halted. Applicant must re-upload a clearer copy. [cite: 10]")
        return
    
    standardized_doc_path = phase_1_ingestion.standardize_document(DOCUMENT_TO_PROCESS)
    if not standardized_doc_path:
        print("\nWorkflow Halted due to standardization failure.")
        return
    
    # --- Phase 2: Information Extraction ---
    print("\n### STARTING PHASE 2: PARALLEL INFORMATION EXTRACTION ###")
    ocr_data = phase_2_extraction.ocr_extraction(standardized_doc_path)
    qr_data = phase_2_extraction.qr_code_validation(standardized_doc_path)
    mismatches = phase_2_extraction.cross_reference_data(APPLICANT_FORM_DATA, ocr_data)

    # --- Phase 3: Authenticity & Fraud Analysis ---
    print("\n### STARTING PHASE 3: AUTOMATED AUTHENTICITY & FRAUD ANALYSIS ### ")
    is_authentic_template, _ = phase_3_analysis.template_matching(standardized_doc_path, DOCUMENT_TEMPLATE)
    is_genuine = phase_3_analysis.forensic_analysis(standardized_doc_path)

    # --- Phase 4: Eligibility Triage & Routing ---
    print("\n### STARTING PHASE 4: AUTOMATED ELIGIBILITY TRIAGE & ROUTING ### ")
    
    # Synthesize all findings to make a decision
    all_checks_passed = (
        is_authentic_template and 
        is_genuine and 
        len(mismatches) == 0
    )

    # For this example, we assume eligibility check is the final step
    # A real system might flag for manual review before this
    if all_checks_passed:
        rules_passed, reasons = phase_4_routing.apply_rules_engine(APPLICANT_FORM_DATA)
        final_status = phase_4_routing.execute_final_action(rules_passed, reasons)
    else:
        # If any authenticity checks fail, flag for manual review immediately [cite: 31]
        print("\n--- Executing Final Action ---")
        print("ACTION: Flag for Manual Review due to failed authenticity checks. [cite: 31]")
        final_status = "Manual Review"

    print(f"\n--- WORKFLOW COMPLETE ---")
    print(f"Final Application Status: {final_status}")


if __name__ == "__main__":
    run_agent()