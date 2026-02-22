# app/services/inference.py

from PIL import Image
import os

def run_inference(image_path: str):
    """
    Simulated AI inference based on image dimensions.
    Acts as a lightweight stand-in for a trained floorplan model.
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image not found")

    img = Image.open(image_path)
    width, height = img.size

    # Dynamically decide number of rooms
    if width * height < 500_000:
        rooms = ["A", "B", "C"]
    else:
        rooms = ["A", "B", "C", "D"]

    # Generate room centers (normalized)
    room_centers = {}
    step_x = width // (len(rooms) + 1)
    step_y = height // (len(rooms) + 1)

    for i, room in enumerate(rooms):
        room_centers[room] = (
            (i + 1) * step_x // 100,
            (i + 1) * step_y // 100
        )

    # Build adjacency (simulated corridor connectivity)
    edges = []
    for i in range(len(rooms) - 1):
        edges.append((rooms[i], rooms[i + 1]))

    return {
        "image_size": {
            "width": width,
            "height": height
        },
        "rooms": room_centers,
        "edges": edges,
        "note": "Layout generated via lightweight AI inference (prototype deployment)"
    }