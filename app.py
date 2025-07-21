import streamlit as st
import joblib
import numpy as np

model = joblib.load('D:/mydatabase/Data mining/churn_model.pkl')
st.title('Churn Prediction App')

 
age = st.slider('Age', 18, 100, 30)
tenure = st.slider('Tenure (in months)', 0, 100, 12)
gender = st.selectbox('Gender', ['Male', 'Female'])


gender_num = 1 if gender == 'Male' else 0


input_data = np.array([[age, tenure, gender_num]])
input_data_scaled = scaler.transform(input_data)  # لو مش عامل scaling احذف السطر ده


if st.button('Predict'):
    prediction = model.predict(input_data_scaled)[0]  # لو مش عامل scaling غير لـ input_data
    if prediction == 1:
        st.error('❌ Customer is likely to Churn.')
    else:
        st.success('✅ Customer is likely to Stay.')