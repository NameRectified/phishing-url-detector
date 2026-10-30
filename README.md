# Phishing URL Detection

## Problem Description

Phishing is a type of cyberattack in which attackers use deceptive URLs to trick users into visiting malicious websites and disclosing sensitive information, such as login credentials or financial details.

The goal of this project is to build a **binary classification system** that takes a URL as input and predicts whether it is **phishing (0)** or **legitimate (1)**.

The system uses features extracted directly from the URL, rather than relying on webpage content. This makes it possible to classify a URL without having to visit or render the website.

### Dataset Selection

This project uses the [LegitPhish Dataset](https://data.mendeley.com/datasets/hx4m73v2sf/2).

Other datasets considered:

- [Phishing Websites – UCI](https://archive.ics.uci.edu/dataset/327/phishing)
- [PhiUSIIL Phishing URL Dataset – UCI](https://archive.ics.uci.edu/dataset/967/phiusil-phishing-url-dataset)

LegitPhish was selected because its URL-based features allow classification without requiring webpage rendering or extracting features from website content.

### Approach

1. Clean the dataset by removing records with missing labels and duplicate URLs.
2. Extract numerical features directly from each URL.
3. Train a Random Forest classifier to distinguish phishing URLs from legitimate ones.
4. Save the trained model using Joblib.
5. Expose the model through a FastAPI service that accepts a URL and returns its predicted class and class probabilities.

## Project Setup

This project uses Python 3.11 and [uv](https://docs.astral.sh/uv/) for dependency and environment management.

Clone the repository and navigate to the project directory.

Install dependencies:

```bash
uv sync
```

## Running the Project

### 1. Train the model

```bash
uv run python train.py
```

This trains the Random Forest classifier and saves the model as `best_model.joblib`.

### 2. Start the prediction API

```bash
uv run python predict.py
```

The API runs at:

`http://localhost:9696`

### 3. Test the API

Open the interactive API documentation:

`http://localhost:9696/docs`

Send a POST request to `/predict` with a URL:

```json
{
  "url": "https://www.google.com"
}
```

The API returns the predicted class along with phishing and legitimate probabilities.

## Environment Setup

### Requirements
- Python 3.11
- uv

### Install dependencies

```bash
uv sync
```

This creates a virtual environment and installs the dependencies specified in `uv.lock`.

### Activate the virtual environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### Deactivate the environment

```bash
deactivate
```

## Dataset

This project uses the LegitPhish dataset for training the phishing URL classifier.

Download the dataset from:

[LegitPhish Dataset – Mendeley Data](https://data.mendeley.com/datasets/hx4m73v2sf/2)

After downloading, place `legit-phish.csv` inside the `datasets/` directory:

```text
datasets/
└── legit-phish.csv
```

The training script expects the dataset at `datasets/legit-phish.csv`.

The PhiUSIIL dataset was used separately for external model evaluation and is not required to run the prediction API.

## Datasets and Attribution

This project uses the following publicly available datasets:

### 1. LegitPhish Dataset

- Authors: Rachana Potpelwar, Uday Kulkarni, Jaishri Waghmare
- Source: [Mendeley Data – LegitPhish](https://data.mendeley.com/datasets/hx4m73v2sf/1)
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Used to train the phishing URL classification model.

### 2. PhiUSIIL Phishing URL Dataset

- Authors: Arvind Prasad, Shalini Chandra
- Source: [UCI Machine Learning Repository – PhiUSIIL](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset)
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Used for external evaluation of the trained model. Only the raw URL column was used to extract features; precomputed webpage-derived features were excluded.

The datasets are redistributed under their respective CC BY 4.0 licenses. Please refer to the original dataset pages for full attribution and licensing information.

## Docker

### Build the Docker image

```bash
docker build -t phishing-detector .
```

### Run the container

```bash
docker run -d --name phishing-api -p 9696:9696 phishing-detector
```

### Access the API

Open the interactive API documentation:

http://localhost:9696/docs

### Stop the container

```bash
docker stop phishing-api
docker rm phishing-api
```

## Cloud Deployment

The Phishing URL Detection API is deployed on Render.

**Live API:** https://phishing-url-detector-v1o2.onrender.com

**Interactive API Documentation:** https://phishing-url-detector-v1o2.onrender.com/docs

### Using the Deployed API

The API exposes a `POST /predict` endpoint that accepts a URL and returns its classification.

**Endpoint:**

```text
POST https://phishing-url-detector-v1o2.onrender.com/predict
```

**Example request:**

```bash
curl -X POST "https://phishing-url-detector-v1o2.onrender.com/predict" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.google.com"}'
```

**Request body:**

```json
{
  "url": "https://www.google.com"
}
```

The response contains:
- `url`: The submitted URL.
- `prediction`: The predicted class (`phishing` or `legitimate`).
- `phishing_probability`: Model-estimated probability of the URL being phishing.
- `legitimate_probability`: Model-estimated probability of the URL being legitimate.

### Deployment Platform

- **Platform:** Render
- **Deployment method:** Docker
- **Application framework:** FastAPI
- **Server:** Uvicorn

The application is containerized using the project's Dockerfile and deployed as a Render Web Service.