import streamlit as st
import numpy as np
import pickle
import random

with open("edtech_model.pkl", "rb") as file:
    model = pickle.load(file)

feature_columns = [ "Problem Solving", "Analytical Thinking", "Logical Reasoning", "Creative Writing",  "Innovation Challenges", "Lateral Thinking", "Leadership", "Communication Skills", "Teamwork"]

st.title("Career Recommendation System")
st.write("Fill in your skills on a scale of 1-10 to get career suggestions.")

user_input = []
for col in feature_columns:
    user_input.append(st.slider(col, min_value=40, max_value=100, value = random.randint(40, 100)))

if st.button("Predict Career"):
    input_data = np.array(user_input).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    career_names = ['Data Scientist' ,'Enterpreneur' ,'Financial Analyst' ,'Human Resource Specialist' ,'Manager' ,'Marketing Executive' ,'Software Engineer' ,'Teacher' ,'Writer']
    st.success(f"Recommended Career: {career_names[prediction]}")