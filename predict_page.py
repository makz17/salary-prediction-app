import streamlit as st
import numpy as np
import pickle

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

def show_predict_page():

    st.markdown("<h2 style='text-align: center; font-weight: bold;'>Software Developer Salary Prediction</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>We need some information to predict salary:</h3>", unsafe_allow_html=True)
    countries = (
        "United States",
        "Canada",
        "United Kingdom",
        "Germany",
        "France",
        "India",
        "Brazil",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 0)

    selection = st.button("Calculate Salary")
    if selection:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")




