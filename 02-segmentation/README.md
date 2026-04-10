# 02. Segmentation — Semantic Segmentation  

This folder contains two compact segmentation case studies on Earth Observation (EO) imagery, covering both general land-cover segmentation and a geohazard application.

The focus is on pixel-wise prediction, spatial evaluation, and clean, reproducible workflows.

---

## Case Studies

### 1. Land-Cover Segmentation
Pixel-wise segmentation of EO imagery into land-cover classes such as vegetation, water, and built-up areas.

**Notebook:** `01_landcover_segmentation.{ipynb,html}`

### 2. Landslide Segmentation
Pixel-wise segmentation of landslide regions using the Landslide4Sense dataset.

**Notebook:** `02_landslide_segmentation.{ipynb,html}`

---

## Approach

- U-Net-based semantic segmentation
- Supervised learning with pixel-level annotations
- Evaluation using IoU and pixel accuracy

---

## Datasets

- General EO segmentation dataset
- **Landslide4Sense** for hazard segmentation

### Dataset Details

- 

---

## Results

| Case Study              | Metric          | Score |
|-------------------------|-----------------|-------|
| General Segmentation    | IoU             | XX    |
| General Segmentation    | Pixel Accuracy  | XX    |
| Landslide Segmentation  | IoU / F1        | XX    |
| Landslide Segmentation  | Pixel Accuracy  | XX    |

**Evaluation metrics:**
- Overall Accuracy (OA)  

**Key Observations:**
- U-Net provides a strong baseline for pixel-wise EO tasks  
- Landslide segmentation is more challenging due to class imbalance and ambiguous boundaries  
- Pixel-level evaluation is essential for judging spatial quality  

---

## Visual Results

### General Segmentation
<p align="center">
  <img src="images/landcover_prediction.png" width="48%" />
</p>

text....

### Landslide Segmentation
<p align="center">
  <img src="images/landslide_prediction.png" width="48%" />
</p>

text...

---

## Training Setup

- Optimizer: SGD (momentum = 0.9, weight decay = 1e-4)   
- Learning rate: 1e-2  
- Batch size: 64
- Epochs: 10  
- Loss function: CrossEntropyLoss  
- Pretraining: ImageNet weights  

---

## Key Takeaways

- Semantic segmentation requires both local detail and global context  
- EO hazard mapping introduces additional challenges beyond standard land-cover segmentation  
- Clean baseline pipelines are more valuable than excessive architectural complexity  

---

## Project Structure

```
01-classification/
├── images/                               # figures (predictions, confusion matrices)
├── 01_landcover_segmentation.ipynb
├── 01_landcover_segmentation.html
├── 02_landslide_segmentation.ipynb
├── 02_landslide_segmentation.html
└── README.md
```

---

## Tech Stack

- Python  
- PyTorch  
- segmentation-models-pytorch  
- NumPy / Matplotlib

---

## Reproducibility

All steps (data loading, preprocessing, training, evaluation) are contained in:

- `01_landcover_segmentation.{ipynb,html}` — full workflow and static view
- `02_landslide_segmentation.{ipynb,html}` — full workflow and static view

The pipeline uses a fixed random seed (LandCoverAI) and deterministic index-based splits (Landslide4Sense) to ensure consistent results.
