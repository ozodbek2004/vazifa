import streamlit as st
import pickle
import numpy as np

model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

bio_features = [
    "ALB (Albumin)", "ALP (Alkaline Phosphatase)", "ALT (Alanine Transaminase)",
    "AST (Aspartate Transaminase)", "BIL (Bilirubin)", "CHE (Cholinesterase)",
    "CHOL (Cholesterol)", "CREA (Creatinine)", "GGT (Gamma-GT)", "PROT (Total Protein)"
]

result_mapping = {
   0: "Donor (Sog'lom)",
1: "Gepatit (Jigar yallig'lanishi)",
2: "Fibroz (Jigar to'qima o'zgarishi)",
3: "Sirroz (Jigar yetishmovchiligi)",
4: "Donor gumon qilinmoqda (Kasallik ehtimoli)",
}

st.title("Jigar Kasalligi tashxisi")

age = st.number_input("Yoshni kiriting", min_value=1, max_value=100, value=25, step=1)
sex = st.radio("Jinsni tanlang", options=["Erkak", "Ayol"])
sex_value = 1 if sex == "Erkak" else 0



inputs = []
for feature in bio_features:
    value = st.number_input(f"{feature}", value=0.0, step=0.1)
    inputs.append(value)

user_data = [age, sex_value] + inputs


if st.button("Natijani ko'rish"):
    prediction = model.predict([user_data])
    result = result_mapping.get(prediction[0], "Aniqlab bo'lmadi")
    st.success(f"Bashorat: {result}")