import os
import io
import pytesseract
import boto3
import fastapi
import uvicorn
import shutil
from fastapi import FastAPI, UploadFile, File
from pdf2image import convert_from_bytes
from googleapiclient.discovery import build
from google.oauth2 import service_account
from transformers import pipeline

# Initialize FastAPI
app = FastAPI()

# S3 Configuration
AWS_ACCESS_KEY = "your-access-key"
AWS_SECRET_KEY = "your-secret-key"
AWS_BUCKET_NAME = "your-bucket-name"
s3_client = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

# GDrive API Configuration
SERVICE_ACCOUNT_FILE = "path/to/your/service-account.json"
SCOPES = ["https://www.googleapis.com/auth/drive"]
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build("drive", "v3", credentials=creds)

# Summarization Model
summarizer = pipeline("summarization")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Uploads file to AWS S3 and extracts text."""
    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    s3_client.upload_file(file_path, AWS_BUCKET_NAME, file.filename)
    extracted_text = extract_text_from_pdf(file_path)
    os.remove(file_path)
    
    return {"filename": file.filename, "text": extracted_text}

@app.post("/summarize")
def summarize_text(text: str):
    """Summarizes extracted text."""
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return {"summary": summary[0]['summary_text']}

def extract_text_from_pdf(pdf_path):
    """Extracts text using Tesseract OCR from PDF."""
    images = convert_from_bytes(open(pdf_path, 'rb').read())
    extracted_text = ""
    for img in images:
        extracted_text += pytesseract.image_to_string(img)
    return extracted_text

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
