# AnaDoc - Cloud-Based Document Analyzer

AnaDoc is a cloud-powered intelligent document analyzer that extracts and summarizes key insights from scanned PDFs using **OCR (Tesseract)** and **NLP (Hugging Face Transformers)**. It integrates with **AWS S3** and **Google Drive** for seamless cloud storage and retrieval.

## 🚀 Key Features
- **OCR Processing**: Extracts text from PDFs using Tesseract OCR.
- **AI Summarization**: Generates concise summaries using NLP.
- **Cloud Storage Integration**: Supports AWS S3 & Google Drive.
- **FastAPI Backend**: Provides a scalable and efficient API.

## 📌 Value Addition
- Unlike traditional OCR tools, AnaDoc enables **distributed cloud processing**, making it ideal for large-scale document analysis.
- **Automates document insights**, reducing manual effort.
- Easily **deployable & extensible** with additional AI features.

---

## 🔧 Setup Guide

### 1️⃣ Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install fastapi uvicorn boto3 pytesseract pdf2image google-auth google-auth-oauthlib transformers
```

### 2️⃣ Set Up Credentials

#### 🔹 AWS S3 Configuration
Replace the placeholders in `main.py` with your **AWS S3** credentials:
```python
AWS_ACCESS_KEY = "your-access-key"
AWS_SECRET_KEY = "your-secret-key"
AWS_BUCKET_NAME = "your-bucket-name"
```

#### 🔹 Google Drive API Configuration
Download your **Google Service Account JSON** file and update:
```python
SERVICE_ACCOUNT_FILE = "path/to/your/service-account.json"
```

### 3️⃣ Run the Server
Start the FastAPI app with:
```bash
uvicorn main:app --reload
```
The server will be available at `http://127.0.0.1:8000`.

### 4️⃣ API Usage

#### 📝 Upload and Extract Text from a PDF
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/upload' \
  -F 'file=@your-document.pdf'
```
_Response:_
```json
{
    "filename": "your-document.pdf",
    "text": "Extracted text from the PDF..."
}
```

#### ✂️ Summarize Extracted Text
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/summarize' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Long extracted text here..."}'
```
_Response:_
```json
{
    "summary": "Concise summary of the text..."
}
```

---

## 🎯 Ready to Use!
AnaDoc is now fully functional. Customize it further by adding **text categorization, metadata extraction, or keyword analysis**. Happy coding! 🚀

