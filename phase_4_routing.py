# phase_4_routing.py
# Implements Phase 4: Automated Eligibility Triage & Routing 

def apply_rules_engine(verified_data):
    """
    Evaluates verified data against specific scheme eligibility criteria. [cite: 27]
    """
    print("\n--- Applying Rules Engine ---")
    # Example for Land Purchase Scheme [cite: 28]
    # This is a simplified rules engine.
    
    applicant_income = verified_data.get("income", 150000) # example income
    is_target_community = verified_data.get("community", "SC") # example community

    rules_passed = True
    reasons = []

    # Rule 1: Income check
    if applicant_income > 120000:
        rules_passed = False
        reasons.append("Income is too high")
    
    # Rule 2: Community check
    if is_target_community != "SC":
        rules_passed = False
        reasons.append("Not from the target community")

    print(f"Eligibility Check Passed: {rules_passed}. Reasons: {reasons}")
    return rules_passed, reasons


def execute_final_action(all_checks_passed, reasons):
    """
    Executes a final action based on the results of the rules engine. [cite: 29]
    """
    print("\n--- Executing Final Action ---")
    if all_checks_passed:
        # Fast-track the application if everything is clear. [cite: 29]
        print("ACTION: Auto-Clear for Committee Review. [cite: 29]")
        return "Auto-Cleared"
    else:
        # Check for specific failure reasons
        if "Income is too high" in reasons or "Not from the target community" in reasons:
            # Place in a queue for final human verification if likely ineligible. [cite: 32]
            print("ACTION: Flag as Likely Ineligible for final human verification. [cite: 32]")
            return "Likely Ineligible"
        else:
            # Route to an officer for complex discrepancies. [cite: 31]
            print("ACTION: Flag for Manual Review due to complex discrepancies. [cite: 31]")
            return "Manual Review"