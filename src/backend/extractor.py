import re


def extract_fields(text):

    data = {
        "product_name": None,
        "brand": None,
        "price": None,
        "net_quantity": None,
        "ingredients": None,
        "expiry": None,
        "manufacturing_date": None,
        "batch_number": None,
        "barcode": None,
        "manufacturer": None,
        "consumer_contact": None
    }

    lines = [x.strip() for x in text.splitlines() if x.strip()]
    clean_text = "\n".join(lines)

    # =========================================================
    # NET QUANTITY
    # =========================================================

    quantity = re.search(
        r"\b(\d+(?:\.\d+)?)\s*"
        r"(g|gm|grams?|kg|ml|millilit(?:re|er)s?|l|lit(?:re|er)s?)\b",
        clean_text,
        re.IGNORECASE
    )

    if quantity:
        data["net_quantity"] = (
            quantity.group(1) + " " + quantity.group(2)
        )


    # =========================================================
    # MRP / PRICE
    # =========================================================

    price = re.search(
        r"MRP\s*[₹Rs.INR\s:;\-]*"
        r"(\d+(?:[.,]\d{1,2})?)",
        clean_text,
        re.IGNORECASE
    )

    if price:
        data["price"] = price.group(1)


    # =========================================================
    # MANUFACTURING DATE
    # =========================================================

    mfg = re.search(
        r"(?:MFG|MFD|MFG\.?\s*DATE|MFD\.?\s*DATE|"
        r"MANUFACTURED(?:\s*DATE)?|DATE\s*OF\s*MANUFACTURE)"
        r"\s*[:\-]?\s*"
        r"([0-3]?\d[/-][01]?\d[/-]\d{2,4}|"
        r"[01]?\d[/-]\d{2,4}|"
        r"\d{4}[/-][01]?\d(?:[/-][0-3]?\d)?)",
        clean_text,
        re.IGNORECASE
    )

    if mfg:
        data["manufacturing_date"] = mfg.group(1)


    # =========================================================
    # EXPIRY
    # =========================================================

    expiry = re.search(
        r"(?:EXP|EXP\.|EXPIRY|EXPIRY\s*DATE|"
        r"BEST\s*BEFORE|USE\s*BY|USE\s*BEFORE)"
        r"\s*[:\-]?\s*"
        r"([0-3]?\d[/-][01]?\d[/-]\d{2,4}|"
        r"[01]?\d[/-]\d{2,4}|"
        r"\d{4}[/-]\d{1,2}(?:[/-]\d{1,2})?)",
        clean_text,
        re.IGNORECASE
    )

    if expiry:
        data["expiry"] = expiry.group(1)


    # =========================================================
    # BATCH NUMBER
    # =========================================================

    batch = re.search(
        r"(?:BATCH|LOT)\s*(?:NO\.?|NUMBER)?"
        r"\s*[:\-]\s*([A-Z0-9][A-Z0-9/-]{3,})",
        clean_text,
        re.IGNORECASE
    )

    if batch:
        value = batch.group(1)

        invalid = {
            "MFG",
            "MFD",
            "DATE",
            "EXP",
            "EXPIRY",
            "MRP",
            "USP"
        }

        if value.upper() not in invalid:
            data["batch_number"] = value


    # =========================================================
    # BARCODE
    # =========================================================

    numbers = re.findall(r"\b\d{8,14}\b", clean_text)

    for number in numbers:

        # Ignore common phone/toll-free numbers
        if number.startswith(("1800", "800")):
            continue

        data["barcode"] = number
        break


    # =========================================================
    # BRAND
    # =========================================================

    # Strong signal: short all-capital line
    for line in lines:

        cleaned = re.sub(r"[^A-Za-z ]", "", line).strip()

        if (
            2 <= len(cleaned.split()) <= 3
            and cleaned
            and cleaned.upper() == cleaned
            and not re.search(
                r"(NET|BATCH|MRP|MFG|EXPIRY|DATE|"
                r"LIMITED|INDUSTRIES|MANUFACTURED)",
                cleaned,
                re.IGNORECASE
            )
        ):
            data["brand"] = cleaned
            break


    # =========================================================
    # PRODUCT NAME
    # =========================================================

    # Look for a short natural-language line.
    # Avoid addresses, company names and legal information.

    blocked = re.compile(
        r"(manufactured|formerly|limited|industries|"
        r"road|haridwar|uttarakhand|maharashtra|"
        r"consumer|contact|email|visit|toll|"
        r"mrp|batch|mfg|mfd|expiry|quantity|"
        r"lic|license|patanjali foods|"
        r"soya industries)",
        re.IGNORECASE
    )

    for line in lines:

        words = line.split()

        if not (1 <= len(words) <= 5):
            continue

        if blocked.search(line):
            continue

        if re.search(r"\d", line):
            continue

        # Ignore obvious labels
        if line.endswith(":"):
            continue

        # Product-like line
        if (
            len(line) >= 4
            and not re.fullmatch(r"[\W_]+", line)
            and line.lower() not in {
                "net quantity",
                "batch no",
                "mfg date",
                "expiry date",
                "mrp",
                "usp"
            }
        ):
            data["product_name"] = line
            break


    # =========================================================
    # MANUFACTURER
    # =========================================================

    # OCR can scramble the text after "Manufactured By".
    # Therefore, don't blindly take the entire following block.

    manufacturer_candidates = []

    for line in lines:

        if re.search(
            r"\b(limited|ltd\.?|industries)\b",
            line,
            re.IGNORECASE
        ):
            if not re.search(
                r"(email|toll free|consumer|visit us)",
                line,
                re.IGNORECASE
            ):
                manufacturer_candidates.append(line)

    if manufacturer_candidates:
        data["manufacturer"] = manufacturer_candidates[0]


    # =========================================================
    # CONSUMER CONTACT
    # =========================================================

    contact_parts = []

    # Phone / toll-free
    phone = re.search(
        r"(?:Toll\s*Free|Phone|Contact|Call)"
        r"[^0-9]{0,20}"
        r"(\d{7,14})",
        clean_text,
        re.IGNORECASE
    )

    if phone:
        contact_parts.append("Phone: " + phone.group(1))

    # Email
    email = re.search(
        r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
        clean_text
    )

    if email:
        contact_parts.append("Email: " + email.group(0))

    if contact_parts:
        data["consumer_contact"] = ", ".join(contact_parts)


    return data
