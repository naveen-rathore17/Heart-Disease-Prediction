# Heart Disease Prediction Using KNN 🩺

A machine learning web application built with **Python, scikit-learn, and Streamlit**. Users enter health-related measurements, and a saved **K-Nearest Neighbors (KNN)** classification model predicts a heart disease class.

> **Important:** This is an educational ML project, not a medical diagnosis or validated clinical risk assessment. Do not use its predictions to make healthcare decisions.

## Features

- Interactive Streamlit form for entering health indicators
- KNN classifier loaded from a saved `.pkl` file
- Saved preprocessing scaler and expected feature columns
- Displays the predicted class as a high-risk or low-risk message

## Tech Stack

- Python
- Streamlit
- Pandas
- scikit-learn (KNN and preprocessing)
- Joblib

## Project Structure

```text
heart-disease-prediction/
├── app.py
├── KNN_Heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

**File descriptions:**

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit user interface and prediction pipeline |
| `KNN_Heart.pkl` | Saved trained KNN classifier |
| `scaler.pkl` | Saved fitted preprocessing scaler |
| `columns.pkl` | Feature column names and their order |
| `requirements.txt` | Python package dependencies |
| `.gitignore` | Files and folders Git should ignore |

## 🚀 Live Demo

Try the Heart Disease Prediction application online using Streamlit.

**🔗 Live App:** [HeartCare AI Predictor](https://heartcare-ai-predictor.streamlit.app/)

**Tech Stack:** Python | KNN | Scikit-learn | Streamlit

> ⚠️ **Disclaimer:** This application is developed for educational purposes only and is not intended for medical diagnosis.

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the placeholders with your actual GitHub repository details.

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If activation is restricted, you can use `venv\Scripts\python.exe` directly instead.

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start Streamlit

```bash
python -m streamlit run app.py
```

Open the local address displayed in the terminal (typically `http://localhost:8501`).

### 5. Make a prediction

1. Enter age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, ECG result, maximum heart rate, exercise-induced angina, oldpeak, and ST slope.
2. Click **Predict**.
3. View the model's classification message.

## Model Input Features

The application uses the following inputs:

| Input | Description |
| --- | --- |
| Age | Age in years |
| Sex | M / F |
| Chest Pain Type | ATA / NAP / TA / ASY |
| RestingBP | Resting blood pressure |
| Cholesterol | Cholesterol level |
| FastingBS | Fasting blood sugar indicator (0 / 1) |
| RestingECG | Normal / ST / LVH |
| MaxHR | Maximum heart rate |
| ExerciseAngina | Y / N |
| Oldpeak | ST depression |
| ST_Slope | Up / Flat / Down |

The saved `columns.pkl` contains the 15 final model input columns, including one-hot encoded categories. The app aligns the input data to these columns and applies the saved scaler before predicting.

## Notes for Developers

- Keep `app.py`, `KNN_Heart.pkl`, `scaler.pkl`, and `columns.pkl` together in the repository root for the current relative file paths to work.
- **Do not commit `venv/`**. Every contributor should create their own environment and install `requirements.txt`.
- The exact scikit-learn version used to train the model was not supplied. If loading the `.pkl` files causes a version warning or error, use the original training environment's package versions and update `requirements.txt` accordingly.
- **Check preprocessing before using the predictions:** the current uploaded `app.py` constructs names such as `SexM`, but the saved expected columns include `Sex_M`. This mismatch can cause categorical inputs to be ignored. Fix and test feature encoding before treating predictions as reliable.
- Only load `.pkl` files from trusted sources. Joblib/pickle loading can execute arbitrary code.
- Model accuracy and clinical validity have not been established by the supplied application files.

## Upload to GitHub

After creating a repository on GitHub:

```bash
git init
git add app.py KNN_Heart.pkl scaler.pkl columns.pkl requirements.txt .gitignore README.md
git commit -m "Add KNN heart disease Streamlit project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

If you already have a Git repository, skip `git init` and any setup commands you have already completed.

## Disclaimer

This project is for educational and demonstration purposes only. Its outputs are model classifications, not medical advice or a substitute for professional evaluation.
