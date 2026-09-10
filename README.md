# Legal Metrology Scanner

A web-based prototype that scans packaged commodity labels and performs automated screening against selected Legal Metrology requirements.

## Problem

Manual verification of packaged product labels can be time-consuming and error-prone. Important declarations such as MRP, net quantity, manufacturer details and dates need to be checked during inspection.

## Solution

The Legal Metrology Scanner uses OCR and rule-based information extraction to identify important product declarations from a product image and screen them against selected Legal Metrology requirements.

## Workflow

```text
Product Image
      ↓
    OCR
      ↓
Information Extraction
      ↓
Compliance Screening
      ↓
Structured JSON
      ↓
Frontend Result
```

## Key Features

- Product label image upload
- OCR-based text extraction using PaddleOCR
- Automatic extraction of product information
- MRP and net quantity detection
- Manufacturing and expiry date detection
- Manufacturer and consumer contact detection
- Barcode and batch number detection
- Legal Metrology compliance screening
- `YES` / `UNCERTAIN` field-level results
- `COMPLIANT` / `REVIEW REQUIRED` overall result
- Explainable screening results

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **OCR:** PaddleOCR
- **API:** REST API
- **Server:** Uvicorn
- **Deployment:** Render
- **Version Control:** Git, GitHub

## Legal Framework

The prototype screens selected declarations based on the **Legal Metrology (Packaged Commodities) Rules, 2011**.

## Live Demo

[Legal Metrology Scanner](https://legal-metrology-scanner-3hut.onrender.com)

## Documentation

- [System Architecture](docs/architecture.md)
- [Project Workflow](docs/workflow.md)

## Disclaimer

This tool provides automated screening assistance and is not a substitute for official legal inspection or certification.
