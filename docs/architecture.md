# System Architecture

## Overview

The Legal Metrology Scanner is a web-based prototype that extracts information from a packaged commodity image and performs automated screening against selected Legal Metrology requirements.

## Architecture

```text
                    ┌──────────────────────┐
                    │        User          │
                    │    Product Image     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Frontend        │
                    │    HTML / CSS / JS   │
                    └──────────┬───────────┘
                               │
                         POST /upload
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │       Backend        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      PaddleOCR       │
                    │    Text Extraction   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Information          │
                    │ Extraction            │
                    │ Regex / Rule Based   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Compliance Engine   │
                    │   Legal Metrology    │
                    │  Requirement Checks  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Structured JSON    │
                    │ Product + Compliance │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Frontend Result    │
                    │       Display        │
                    └──────────────────────┘
```
## Components

### 1. Frontend

The frontend is developed using HTML, CSS and JavaScript.

It provides:

- Product image upload
- Scan button
- Processing/loading status
- Extracted product information
- Compliance results
- OCR extracted text
- Disclaimer for automated screening

The frontend sends the uploaded image to the backend using the Fetch API.

### 2. Backend

The backend is developed using Python and FastAPI.

The `/upload` API:

1. Receives the uploaded image.
2. Temporarily saves the image.
3. Sends the image to the OCR module.
4. Passes the extracted text to the information extraction module.
5. Sends the extracted fields to the compliance engine.
6. Returns the complete result as JSON.

### 3. OCR Module

PaddleOCR is used to extract text from the uploaded product image.

The OCR module processes the image and returns the detected text, which is then used by the information extraction module.

### 4. Information Extraction

The extracted OCR text is processed using Python regular expressions and rule-based logic.

The system attempts to identify:

- Product Name
- Brand
- Net Quantity
- MRP / Price
- Batch Number
- Manufacturing Date
- Expiry / Best Before
- Barcode
- Manufacturer
- Consumer Contact
- Ingredients

### 5. Compliance Engine

The compliance engine checks whether selected required product declarations were detected.

The current checks include:

- Commodity / Product Name
- Net Quantity
- Manufacturer
- Retail Price / MRP
- Manufacturing Date
- Expiry / Best Before
- Consumer Complaint Contact

Each check produces one of two statuses:

- `YES` — required information was detected.
- `UNCERTAIN` — information could not be reliably detected.

### 6. Overall Result

The system counts the successful and uncertain checks.

If all required checks are detected:

`COMPLIANT`

If one or more checks are uncertain:

`REVIEW REQUIRED`

This approach avoids treating an OCR failure as a definite legal non-compliance and instead indicates that manual review may be required.

### 7. JSON Response

The backend returns a structured JSON response containing:

- OCR extracted text
- Product information
- Compliance results
- Overall compliance status
- Number of detected checks
- Number of checks requiring review

### 8. Deployment

The backend API is deployed on Render.

The frontend communicates with the deployed FastAPI backend through the `/upload` REST endpoint.
