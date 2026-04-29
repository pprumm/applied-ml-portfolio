# Deployment Demo

Minimal, step-by-step deployment of an Earth Observation (EO) ML model as a reproducible API service.

---

## Stack

FastAPI · Docker · GitHub Actions · Render · Rasterio · GDAL · Streamlit

---

## Pipeline

```text
EO image (GeoTIFF)
→ preprocessing (Rasterio/GDAL)
→ trained model
→ FastAPI API
→ (optional) Streamlit UI
→ Docker
→ CI (GitHub Actions)
→ CD (Render)
````

---

## 1. Install & Run (Local)

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 2. Test

```bash
pytest
```

---

## 3. Optional UI (Streamlit)

```bash
streamlit run streamlit_app/app.py
```

* upload EO image
* run inference
* visualize results

---

## 4. Run with Docker

```bash
docker build -t eo-deployment-demo .
docker run -p 8000:8000 eo-deployment-demo
```

---

## 5. CI (GitHub Actions)

On each push:

* install dependencies
* run tests
* verify API startup

---

## 6. CD (Render, optional)

Deploy as a public API.

**Start command:**

```bash
uvicorn app:app --host 0.0.0.0 --port 10000
```

**Flow:**

```text
git push → CI passes → Render deploy → live API
```

---

## Purpose

Demonstrates end-to-end ML system integration:

* geospatial preprocessing (Rasterio/GDAL)
* API-based inference (FastAPI)
* optional user interface (Streamlit)
* reproducible environment (Docker)
* automated validation (CI)
* optional live deployment (CD)
