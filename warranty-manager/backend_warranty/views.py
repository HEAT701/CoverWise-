'''
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
from warranty_app.models import Warranty
from pdf2image import convert_from_path
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render
import os
import json
from django.http import JsonResponse
import re
import pytesseract
from django.utils.dateparse import parse_date
# ✅ Safe way to set pytesseract command
TESSERACT_PATH = getattr(settings, "TESSERACT_CMD", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def read_qr_from_image(image_path):
    img = cv2.imread(image_path)
    qr_codes = decode(img)
    qr_texts = []
    for qr in qr_codes:
        data = qr.data.decode("utf-8")
        qr_texts.append(data)
    return qr_texts

def extract_text_ocr(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def find_expiry_date(text):
    match = re.search(r'(\d{4}-\d{2}-\d{2})', text)
    if match:
        return match.group(1)
    return None

@csrf_exempt
def upload_warranty(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        ext = file.name.split(".")[-1].lower()

        save_dir = os.path.join(settings.MEDIA_ROOT, "warranty_cards")
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, file.name)

        with open(save_path, "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

        extracted_text = ""

        if ext == "pdf":
            pages = convert_from_path(save_path)
            for i, page in enumerate(pages):
                img_path = f"{save_path}_page_{i}.png"
                page.save(img_path, "PNG")
                qr_data_list = read_qr_from_image(img_path)
                if qr_data_list:
                    extracted_text = qr_data_list[0]
                    break
                else:
                    extracted_text = extract_text_ocr(img_path)
                    if extracted_text.strip():
                        break
        else:
            qr_data_list = read_qr_from_image(save_path)
            if qr_data_list:
                extracted_text = qr_data_list[0]
            else:
                extracted_text = extract_text_ocr(save_path)

        if not extracted_text:
            return JsonResponse({"error": "No data found in QR or OCR"}, status=404)

        # 📝 Extract specific fields
        product_name = find_field(extracted_text, r'Product[:\- ]?([A-Za-z0-9 ]+)')
        model = find_field(extracted_text, r'Model[:\- ]?([A-Za-z0-9 ]+)')
        product_id = find_field(extracted_text, r'Product ID[:\- ]?([A-Za-z0-9 ]+)')

        expiry_date = find_expiry_date(extracted_text)

        # Save to DB
        Warranty.objects.create(
            user_id=request.user,
            product_name=product_name or "Unknown",
            product_id=model or "Unknown",
            expiry_date=parse_date(expiry_date) if expiry_date else None,
            qr_data=extracted_text,
            warranty_image=file
        )

        return JsonResponse({
            'Product ID': product_id,
            "Product Name": product_name,
            "model": model,
            "expiry_date": expiry_date
        })

    return JsonResponse({"error": "No file uploaded"}, status=400)


def find_field(text, pattern):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None
'''