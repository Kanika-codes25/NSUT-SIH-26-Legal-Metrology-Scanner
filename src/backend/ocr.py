import os

os.environ["FLAGS_use_mkldnn"] = "0"
os.environ["FLAGS_enable_pir_api"] = "0"
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"

from paddleocr import PaddleOCR


def get_text(image_path):

    print("Starting OCR...")

    ocr = PaddleOCR(
        text_detection_model_name="PP-OCRv4_mobile_det",
        text_recognition_model_name="en_PP-OCRv4_mobile_rec",
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
        enable_mkldnn=False
    )

    print("OCR initialized!")

    result = ocr.predict(image_path)

    texts = []

    for res in result:
        data = res.json

        if isinstance(data, str):
            import json
            data = json.loads(data)

        rec_texts = data.get("res", {}).get("rec_texts", [])

        texts.extend(rec_texts)

    text = "\n".join(texts)

    print("OCR RESULT:")
    print(text)

    return text
