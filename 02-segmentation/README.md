# 02. Segmentation — Semantic Segmentation  

This folder contains two compact segmentation case studies on Earth Observation (EO) imagery, covering both general land-cover segmentation and a geohazard application.

The focus is on pixel-wise prediction, spatial evaluation, and clean, reproducible workflows.

---

## Case Studies

### 1. General EO Segmentation
Pixel-wise segmentation of EO imagery into land-cover classes such as vegetation, water, and built-up areas.

**Notebook:** `01_general_segmentation.ipynb / .html`

### 2. Landslide Segmentation
Pixel-wise segmentation of landslide regions using the Landslide4Sense dataset.

**Notebook:** `02_landslide_segmentation.ipynb / .html`

---

## Approach

- U-Net-based semantic segmentation
- Supervised learning with pixel-level annotations
- Evaluation using IoU and pixel accuracy

---

## Datasets

- General EO segmentation dataset
- **Landslide4Sense** for hazard segmentation

---

## Results

| Case Study              | Metric          | Score |
|-------------------------|-----------------|-------|
| General Segmentation    | IoU             | XX    |
| General Segmentation    | Pixel Accuracy  | XX    |
| Landslide Segmentation  | IoU / F1        | XX    |
| Landslide Segmentation  | Pixel Accuracy  | XX    |

**Observations:**
- U-Net provides a strong baseline for pixel-wise EO tasks  
- Landslide segmentation is more challenging due to class imbalance and ambiguous boundaries  
- Pixel-level evaluation is essential for judging spatial quality  

---

## Visual Results

### General Segmentation
![general](results/general_prediction.png)

### Landslide Segmentation
![landslide](results/landslide_prediction.png)

---

## Key Takeaways

- Semantic segmentation requires both local detail and global context  
- EO hazard mapping introduces additional challenges beyond standard land-cover segmentation  
- Clean baseline pipelines are more valuable than excessive architectural complexity  

---

## Tech Stack

- Python  
- PyTorch  
- segmentation-models-pytorch  
- NumPy / Matplotlib
