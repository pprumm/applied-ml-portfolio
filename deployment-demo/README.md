## Deployment Demo

Inference-only deployment of a pretrained EO model as an API.

---

## Purpose

Sentinel-2 (13 bands) → TorchGeo ResNet50 → API inference  
Focus: **EO data + ML inference + deployment (CI/CD)**

---

## Flow

```text
GeoTIFF (13 bands) → Rasterio/GDAL → TorchGeo (inference) → FastAPI → Streamlit → Docker → CI → CD (Render)
````

---

## Input

```text
sample_data/tile/
B01.tif ... B12.tif
```

Streamlit:

* upload new 13-band tile
* test inference

---

## Output

```json
{
  "model": "resnet50_sentinel2_all_moco",
  "mode": "inference_only",
  "embedding_shape": [2048]
}
```

---

## Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

UI:

```bash
streamlit run streamlit_app/app.py
```

Docker:

```bash
docker build -t eo-deployment-demo .
docker run -p 8000:8000 eo-deployment-demo
```

---

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

FastAPI · Docker · GitHub Actions · Render
Rasterio · GDAL · TorchGeo · Streamlit
