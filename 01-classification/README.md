# 01. Classification — Scene Classification  

This project demonstrates a structured machine learning workflow for scene-level classification on Earth Observation (EO) imagery.

The objective is not only model performance, but clear comparison between feature-based machine learning and deep learning under small-data conditions.

---

## Task

Classify land-use scenes from EO imagery into semantic categories (e.g. forest, residential, agricultural).

---

## Approach

Two modeling strategies are implemented:

- **Feature-based ML (baseline)**  
  SVM trained on pretrained ResNet feature embeddings  

- **Deep Learning (CNN-based transfer learning)**  
  AlexNet, VGG, ResNet on RGB imagery

---

## Dataset

- UC Merced Land Use Dataset  
- Image size: 256 × 256 × 3  
- Multi-class classification  

---

## Results

| Model                      | Accuracy | Notes                              |
|----------------------------|----------|------------------------------------|
| SVM (ResNet features)      | XX%      | Fixed deep features (no fine-tuning) |
| AlexNet                    | XX%      | Shallow baseline                   |
| VGG16                      | XX%      | Strong feature extraction          |
| ResNet18                   | XX%      | Efficient, stable                  |
| ResNet50                   | XX% ⭐   | Best performance                   |
| ResNet101                  | XX%      | Marginal gain, higher cost         |

---

**Key observations:**
- CNN significantly outperforms feature-based ML by adapting representations  
- Feature-based ML provides a strong baseline under limited data  
- Transfer learning is effective in small-data EO scenarios  

---

**Key observations:**
- CNN significantly outperforms classical ML by capturing spatial structure  
- Classical ML struggles with texture and contextual patterns  
- Transfer learning is effective in small-data EO scenarios  

---

## Visual Results

### Sample Predictions
![predictions](results/sample_predictions.png)

### Confusion Matrix
![confusion](results/confusion_matrix.png)

---

## Key Takeaways

- Spatial context is critical for EO classification  
- Feature-based baselines provide a meaningful reference point  
- Simple architectures + clean pipelines outperform over-engineered solutions  

---

## Tech Stack

- Python  
- PyTorch  
- Scikit-learn  
- NumPy / Matplotlib  

---

## Reproducibility

All steps (data loading, preprocessing, training, evaluation) are contained in:

- `scene_classification_ucmerced.ipynb / .html` — full workflow and static view
