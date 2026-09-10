def check_compliance(data):

    checks = {}

    # 1. Commodity / Product name
    if data.get("product_name"):
        checks["product_name"] = {
            "status": "YES",
            "message": "Commodity name detected."
        }
    else:
        checks["product_name"] = {
            "status": "UNCERTAIN",
            "message": "Commodity name could not be reliably detected."
        }

    # 2. Net quantity
    if data.get("net_quantity"):
        checks["net_quantity"] = {
            "status": "YES",
            "message": f"Net quantity detected: {data['net_quantity']}"
        }
    else:
        checks["net_quantity"] = {
            "status": "UNCERTAIN",
            "message": "Net quantity could not be reliably detected."
        }

    # 3. Manufacturer
    if data.get("manufacturer"):
        checks["manufacturer"] = {
            "status": "YES",
            "message": "Manufacturer information detected."
        }
    else:
        checks["manufacturer"] = {
            "status": "UNCERTAIN",
            "message": "Manufacturer information could not be reliably detected."
        }

    # 4. Retail price / MRP
    if data.get("price"):
        checks["retail_price"] = {
            "status": "YES",
            "message": f"Retail price detected: ₹{data['price']}"
        }
    else:
        checks["retail_price"] = {
            "status": "UNCERTAIN",
            "message": "MRP could not be reliably read. Manual verification required."
        }

    # 5. Manufacturing date
    if data.get("manufacturing_date"):
        checks["manufacturing_date"] = {
            "status": "YES",
            "message": f"Manufacturing date detected: {data['manufacturing_date']}"
        }
    else:
        checks["manufacturing_date"] = {
            "status": "UNCERTAIN",
            "message": "Manufacturing date could not be reliably read."
        }

    # 6. Expiry / Best Before
    if data.get("expiry"):
        checks["expiry_or_best_before"] = {
            "status": "YES",
            "message": f"Expiry/Best Before detected: {data['expiry']}"
        }
    else:
        checks["expiry_or_best_before"] = {
            "status": "UNCERTAIN",
            "message": "Expiry/Best Before could not be reliably detected."
        }

    # 7. Consumer complaint contact
    if data.get("consumer_contact"):
        checks["consumer_contact"] = {
            "status": "YES",
            "message": "Consumer complaint contact information detected."
        }
    else:
        checks["consumer_contact"] = {
            "status": "UNCERTAIN",
            "message": "Consumer complaint contact information could not be reliably detected."
        }

    # ---------------- OVERALL RESULT ----------------

    yes_count = sum(
        1
        for check in checks.values()
        if check["status"] == "YES"
    )

    uncertain_count = sum(
        1
        for check in checks.values()
        if check["status"] == "UNCERTAIN"
    )

    if uncertain_count == 0:
        overall_status = "COMPLIANT"
    else:
        overall_status = "REVIEW REQUIRED"

    return {
        "overall_status": overall_status,
        "checks_passed": yes_count,
        "checks_uncertain": uncertain_count,
        "checks": checks
    }
