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

- Controlled comparison of CNN (FCN, DeepLabV3, U-Net) and transformer (SegFormer, Swin) architectures  
- Evaluation under small-data and class-imbalance conditions     
- Input strategy analysis (RGB vs multispectral vs spectral projection, where applicable)  
- Pixel-wise evaluation with task-appropriate metrics (beyond OA)
  
---

## Datasets

- General Land-Cover Segmentation 
- Landslide Hazard Segmentation

### Dataset Details

**General Segmentation (LandCoverAI subset)**
- RGB aerial imagery
- Pixel-wise land-cover annotations (5 classes: Background, Building, Woodland, Water, Road)
- Background class ignored
- Resized to 512 × 512 for training
- Total samples: 100
- Train / validation / test split: 60 / 20 / 20 (controlled subset, fixed seed)

**Landslide Segmentation (Landslide4Sense subset)**
- 14-channel input (spectral + topographic)
  - 12 multispectral bands from Sentinel-2 (B1–B12)
  - 1 slope band derived from ALOS PALSAR (B13)
  - 1 elevation band (DEM) from ALOS PALSAR (B14)
- Pixel-wise binary mask (landslide vs. non-landslide)
- Patch size: 128 × 128 (~10 m resolution)
- Total samples: 3799
- Train / test split: 959 / 2,840 (deterministic, index-based)

---

## Results

### General Segmentation — Model Benchmark (Controlled Setting)

| Model                 | Architecture Type | mIoU    | OA    | Key Insight                               |
|-----------------------|-------------------|---------|-------|-------------------------------------------|
| FCN (ResNet50)        | CNN (baseline)    | **0.70**| 0.93  | Strong and stable baseline                |
| DeepLabV3 (ResNet50)  | CNN (ASPP)        | 0.56    | 0.91  | No gain from multi-scale under small data |
| U-Net (TorchGeo)      | Encoder–Decoder   | 0.43    | 0.84  | Weak generalization                       |
| U-Net (ResNet50)      | Hybrid CNN        | 0.46    | 0.89  | Slight improvement via pretraining        |
| SegFormer-B0          | Transformer       | 0.45    | 0.89  | Underperforms in limited data regime      |

### General Segmentation — Detailed Metrics (FCN ResNet50, Per-class IoU)

| Class    | IoU    | Key Insight |
|----------|--------|-------------|
| Building | 0.62 | Moderate performance; variability in roof appearance |
| Woodland | 0.96 | Woodland dominates performance |
| Water    | 0.85 | Generally strong; occasional confusion with vegetation |
| Road     | 0.38 | Primary failure mode (thin, fragmented) |

### Landslide Segmentation — Multispectral Strategy Comparison

| Model                 | Input Strategy    | Landslide F1 | Mean F1 | OA    | Key Insight                               |
|-----------------------|-------------------|--------------|---------|-------|-------------------------------------------|
| U-Net                 | 14 bands (direct) | **61.74**    | 80.46   | 98.39 | Best balance, strong baseline             |
| FCN (ResNet50)        | 14 bands (direct) | 50.45        | 74.62   | 97.64 | Stable but weaker minority detection      |
| FCN (ResNet50)        | 14 → 3 projection | 52.88        | 75.89   | 97.85 | Learnable spectral compression helps      |
| DeepLabV3 (ResNet50)  | 14 → 3 projection | 52.99        | 75.95   | 97.87 | Comparable to FCN                         |
| U-Net (TorchGeo)      | 14 bands (direct) | 58.02        | 78.58   | 98.29 | Native multispectral model                |
| SegFormer-B0          | 14 → 3 projection | 59.56        | 79.26   | 97.97 | Transformer competitive but data-hungry   |
| Swin Transformer      | 14 → 3 projection | 55.86        | 77.53   | 98.43 | Strong OA, weaker on minority class       |

### Peak Performance (Early Convergence)

| Model   | Setting           | Landslide F1 | Mean F1 | OA    |
|---------|-------------------|--------------|---------|-------|
| U-Net   | 14 bands (direct) | **63.01**    | 81.09   | 98.39 |

**Evaluation metrics:**
- Overall Accuracy (OA)
- Intersection over Union (IoU / mIoU)
- F1-score (Landslide class, primary metric under imbalance)

**Key Observations:**
- U-Net provides a strong baseline for pixel-wise EO tasks  
- Landslide segmentation is more challenging due to class imbalance and ambiguous boundaries  
- Pixel-level evaluation is essential for judging spatial quality
- Simple CNN baselines (U-Net / FCN) remain highly competitive under limited data conditions

---

## Visual Results

### General Segmentation
<p align="center">
  <img src="images/landcover_prediction.png" width="85%" />
</p>

Clear spatial segmentation with strong performance on large homogeneous regions (e.g., vegetation).  
Building predictions rely on roof appearance, leading to boundary leakage and confusion with visually similar regions.   
Errors primarily occur at class boundaries and thin structures (e.g., roads), highlighting structural challenges in EO segmentation.  

### Landslide Segmentation
<p align="center">
  <img src="images/landslide_prediction.png" width="100%" />
</p>

Model captures major landslide regions but struggles with fine boundaries and small fragmented areas.  
Performance is sensitive to class imbalance, making Landslide F1 more informative than overall accuracy.

---

## Training Setup

**General Segmentation**
- Optimizer: Adam
- Learning rate: 1e-4
- Scheduler: StepLR (step_size=5, gamma=0.5)
- Batch size: 4
- Epochs: 15  
- Loss function: CrossEntropyLoss (ignore background class)  
- Pretraining: ImageNet weights

**Landslide Segmentation**
- Optimizer: Adam (weight decay = 5e-4)   
- Learning rate: 2.5e-4  
- Batch size: 32
- Epochs: 100  
- Loss function: CrossEntropyLoss (3:1 landslide class weight)  

---

## Key Takeaways

- Semantic segmentation requires both local detail and global context  
- EO hazard mapping introduces additional challenges beyond standard land-cover segmentation  
- Clean baseline pipelines are more valuable than excessive architectural complexity  

---

## Project Structure

```
02-segmentation/
├── images/                               # figures (predictions, confusion matrices)
├── 01_landcover_segmentation.ipynb
├── 01_landcover_segmentation.html
├── 02_landslide_segmentation.ipynb
├── 02_landslide_segmentation.html
└── README.md
```

---

## Tech Stack

- Python, PyTorch  
- Torchvision (FCN, DeepLabV3, ResNet)  
- TorchGeo (LandCoverAI, U-Net)  
- segmentation-models-pytorch (U-Net)  
- Hugging Face Transformers (SegFormer, UPerNet-Swin)  
- NumPy, Matplotlib, scikit-learn  

---

## Reproducibility

All steps (data loading, preprocessing, training, evaluation) are contained in:

- `01_landcover_segmentation.{ipynb,html}` — full workflow and static view
- `02_landslide_segmentation.{ipynb,html}` — full workflow and static view

The pipeline uses a fixed random seed (LandCoverAI) and deterministic index-based splits (Landslide4Sense) to ensure consistent results.
