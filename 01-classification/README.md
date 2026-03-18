# 01. Classification — Scene Classification  

This project demonstrates a structured machine learning workflow for scene-level classification on Earth Observation (EO) imagery.

The objective is not only model performance, but clear comparison between classical machine learning and deep learning under small-data conditions.

---

## Task

Classify land-use scenes from EO imagery into semantic categories (e.g. forest, residential, agricultural).

---

## Approach

Two modeling strategies are implemented:

- **Classical ML (baseline)**  
  Random Forest trained on flattened pixel features  

- **Deep Learning (CNN-based transfer learning)**  
  AlexNet, VGG16, ResNet18, ResNet50, ResNet101 on RGB imagery

---

## Dataset

- UC Merced Land Use Dataset  
- Image size: 256 × 256 × 3  
- Multi-class classification  

---

## Results

| Model              | Type          | Accuracy | Notes                         |
|--------------------|---------------|----------|-------------------------------|
| Random Forest      | Classical ML  | XX%      | No spatial awareness          |
| AlexNet            | CNN           | XX%      | Shallow baseline              |
| VGG16              | CNN           | XX%      | Strong feature extraction     |
| ResNet18           | CNN           | XX%      | Efficient, stable             |
| ResNet50           | CNN           | XX% ⭐   | Best performance              |
| ResNet101          | CNN           | XX%      | Marginal gain, higher cost    |

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
- Baseline models are essential for meaningful comparison  
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
