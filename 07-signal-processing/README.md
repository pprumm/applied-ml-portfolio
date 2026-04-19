# 07. Signal Processing — GNSS Residual Analysis & Sensor Fusion

Time-series analysis of GNSS observations using **residual analysis** and **lightweight sensor fusion (multi-satellite GNSS and GNSS–InSAR integration)**, combining physics-based measurement models with machine learning.

---

## Overview

This project extends the signal-processing framework developed in the VLBI section to **GNSS measurements**, focusing on **measurement modeling, residual analysis, multi-satellite GNSS fusion, and cross-sensor integration with InSAR**.

Rather than implementing a full orbit determination system, a simplified measurement model is used to explain the dominant signal structure. Machine learning is then applied to **residuals** to detect anomalies and unmodeled effects.

---

## What is demonstrated

* GNSS signal processing via measurement modeling (observation − model)
* Residual construction and interpretation in GNSS workflows
* Time-series anomaly detection using **Autoencoder / LSTM**
* **Lightweight sensor fusion** via multi-satellite residual aggregation
* Conceptual integration of GNSS and InSAR time-series signals
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

### 3. Orbit Determination Context

Satellite positions in the measurement model are taken from external orbit products (e.g., broadcast ephemeris or precise SP3). Their accuracy directly influences the structure and stability of the residuals.

$$
\rho = | \mathbf{x}_s - \mathbf{x}_r |
$$

where $$( \mathbf{x}_s )$$ is the satellite state and $$( \mathbf{x}_r )$$ is the receiver position.

Comparing residuals across orbit sources illustrates how state accuracy propagates into measurement consistency, reflecting the estimation–residual loop in GNSS workflows without implementing a full POD system.

### 4. Residual Signal Processing

* Normalize residuals
* Construct temporal windows
* Organize signals per satellite

### 5. Sensor Fusion Component (GNSS & GNSS–InSAR)

This project incorporates a **lightweight sensor-fusion strategy** at two levels:

**5.1. Multi-satellite GNSS fusion (homogeneous):**

Residuals from multiple satellites are aggregated into a single signal:

$$
r_{\text{fused}} = \frac{1}{N} \sum_{i=1}^{N} r_i
$$

This reduces satellite-specific noise and improves robustness for anomaly detection.

**5.2. GNSS–InSAR integration (cross-sensor, conceptual):**

GNSS and InSAR provide complementary observations:

* GNSS → absolute, point-wise displacement (cm-level)
* InSAR → dense spatial deformation (mm-level, relative, LOS)

GNSS signals can be used to:

* anchor InSAR time-series to an absolute reference
* correct long-term drift and bias
* support joint interpretation of deformation signals

This demonstrates how GNSS-derived signals can serve as a stable reference for integrating satellite-based Earth observation data.


### 6. Anomaly Injection (Controlled Evaluation)

Synthetic anomalies are introduced to simulate real GNSS signal issues:

* spikes (measurement outliers)
* step jumps (cycle-slip-like events)
* drift (bias accumulation)
* short data gaps

This enables controlled and reproducible evaluation.

### 7. Deep Learning Model

**Autoencoder (primary):**

* learns normal residual patterns
* anomaly = high reconstruction error

**Alternative:**

* LSTM for sequence prediction
* anomaly = large prediction error

### 8. Evaluation

* reconstruction error distribution
* anomaly detection precision / recall
* comparison of:
  * per-satellite residuals
  * fused residual signal

---

## Key Results

* Clear detection of injected anomalies (spikes, drift, jumps)
* Fused residual signal is more stable than individual satellite signals
* Improved robustness through multi-satellite aggregation
* Conceptual demonstration of GNSS–InSAR integration for deformation signal interpretation
* Demonstrates that ML captures **unmodeled GNSS signal behavior beyond baseline physics**

---

## Focus

* GNSS signal interpretation
* residual-based reasoning (core to GNSS/OD workflows)
* multi-satellite signal aggregation
* cross-sensor fusion (GNSS + InSAR)
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

Aggregating residuals across multiple satellites provides a simple yet effective form of GNSS-level sensor fusion. This concept extends naturally to cross-sensor integration, where GNSS can anchor and stabilize InSAR-derived deformation signals for robust Earth system analysis.

---

## Positioning

This project complements classical GNSS processing by applying machine learning to **residual analysis**, demonstrating a modern approach to **signal monitoring and anomaly detection with lightweight sensor fusion across GNSS and satellite-based Earth observation data**.

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
* Sensor fusion includes both **multi-satellite GNSS aggregation** and **conceptual GNSS–InSAR integration**
* Synthetic anomaly injection ensures controlled evaluation
* Pipeline structure mirrors real GNSS monitoring workflows

---

## Pipeline

```text
GNSS Observation → Measurement Model → Residuals → GNSS Fusion → GNSS–InSAR Integration → ML Model → Anomaly Detection
