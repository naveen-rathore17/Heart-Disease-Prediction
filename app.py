import streamlit as st 
import pandas as pd
import joblib

model = joblib.load('KNN_Heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_col = joblib.load('columns.pkl')

st.title("Heart Stroke Prediction by Naveen🩺")
st.markdown('Provide The Following Details')

age = st.slider('Age',18,100,40)
sex = st.selectbox('Sex',['M','F'])
chest_pain = st.selectbox("Chest Pain Type",['ATA','NAP','TA','ASY'])
resting_bp=st.number_input("resting Blood Pressure (mm Hg)",80,200,120)
cholestrol = st.number_input("Cholesterol (mg/dL)",100,600,200)
fasting_bs = st.selectbox("Fasting blood Sugar > 120 mg/dL",[0,1])
resting_ecg = st.selectbox("Resting ECG",['Normal','ST','LVH'])
max_hr = st.slider("Max Heart Rate",60,220,150)
exercise_angina = st.selectbox("Exercise-Induced Angina",['Y','N'])
oldpeak = st.slider("Oldpeak (ST Depression)",0.0,6.0,1.0)
st_slope = st.selectbox("ST Slope",['Up','Flat','Down'])

if st.button("Predict"):
  raw_input={
      'Age': age,
      'Sex' + sex:1,
      'ChestPainType'+ chest_pain:1,
      'RestingBP': resting_bp,
      'Cholesterol': cholestrol,
      'FastingBS': fasting_bs,
      'RestingECG'+ resting_ecg:1,
      'MaxHR': max_hr,
      'ExerciseAngina'+ exercise_angina:1,
      'Oldpeak': oldpeak,
      'ST_Slope'+ st_slope:1
  }
  input_df= pd.DataFrame([raw_input])
  for col in expected_col:
    if col not in input_df.columns:
      input_df[col] = 0
  input_df = input_df[expected_col]

  scaled_input = scaler.transform(input_df)
  prediction = model.predict(scaled_input)[0]

  if prediction == 1:
    st.error("⚠️High risk Of Heart Disease")
  else:
    st.error("✅Low risk to Heart Disease") 