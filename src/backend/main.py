from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from ocr import get_text
from extractor import extract_fields
from compliance import check_compliance


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://legal-metrology-scanner-3hut.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Legal Metrology Scanner API is running"
    }


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    image_path = os.path.join(
    os.path.dirname(__file__),
    "uploaded_image.jpg"
)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = get_text(image_path)

    data = extract_fields(text)

    compliance = check_compliance(data)

    return {
        "message": "Image processed successfully",
        "filename": file.filename,
        "ocr_text": text,
        "product": data,
        "compliance": compliance
    }
