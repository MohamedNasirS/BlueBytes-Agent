# 🧠 AI Document Verification & Guidance Agent

An autonomous AI agent that automates **document verification** and **application guidance**, built for intelligent processing of documents like PAN cards and loan applications. Designed originally for the **Dr. B.R. Ambedkar Development Corporation Ltd. (ADCL)**, this system combines **AI-powered forgery detection** and **automated assistance** through a simple web interface.

---

## 🚀 Features

- **📄 Multi-Document Processing**  
  Upload and analyze multiple documents (e.g., PAN cards, loan forms) simultaneously.

- **🔍 AI-Powered Verification**  
  A custom-trained neural network checks for forgery or tampering in uploaded documents.

- **📌 Automated Application Guidance**  
  The system reads and highlights key content in application forms—such as critical deadlines or missing details.

- **🌐 Interactive Web Interface**  
  Built with **Streamlit**, the UI allows users to upload documents and view results in real time.

---

## ⚙️ Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)  
  Ensure it is installed and added to your system's PATH.

---

## 🛠️ Installation

### Step 1: Clone the Repository

```bash
git https://github.com/MohamedNasirS/BlueBytes-Agent.git
cd <your-repository-folder>
```

### Step 2: Set Up a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- **Windows:**
  ```bash
  .\.venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source .venv/bin/activate
  ```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 How to Run the Agent

### 🔹 Step 1: Prepare Template

Place a clean, blank image of a **PAN card** in the root directory and name it:

```text
pan_card_template.png
```

---

### 🔹 Step 2: Generate Dataset and Train Model

Generate synthetic data:

```bash
python generate_dataset.py
```

Train the model:

```bash
python train_model.py
```

This will save a trained model as `document_verifier.keras`.

---

### 🔹 Step 3: Launch the Web App

Run the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and go to:

```text
http://localhost:8501
```

You're ready to upload and verify documents!

---

## 📁 Project Structure

```
├── app.py
├── generate_dataset.py
├── train_model.py
├── requirements.txt
├── pan_card_template.png
├── dataset/ (auto-generated)
└── document_verifier.keras (trained model)
```

---

## 🧑‍💼 Use Case

This agent can be adapted for any institution requiring secure document validation, such as:

- Financial institutions verifying loan applications
- Government agencies validating citizen documents
- Educational institutions managing form submissions

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

Inspired by real-world needs of ADCL and designed with social impact in mind.
