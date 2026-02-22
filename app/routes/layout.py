# app/routes/layout.py

from fastapi import APIRouter, HTTPException
from app.services.inference import run_inference
import os
import json

router = APIRouter()   # ✅ THIS WAS MISSING

LAST_IMAGE_FILE = "data/last_image.txt"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@router.get("/")
def get_layout():
    if not os.path.exists(LAST_IMAGE_FILE):
        raise HTTPException(status_code=400, detail="No image uploaded yet")

    with open(LAST_IMAGE_FILE, "r") as f:
        image_path = f.read().strip()

    layout = run_inference(image_path)

    # save layout json for Unreal / Unity
    with open(f"{OUTPUT_DIR}/layout.json", "w") as f:
        json.dump(layout, f, indent=2)

    return {"layout": layout}