# Placement Predictor App 🎓💼

This is a simple machine learning web app built using **Streamlit** that predicts whether a student will be placed or not, based on their **CGPA** and **IQ**.

## 🔍 About

The app uses a trained **Logistic Regression model** and a fitted **StandardScaler** to make predictions. It is designed to demonstrate basic machine learning deployment using Streamlit.

## 🚀 Live Demo

Try the deployed app here:  
👉 [Placement Predictor on Hugging Face Spaces](https://huggingface.co/spaces/<your-username>/<your-space-name>)

> ⚠️ Replace the above link with your actual Hugging Face Space URL.

## 📁 Files in This Repo

- `app.py` or `streamlit_app.py`: Main Streamlit app script
- `model.pkl`: Trained ML model (Logistic Regression)
- `sc.pkl`: Pre-fitted scaler used to transform input data
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker config for Hugging Face Spaces

## 🧠 How It Works

1. User inputs CGPA and IQ
2. The inputs are scaled using `StandardScaler`
3. The model predicts placement (`Placed` or `Not Placed`)
4. Streamlit displays the result on the interface

## 🔧 How to Run Locally

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py  # or streamlit_app.py
