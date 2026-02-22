from fastapi import FastAPI
from app.routes import upload, layout, route

app = FastAPI(title="AI 2D to 3D Walkthrough Backend")

app.include_router(upload.router, prefix="/upload")
app.include_router(layout.router, prefix="/layout")
app.include_router(route.router, prefix="/route")