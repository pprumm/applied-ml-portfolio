from pathlib import Path
from tempfile import NamedTemporaryFile
from collections import defaultdict

import torch
import cv2
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from ultralytics import YOLO


app = FastAPI(title="EO Object Detection API")

# load model 
model = YOLO("weights/best.pt")
CLASS_NAMES = {
    0: "Airplanes",
    1: "Ships",
    2: "Storage tanks",
    3: "Baseball diamonds",
    4: "Tennis courts",
    5: "Basketball courts",
    6: "Ground track fields",
    7: "Harbors",
    8: "Bridges",
    9: "Vehicles",
}


@app.get("/")
def root():
    return {
        "message": "YOLOv8 EO detection API",
        "status": "running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix or ".jpg"

    # save uploaded file
    with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        input_path = tmp.name

    # inference 
    results = model.predict(
        source=input_path,
        imgsz=640,
        conf=0.25,
        device=0 if torch.cuda.is_available() else "cpu",
        verbose=False
    )

    r = results[0]
    
    # detection summary (console output)
    summary = defaultdict(list)

    if r.boxes is not None:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = CLASS_NAMES.get(cls_id, str(cls_id))
            summary[class_name].append(conf)

    class_summary = {
        class_name: {
            "count": len(confidences),
            "average_confidence": round(sum(confidences) / len(confidences), 3)
        }
        for class_name, confidences in summary.items()
    }

    class_summary = dict(
        sorted(class_summary.items(), key=lambda x: x[1]["count"], reverse=True)
    )

    print("========== Detection Summary ==========")
    print({
        "num_detections": sum(v["count"] for v in class_summary.values()),
        "summary": class_summary
    })
     

    # draw boxes + labels 
    im = r.plot()

    # save output image
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / f"pred_{Path(file.filename).name}"
    cv2.imwrite(str(output_path), im)

    return FileResponse(
        output_path,
        media_type="image/jpeg",
        filename=f"pred_{Path(file.filename).name}"
    )