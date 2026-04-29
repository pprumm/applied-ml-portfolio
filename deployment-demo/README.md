## Deployment Demo

Minimal, reproducible deployment of an EO ML model as an API service.

## Flow

```text
GeoTIFF → Rasterio/GDAL → Model → FastAPI → (Streamlit) → Docker → CI → CD
```

---

## Quick Start

### 1. Local API

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Tests

```bash
pytest
```

### 3. Optional UI

```bash
streamlit run streamlit_app/app.py
```

* upload EO image
* run inference
* visualize output


### 4. Docker

```bash
docker build -t eo-deployment-demo .
docker run -p 8000:8000 eo-deployment-demo
```


### 5. CI (GitHub Actions)

On push:

* install deps
* run tests
* check API startup

### 6. CD (Render, optional)

Start command:

```bash
uvicorn app:app --host 0.0.0.0 --port 10000
```

Flow:

```text
git push → CI ✅ → Render deploy → live API
```

--- 

## Stack

**FastAPI · Docker · GitHub Actions · Render · Rasterio · GDAL · Streamlit**

## Purpose

* EO preprocessing (Rasterio/GDAL)
* API inference (FastAPI)
* optional UI (Streamlit)
* reproducibility (Docker)
* automated validation (CI/CD)
