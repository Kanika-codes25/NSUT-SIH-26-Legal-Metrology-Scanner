# Project Workflow

## Step 1: Image Upload

The user uploads an image of a product package or label through the frontend.

## Step 2: Image Processing

The uploaded image is temporarily processed by the backend for text extraction.

## Step 3: OCR

PaddleOCR detects and extracts visible text from the product image.

## Step 4: Information Extraction

The extracted OCR text is analyzed to identify important product and manufacturer information.

The system extracts fields such as:

- Product Name
- Brand
- Manufacturer
- Net Quantity
- MRP
- Batch Number
- Manufacturing Date
- Expiry / Best Before
- Consumer Contact
- Barcode

## Step 5: Compliance Screening

The extracted information is checked against selected requirements of the Legal Metrology (Packaged Commodities) Rules, 2011.

## Step 6: Uncertainty Handling

If a required field cannot be reliably detected, the system marks it as `UNCERTAIN` instead of incorrectly declaring the product non-compliant.

Possible field-level outcomes include:

- `YES`
- `UNCERTAIN`

## Step 7: Final Result

The system generates an overall result:

- `COMPLIANT` — required information was detected.
- `REVIEW REQUIRED` — one or more required fields could not be reliably verified.

## Step 8: Result Display

The structured JSON response is sent back to the frontend and displayed to the user along with the extracted information and compliance results.

## Complete Flow

Image Upload  
→ OCR  
→ Information Extraction  
→ Compliance Screening  
→ Uncertainty Handling  
→ JSON Response  
→ Frontend Display
