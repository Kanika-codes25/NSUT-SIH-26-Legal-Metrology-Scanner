
````markdown
# Legal Metrology Scanner

A web-based prototype that scans packaged commodity labels and performs automated screening against selected Legal Metrology requirements.

## Problem Statement

**PS Number:** SIH26034

**Problem Statement Title:**

Software System to check compliance of Packaged Commodities under Legal Metrology(Packaged Commodities) Rules, 2011 by scanning products, images and labels.

**Organization:** Ministry of Consumer Affairs, Food & Public Distribution

**Category:** Software

**Theme:** Miscellaneous

## Problem

Manual inspection of packaged commodity labels can be time-consuming and may require checking multiple mandatory declarations.

The proposed system assists in screening product labels by extracting information from product images and checking selected Legal Metrology requirements.

## Proposed Solution

The Legal Metrology Scanner allows a user to upload an image of a packaged commodity.

The system:

1. Extracts text from the product image using OCR.
2. Identifies important product information.
3. Checks selected Legal Metrology requirements.
4. Marks fields as `YES` or `UNCERTAIN`.
5. Generates an overall screening result.
6. Displays the extracted information and compliance results through the frontend.

The system is intended as an automated inspection assistance tool and not as official legal certification.

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
Uncertainty Handling
      ↓
Structured JSON
      ↓
Frontend Result
````

## Key Features

* Product label image upload
* OCR-based text extraction using PaddleOCR
* Automatic product information extraction
* Product name and brand detection
* MRP / retail price detection
* Net quantity detection
* Manufacturing date detection
* Expiry / Best Before detection
* Manufacturer information detection
* Consumer contact detection
* Barcode detection
* Batch number detection
* Legal Metrology compliance screening
* `YES` / `UNCERTAIN` field-level results
* `COMPLIANT` / `REVIEW REQUIRED` overall result
* Explainable screening results
* OCR text display

## Technology Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, FastAPI
* **OCR:** PaddleOCR
* **Information Extraction:** Python Regex / Rule-Based Logic
* **API:** REST API
* **Server:** Uvicorn
* **Deployment:** Render
* **Version Control:** Git, GitHub
* **Development Environment:** VS Code

## Legal Framework

The prototype screens selected declarations based on the **Legal Metrology (Packaged Commodities) Rules, 2011**.

The current screening checks include:

* Commodity / Product Name
* Net Quantity
* Manufacturer Information
* Retail Price / MRP
* Manufacturing Date
* Expiry / Best Before
* Consumer Complaint Contact

## System Architecture

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
                    │ Extraction           │
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

Detailed architecture:

[System Architecture](docs/architecture.md)

Detailed workflow:

[Project Workflow](docs/workflow.md)

## Repository Structure

```text
NSUT-SIH-26-Legal-Metrology-Scanner/
├── README.md
├── SUBMISSION_GUIDE.md
├── submission/
│   ├── PRESENTATION.md
│   ├── DEMO.md
│   └── [Final PPT]
├── src/
│   ├── backend/
│   │   ├── main.py
│   │   ├── ocr.py
│   │   ├── extractor.py
│   │   └── compliance.py
│   └── frontend/
│       └── index.html
├── docs/
│   ├── architecture.md
│   └── workflow.md
├── assets/
│   └── screenshots/
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then install the required dependencies:

```bash
cd NSUT-SIH-26-Legal-Metrology-Scanner
pip install -r requirements.txt
```

## Run

### Backend

```bash
cd src/backend
uvicorn main:app --reload
```

### Frontend

Open the frontend using a local server.

The frontend communicates with the FastAPI backend through the `/upload` endpoint.

## Live Demo

[Legal Metrology Scanner](https://legal-metrology-scanner-3hut.onrender.com)

## Demo Video

[Watch Project Demo](https://drive.google.com/file/d/1S7wW1FfCkXNbtfTe_pjolgadyMNGW1fZ/view?usp=drive_link)

## Project Presentation

[View Project Presentation](submission/YOUR_PPT_FILENAME.pptx)

> Replace `YOUR_PPT_FILENAME.pptx` with the exact name of the PPT file uploaded to the `submission/` folder.

## Screenshots

Project screenshots are available in:

`assets/screenshots/`

## Documentation

* [System Architecture](docs/architecture.md)
* [Project Workflow](docs/workflow.md)
* [Submission Guide](SUBMISSION_GUIDE.md)
* [Demo Details](submission/DEMO.md)
* [Project Presentation](submission/PRESENTATION.md)

## Future Scope

* Improved OCR accuracy for different packaging layouts
* Support for a larger variety of product categories
* Expanded coverage of Legal Metrology rules
* Configurable rule engine for future regulatory updates
* Dedicated barcode / QR code decoding
* Larger product image testing dataset
* Improved validation and confidence scoring
* Better handling of complex packaging layouts

## Innovation

The prototype focuses on:

* **Automated compliance screening** instead of only OCR
* **Product-independent processing** rather than product-specific hardcoding
* **Uncertainty-aware results** to avoid treating OCR failure as definite non-compliance
* **Field-level explainability** showing which declarations were detected
* **End-to-end workflow** from product image to compliance result

## Disclaimer

This tool provides automated screening assistance and is not a substitute for official legal inspection, verification, or certification.

````

