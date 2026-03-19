# Time-Series — InSAR Deformation Modeling

A compact Earth Observation project demonstrating temporal modeling of InSAR-derived ground deformation using sequence learning.

---

## Overview

This project presents a compact workflow for modeling **ground deformation time series** derived from InSAR observations using **sequence models (LSTM and Transformer)**.

Rather than focusing on full interferometric processing, the emphasis is on **temporal learning from displacement signals**, reflecting a common downstream task in geodetic and Earth Observation workflows.

---

## Objective

InSAR provides millimeter-scale measurements of surface displacement over time. These signals exhibit temporal structure driven by physical processes such as subsidence, uplift, and seasonal effects.

The objective of this notebook is to:

* learn temporal dependencies in deformation time series
* perform **one-step forecasting** of displacement
* compare a **persistence baseline** with learned sequence models (LSTM, Transformer)

---

## Why InSAR Time Series?

In contrast to image-based EO tasks, InSAR data is inherently **temporal** and requires sequence-based modeling.

Key characteristics:

* long-term trends (e.g., subsidence)
* seasonal components
* measurement noise and decorrelation effects
* irregular or sparse observations

This makes it well-suited for **time-series machine learning approaches**.

---

## Workflow

1. Load and inspect InSAR displacement time series
2. Visualize temporal patterns and signal characteristics *(figure to be added)*
3. Transform the series into supervised learning sequences
4. Define a persistence baseline (`yₜ₊₁ = yₜ`)
5. Train sequence models (**LSTM and Transformer**) for short-term forecasting
6. Evaluate using **MAE** *(values to be added)* and compare against baseline
7. Analyze prediction behavior and limitations *(figure to be added)*

---

## Technical Focus

* Time-series modeling of EO-derived geodetic signals
* Sequence preparation via sliding windows
* Baseline vs sequence model comparison (LSTM vs Transformer)
* Compact PyTorch implementations
* Physically informed interpretation of results

---

## Results

The notebook demonstrates that:

* deformation signals can be framed as **supervised temporal learning problems**
* sequence models (LSTM, Transformer) capture temporal structure beyond a naive baseline
* performance is constrained by **noise, sampling, and signal variability** inherent in InSAR data

*(quantitative results to be added)*
*(prediction vs ground truth figure to be added)*

---

## Repository Contents

* `insar_timeseries_models.{ipynb,html}` — complete workflow
* `README.md` — project description

---

## Key Takeaway

This project illustrates a clean and reproducible approach to **modeling InSAR deformation time series**, highlighting the role of sequence learning in Earth Observation and geodetic applications.
