# Detection (Earth Observation)

This project covers spatial and temporal detection tasks on Earth Observation (EO) data, including object detection, change detection, and anomaly detection.

The focus is on identifying regions of interest under real-world conditions such as seasonal variation, noise, and limited labeled data.

---

## Tasks

- **Object Detection**  
  Identify and localize objects within EO imagery  

- **Change Detection**  
  Detect changes between multi-temporal image pairs  

- **Anomaly Detection**  
  Identify rare or unusual patterns without explicit labels  

---

## Approach

- Deep learning models for spatial pattern recognition  
- Multi-temporal inputs for change detection  
- Reconstruction-based methods (autoencoder) for anomaly detection  

---

## Dataset

- EO imagery (multi-temporal for change detection)  
- RGB / multi-channel inputs depending on task  

---

## Results

| Task              | Metric        | Score |
|-------------------|--------------|-------|
| Object Detection  | mAP / IoU    | XX    |
| Change Detection  | F1 / IoU     | XX    |
| Anomaly Detection | F1           | XX    |

**Observations:**
- Multi-temporal information is critical for change detection  
- Larger input resolution improves detection performance  
- Anomaly detection is sensitive to global vs local context  

---

## Visual Results

### Example Outputs
![results](results/sample_results.png)

---

## Key Takeaways

- Detection tasks require spatial and temporal context  
- Model performance is strongly influenced by input resolution  
- Simple baselines provide important reference points for evaluation  

---

## Tech Stack

- Python  
- PyTorch  
- segmentation-models-pytorch / torchvision  
- NumPy / Matplotlib  

---

## Reproducibility

Each task is implemented as a standalone notebook:

- `object_detection.ipynb`  
- `change_detection.ipynb`  
- `anomaly_detection.ipynb`  

The workflows are designed to be minimal, structured, and reproducible.
