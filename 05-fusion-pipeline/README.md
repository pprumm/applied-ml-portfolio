# Fusion Pipeline — Flood Mapping

## Overview

This project presents a compact geospatial ML pipeline for flood mapping using Sentinel-1 SAR and Sentinel-2 optical data.

The focus is on building a clear, reproducible workflow from raw geospatial data to segmentation output under real-world observation constraints, rather than maximizing model complexity.

---

## Why SAR + Optical?

Flood events often occur under heavy cloud cover, limiting optical imagery.

- **Sentinel-2 (optical)**: strong surface detail under clear conditions  
- **Sentinel-1 (SAR)**: weather-independent backscatter (VV, VH)  

Combining both improves robustness under real-world conditions.

---

## Pipeline

1. **Data Ingestion**
   - Read GeoTIFF with Rasterio (GDAL backend)
   - Extract SAR (VV, VH) and optical bands (RGB + NIR)

2. **Preprocessing**
   - Align resolution
   - Stack channels
   - Normalize inputs

3. **Model**
   - Lightweight U-Net segmentation
   - Multimodal feature fusion

4. **Inference**
   - Flood probability map
   - Binary flood mask

5. **Evaluation**
   - IoU, F1-score, Precision, Recall

---

## Geospatial Processing

Rasterio (GDAL) is used to:

- read GeoTIFF bands  
- stack SAR and multispectral inputs  
- resample to a common grid  

This bridges geospatial data handling with ML workflows.

---

## Model Design

- SAR branch: Sentinel-1 (VV, VH)  
- Optical branch: Sentinel-2 (RGB + NIR)  
- Feature fusion → segmentation mask  

---

## Results

Metrics:
- (IoU / F1-score / Precision / Recall to be added)

Example outputs:
- (![Prediction Map](results/prediction_map.png)
- (![Flood Mask](results/flood_mask.png))

---

## Key Insight

- Optical provides surface detail  
- SAR remains reliable under clouds  
- Fusion improves robustness for flood mapping  

---

## Engineering Relevance

This project demonstrates an end-to-end ML pipeline:

- geospatial data ingestion  
- multimodal preprocessing  
- deep learning segmentation  
- reproducible inference workflow  

---

## Applications

- disaster response  
- flood monitoring  
- infrastructure risk assessment  

---

## Summary

A minimal, engineering-focused pipeline combining:

- SAR (Sentinel-1)  
- Optical (Sentinel-2)  
- Deep learning segmentation  

for robust flood extent mapping.
