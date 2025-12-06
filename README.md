# 🏡 Intelligent Real Estate Valuation Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-green)
![React](https://img.shields.io/badge/React-Frontend-cyan)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

### 🚀 End-to-End Machine Learning SaaS Platform

**Status:** Active Development
**Live Demo:** [Add link here if you deploy later]

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

### 🐳 DevOps & MLOps
* **Containerization:** Docker & Docker Compose.
* **Version Control:** Git & GitHub.

---

## 🏗️ Project Architecture

```text
real-estate-valuation-platform/
│
├── docker-compose.yml     # Orchestration
├── backend/               # The "Brain" (Python)
│   ├── Dockerfile         # Python Container Logic
│   ├── app/               # FastAPI Server
│   │   └── main.py        # API Entry Point
│   ├── ml_engine/         # AI Logic
│   │   ├── training.py    # PyTorch Training Loop
│   │   ├── prediction.py  # Inference Logic
│   │   └── models/        # Saved .pth and .pkl artifacts
│   └── scripts/           # Data Generation Tools
│
├── frontend/              # The "Face" (React)
│   ├── Dockerfile         # React Container Logic
│   ├── src/
│   │   └── App.js         # UI Logic & API Connection
│   └── public/
│
└── housing_data.csv       # Generated Dataset

🐳 Quick Start (Docker)
Recommended for easy setup.

To spin up the full stack (Frontend + Backend) instantly:

Bash

docker-compose up --build
Frontend: Open http://localhost:3000

Backend API: Running on http://localhost:8001

⚡ How to Run Locally
1. Backend Setup (The AI Engine)
Navigate to the backend folder and install dependencies:

Bash
cd backend
pip install -r requirements.txt


Step A: Generate Data Create the synthetic dataset using statistical distributions:
Bash
python scripts/generate_data.py

Step B: Train the Model Train the Neural Network. This will save the model weights to ml_engine/models/:
Bash
python ml_engine/training.py

Step C: Start the API Launch the FastAPI server:
Bash
uvicorn app.main:app --reload --port 8001

The API will be live at: http://127.0.0.1:8001/docs

2. Frontend Setup (The User Interface)
Open a new terminal (keep the backend running) and navigate to the frontend:

Bash
cd frontend
npm install
npm start

The App will open automatically at: http://localhost:3000

1. AI Prediction Interface
[View Screenshot](./Screenshot.png)


2. API Documentation (Swagger UI)
[View Screenshot](./Screenshot2.png)


🔮 Future Improvements
Database: Migrate from CSV to PostgreSQL.

CI/CD: Automate testing pipelines with GitHub Actions.

Cloud Deployment: Deploy containers to AWS ECS or Azure.

```
