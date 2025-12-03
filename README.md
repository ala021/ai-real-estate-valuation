# 🏡 Intelligent Real Estate Valuation Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-green)
![React](https://img.shields.io/badge/React-Frontend-cyan)

### 🚀 End-to-End Machine Learning SaaS Platform

**Status:** Active Development


## 📋 Overview
This project is a full-stack AI application designed to predict real estate property values with high precision. Unlike simple notebook experiments, this is a production-ready system that integrates a **Deep Learning** regression model into a scalable **Microservices Architecture**.

It demonstrates a complete data pipeline: from raw data generation (Numpy) to model training (PyTorch), API deployment (FastAPI), and user interaction (React).

---

## 🛠️ Tech Stack

### 🧠 Artificial Intelligence & Data Science
* **Deep Learning:** PyTorch (Custom `nn.Module` Architecture).
* **Data Processing:** Pandas, Numpy (Advanced Statistical Distributions).
* **Model Serialization:** Joblib & State Dicts for inference.
* **Metrics:** R2 Score Validation.

### ⚙️ Backend Engineering
* **Framework:** FastAPI (Asynchronous REST API).
* **Validation:** Pydantic Models for strict type checking.
* **Architecture:** Modular MVC pattern (Separation of Concerns).

### 💻 Frontend Development
* **Framework:** React.js (Hooks & State Management).
* **Styling:** CSS3 & Responsive Design.
* **Connectivity:** Fetch API for real-time inference.

---

## 🏗️ Project Architecture

```text
real-estate-valuation-platform/
│
├── backend/               # The "Brain" (Python)
│   ├── app/               # FastAPI Server
│   │   └── main.py        # API Entry Point
│   ├── ml_engine/         # AI Logic
│   │   ├── training.py    # PyTorch Training Loop
│   │   ├── prediction.py  # Inference Logic
│   │   └── models/        # Saved .pth and .pkl artifacts
│   └── scripts/           # Data Generation Tools
│
├── frontend/              # The "Face" (React)
│   ├── src/
│   │   └── App.js         # UI Logic & API Connection
│   └── public/
│
└── housing_data.csv       # Generated Dataset
