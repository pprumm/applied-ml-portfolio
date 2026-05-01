# Deployment Demo

Inference-only deployment of a trained EO object detection model as an API.

## Purpose

VHR aerial image → YOLOv8 → object detection API  
Focus: **EO object detection + ML inference + deployment (CI/CD)**

## Flow

```text
Image → YOLOv8 checkpoint → FastAPI → Streamlit → Docker → CI → CD (Render)
````

---

## Input

```text
sample_data/images/
test_3.jpg ... test_649.jpg (130 test images)
```

Streamlit:

* upload an aerial image
* run YOLO inference
* visualize detected objects

## Output

```json
{
  "model": "yolov8_vhr10",
  "mode": "inference_only",
  "detections": [
    {
      "class": "airplane",
      "confidence": 0.94,
      "bbox": [120, 80, 260, 210]
    }
  ]
}
```


## Run

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

API:
```
http://127.0.0.1:8000/predict
```

Tests:
```
python -m pytest
```

UI:

```bash
python -m streamlit run streamlit_app/app.py
```

Docker:

```bash
docker build -t eo-deployment-demo .
docker run -p 8000:8000 eo-deployment-demo
```

## CI/CD

```text
git push → CI (GitHub Actions) → CD (Render) → live API
```

Start (Render):

```bash
uvicorn app:app --host 0.0.0.0 --port 10000
```

---

## Stack

YOLOv8 · Ultralytics · FastAPI · Streamlit
Docker · GitHub Actions · Render · PyTorch
