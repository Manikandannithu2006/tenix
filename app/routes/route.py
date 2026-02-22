# app/routes/route.py

from fastapi import APIRouter, HTTPException
from app.services.inference import run_inference
from app.services.pathfinding import astar
import os
import json

router = APIRouter()

LAST_IMAGE_FILE = "data/last_image.txt"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@router.get("/")
def find_route(start: str, end: str):
    # 1. Check if image exists
    if not os.path.exists(LAST_IMAGE_FILE):
        raise HTTPException(status_code=400, detail="No image uploaded yet")

    # 2. Read last uploaded image
    with open(LAST_IMAGE_FILE, "r") as f:
        image_path = f.read().strip()

    # 3. Run inference
    layout = run_inference(image_path)

    # 4. Build graph
    graph = {}
    for a, b in layout["edges"]:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    # 5. Run pathfinding
    path = astar(graph, start, end)

    result = {
        "start": start,
        "end": end,
        "path": path
    }

    # 6. Save JSON for Unreal / Unity
    with open(f"{OUTPUT_DIR}/route.json", "w") as f:
        json.dump(result, f, indent=2)

    return result