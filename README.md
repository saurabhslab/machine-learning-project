# Student Performance Prediction ML Project

## Overview

This repository contains an end-to-end machine learning project for predicting student math exam performance. The project includes data ingestion, preprocessing, model training, artifact persistence, and a Flask-based web application for inference.

## Key features

- Data ingestion from `notebook/data/stud.csv`
- Data preprocessing with categorical encoding and scaling
- Model training using multiple regressors and hyperparameter search
- Model artifact saving to `artifacts/model.pkl` and `artifacts/preprocessor.pkl`
- Flask web UI for single-student prediction

## Repository structure

- `app.py` - Flask application entrypoint for the prediction UI
- `requirements.txt` - Python dependencies
- `setup.py` - package metadata and install helper
- `artifacts/` - saved model, preprocessor, and split datasets
- `notebook/` - notebooks for EDA and model training
- `src/`
  - `components/`
    - `data_ingestion.py` - ingestion and train/test split logic
    - `data_transformation.py` - preprocessing pipeline and transformer persistence
    - `model_trainer.py` - model selection, tuning, training, and saving
  - `pipeline/`
    - `predict_pipeline.py` - inference pipeline used by Flask
  - `exception.py` - custom exception handling
  - `logger.py` - logging configuration
  - `utils.py` - helpers for object persistence and model evaluation
- `templates/`
  - `index.html` - home landing page
  - `home.html` - prediction form UI

## Setup

1. Create a Python environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Training the model

The current training flow is implemented in `src/components/data_ingestion.py`, which reads the dataset, splits it, preprocesses it, and then trains a regression model.

Run:
```bash
python src/components/data_ingestion.py
```

This should create:
- `artifacts/train.csv`
- `artifacts/test.csv`
- `artifacts/data.csv`
- `artifacts/preprocessor.pkl`
- `artifacts/model.pkl`

## Running the web app

Start the Flask app:
```bash
python app.py
```

Open your browser at:

- `http://localhost:5001/`

Use the form to enter student demographics and exam scores, then submit to get the predicted math score.

## Notes

- The web UI form is defined in `templates/home.html`.
- Inference loads the saved model and preprocessor from the `artifacts/` folder.
- If you want to retrain or improve the model, update the training logic in `src/components/model_trainer.py` and data transformation logic in `src/components/data_transformation.py`.

## Contact

- Author: Saurabh
