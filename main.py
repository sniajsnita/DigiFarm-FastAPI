from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

# CORS supaya React Expo bisa akses langsung kalau perlu
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model load SEKALI saat startup — sudah benar, pertahankan ini
model = YOLO("best.pt")

@app.get("/")
def home():
    return {"message": "YOLO FastAPI running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    
    # Resize dulu kalau gambar terlalu besar — ini yang bikin lama
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    # YOLO butuh max 640px, resize kalau lebih besar
    max_size = 640
    if max(image.size) > max_size:
        image.thumbnail((max_size, max_size), Image.LANCZOS)

    results = model(image, verbose=False)  # verbose=False kurangi log noise

    detections = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            detections.append({
                "class": model.names[cls_id],
                "confidence": round(conf, 4),
                "bbox": [round(x, 2) for x in box.xyxy[0].tolist()]
            })

    return {
        "status": "success",
        "detections": detections
    }