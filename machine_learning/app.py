import streamlit as st
import joblib
import numpy as np

model=joblib.load('student_result_classifier.pkl')

st.title("Student Pass/Fail Classifier based on Study hours and Attendance")
#streamlit run <filepath>
st.write("Enter Study Hours and Attendance")

#User Inputs
study_hours=st.number_input("Study Hours", placeholder="Study Hours")
attendance=st.slider("Attendance",min_value=0,max_value=100)

input_data=np.array([[study_hours,attendance]])

if st.button("Predict"):
    prediction=model.predict(input_data)
    classnames=['Fail','Pass']
    st.success(f"Predicted Class: {classnames[prediction[0]]}") #prediction[0]-->0 ; classnames[0]-->Fail