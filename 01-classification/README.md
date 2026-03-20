# 01. Classification — Scene Classification  

This project demonstrates a structured machine learning workflow for scene-level classification on Earth Observation (EO) imagery.

The objective is not only model performance, but a clear comparison between feature-based machine learning and deep learning under small-data conditions.

---

## Task

Classify land-use scenes from EO imagery into semantic categories (e.g. forest, residential, agricultural).

---

## Approach

Two modeling strategies are implemented:

- **Feature-based ML (baseline)**  
  SVM trained on fixed feature embeddings extracted from a pretrained ResNet

- **Deep Learning (CNN-based transfer learning)**  
  AlexNet, VGG16, and ResNet architectures trained via transfer learning on RGB imagery

---

## Dataset

- UC Merced Land Use Dataset  
- Image size: 256 × 256 × 3  
- Multi-class classification  

---

## Results

| Model                 | Accuracy (%) | Notes                                                              |
| --------------------- | ------------ | ------------------------------------------------------------------ |
| SVM (ResNet features) | 91.9         | Fixed pretrained embeddings (no fine-tuning)                      |
| AlexNet               | 86.4         | Shallow CNN baseline (limited capacity)                           |
| VGG16                 | 82.9         | High-capacity CNN — prone to overfitting on small data            |
| ResNet18              | 97.1         | Residual learning — efficient and stable                          |
| ResNet50              | **98.6**     | Best-performing model                                             |
| ResNet101             | 96.7         | Increased depth without performance improvement                   |

ResNet50 achieves the best trade-off between accuracy and model complexity, while deeper variants show diminishing returns.

---

**Key observations:**
- CNNs outperform feature-based ML by learning task-specific representations  
- Feature-based ML remains a strong baseline under limited data  
- Deeper architectures (ResNet) outperform AlexNet/VGG due to residual learning  
- Transfer learning is effective in small-data EO scenarios  
  
---

## Visual Results

### Sample Predictions
![predictions](results/sample_predictions.png)

### Confusion Matrix
![confusion](results/confusion_matrix.png)

---

## Key Takeaways

- Spatial context is critical for EO scene classification 
- Feature-based baselines provide a meaningful reference point 
- Simple architectures and clean pipelines outperform over-engineered solutions

---

## Tech Stack

- Python  
- PyTorch  
- Scikit-learn  
- NumPy / Matplotlib  

---

## Reproducibility

All steps (data loading, preprocessing, training, evaluation) are contained in:

- `scene_classification_ucmerced.{ipynb,html}` — full workflow and static view
