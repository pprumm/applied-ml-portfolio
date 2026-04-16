# 07. Signal Processing — GNSS Residual Analysis & Sensor Fusion

Time-series analysis of GNSS observations using **residual analysis** and **lightweight sensor fusion**, combining physics-based measurement models with machine learning.

---

## Overview

This project extends the signal-processing framework developed in the VLBI section to **GNSS measurements**, focusing on **measurement modeling, residual analysis, and multi-satellite fusion**.

Rather than implementing a full orbit determination system, a simplified measurement model is used to explain the dominant signal structure. Machine learning is then applied to **residuals** to detect anomalies and unmodeled effects.

---

## What is demonstrated

* GNSS signal processing via measurement modeling (observation − model)
* Residual construction and interpretation in GNSS workflows
* Time-series anomaly detection using **Autoencoder / LSTM**
* **Lightweight sensor fusion** via multi-satellite aggregation
* Integration of physics-based modeling and machine learning

---

## Dataset

* GNSS observation data (RINEX) from International GNSS Service
* Precise orbit products (SP3) from NASA CDDIS

**Setup:**

* Single ground station
* Short observation window (e.g., 24 hours)
* Multi-satellite measurements

---

## Approach

### 1. Data Ingestion

* Parse RINEX observations (pseudorange / carrier phase)
* Load precise satellite orbits (SP3)
* Synchronize timestamps across satellites

### 2. Measurement Modeling

A simplified GNSS measurement model is used to compute the expected geometric range between satellite and receiver.

Residuals are constructed as:

$$
\text{residual} = \text{observation} - \text{model}
$$

This isolates unmodeled effects such as noise, bias, and anomalies.

### 3. Residual Signal Processing

* Normalize residuals
* Construct temporal windows
* Organize signals per satellite

### 4. Sensor Fusion Component

This project incorporates a **lightweight GNSS sensor-fusion strategy** by combining:

* multiple satellite observations (**multi-source fusion**)
* physics-based model predictions with measurements (**model–measurement fusion**)

Residuals are computed per satellite and aggregated into a fused signal:

$$
r_{\text{fused}} = \frac{1}{N} \sum_{i=1}^{N} r_i
$$

This improves robustness against noise or faults affecting individual satellites and produces a more stable anomaly detection signal.


### 5. Anomaly Injection (Controlled Evaluation)

Synthetic anomalies are introduced to simulate real GNSS signal issues:

* spikes (measurement outliers)
* step jumps (cycle-slip-like events)
* drift (bias accumulation)
* short data gaps

This enables controlled and reproducible evaluation.

### 6. Deep Learning Model

**Autoencoder (primary):**

* learns normal residual patterns
* anomaly = high reconstruction error

**Alternative:**

* LSTM for sequence prediction
* anomaly = large prediction error

### 7. Evaluation

* reconstruction error distribution
* anomaly detection precision / recall
* comparison of:

  * per-satellite residuals
  * fused residual signal

---

## Key Results

* Clear detection of injected anomalies (spikes, drift, jumps)
* Fused residual signal is more stable than individual satellite signals
* Improved robustness through multi-satellite fusion
* Demonstrates that ML captures **unmodeled GNSS signal behavior beyond baseline physics**

---

## Focus

* GNSS signal interpretation
* residual-based reasoning (core to GNSS/OD workflows)
* lightweight sensor fusion
* time-series anomaly detection
* robustness under noisy measurements

---

## Visual Summary

<p align="center">
  <img src="images/residual_per_satellite.png" width="48%" />
  <img src="images/fused_residual_anomaly.png" width="48%" />
</p>
<p align="center"><sub><em>
Per-satellite residual signals (left) and fused residual anomaly signal (right).
</em></sub></p>

---

## Key Insight

While classical GNSS processing explains most of the signal through physical models, **residual analysis reveals subtle errors, anomalies, and unmodeled effects**.

Aggregating residuals across multiple satellites provides a simple yet effective form of sensor fusion, improving robustness and interpretability of anomaly detection.

---

## Positioning

This project complements classical GNSS processing by applying machine learning to **residual analysis**, demonstrating a modern approach to **signal monitoring and anomaly detection with lightweight sensor fusion**.

---

## Technical Stack

* Python
* PyTorch (Autoencoder / LSTM)
* NumPy / Pandas
* Matplotlib
* georinex (RINEX parsing)

---

## Notes

* Focus is on **signal behavior and interpretability**, not full orbit determination
* Sensor fusion is implemented at the **measurement level (multi-satellite)**
* Synthetic anomaly injection ensures controlled evaluation
* Pipeline structure mirrors real GNSS monitoring workflows

---

## Pipeline

```text
GNSS Observation → Measurement Model → Residuals → Fusion → ML Model → Anomaly Detection
```
