from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "data/samples"
LAST_IMAGE_FILE = "data/last_image.txt"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_plan(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔹 store last uploaded image path
    with open(LAST_IMAGE_FILE, "w") as f:
        f.write(file_path)

    return {
        "message": "Floor plan uploaded successfully",
        "file_path": file_path
    }