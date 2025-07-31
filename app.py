import streamlit as st
from main_agent import process_document_batch
import os
import fitz  # PyMuPDF

UPLOADS_DIR = "uploads"
os.makedirs(UPLOADS_DIR, exist_ok=True)

# --- Web App UI ---
st.title("🤖 AI Multi-Document Processor")
st.write("Upload all your documents (e.g., PAN Card, Loan Application) at once.")

# Allow multiple files to be uploaded
uploaded_files = st.file_uploader(
    "Choose documents...",
    type=["jpg", "png", "pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    saved_file_paths = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOADS_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        saved_file_paths.append(file_path)

    st.success(f"{len(uploaded_files)} document(s) uploaded successfully!")

    if st.button("Process All Documents"):
        with st.spinner("Agent is analyzing all documents..."):
            # Process the entire batch of file paths
            all_results = process_document_batch(saved_file_paths)

            st.write("---")
            st.header("Analysis Report")

            for result in all_results:
                # Use an expander for each document's result
                with st.expander(f"**{os.path.basename(result['file'])}** | Type: {result['type']}"):
                    
                    # Display Verification Status
                    if result['status'] == "Verified" or result['status'] == "Analysis Complete":
                        st.success(f"**Status:** {result['status']}")
                    else:
                        st.warning(f"**Status:** {result['status']}")
                    
                    st.write(f"**Summary:** {result['summary']}")
                    
                    # Display Loan Guidance if it exists
                    guidance = result.get('guidance')
                    if guidance and (guidance["critical_sections"] or guidance["action_items"]):
                        st.write("---")
                        st.markdown("##### Loan Guidance")
                        if guidance["critical_sections"]:
                            st.info(f"**⚠️ Critical Sections:** {', '.join(guidance['critical_sections'])}")
                        if guidance["action_items"]:
                            for item in guidance["action_items"]:
                                st.info(f"**✅ Action Item:** {item}")