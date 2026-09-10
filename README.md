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
