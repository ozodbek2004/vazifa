import streamlit as st
import pickle

# Modelni yuklash
model_path = "modelim.pkl"  # Model fayl yo'li
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Bioximik parametrlar ro'yxati
bio_features = [
    "ALB (Albumin)", "ALP (Alkaline Phosphatase)", "ALT (Alanine Transaminase)",
    "AST (Aspartate Transaminase)", "BIL (Bilirubin)", "CHE (Cholinesterase)",
    "CHOL (Cholesterol)", "CREA (Creatinine)", "GGT (Gamma-GT)", "PROT (Total Protein)"
]

# Natija xaritasi
result_mapping = {
    0: "Donor (Sog'lom)",
    1: "Gepatit (Jigar yallig'lanishi)",
    2: "Fibroz (Jigar to'qima o'zgarishi)",
    3: "Sirroz (Jigar yetishmovchiligi)",
    4: "Donor gumon qilinmoqda (Kasallik ehtimoli)"
}

# Dastur sarlavhasi
st.title("Jigar Kasalligi Tashxisi")
st.write("""
Ushbu dastur bioximik test natijalaringizga asoslanib jigar kasalligi ehtimolini bashorat qiladi. 
Kerakli parametrlarni kiriting va natijani ko'ring.
""")

# Foydalanuvchi ma'lumotlari
st.header("Shaxsiy Ma'lumotlar")
age = st.number_input("Yoshingizni kiriting", min_value=1, max_value=100, value=25, step=1)
sex = st.radio("Jinsingizni tanlang", options=["Erkak", "Ayol"])
sex_value = 1 if sex == "Erkak" else 0

# Bioximik parametrlarni kiritish
st.header("Bioximik Parametrlari")
inputs = []
for feature in bio_features:
    value = st.number_input(f"{feature} (mmol/L yoki tegishli birlikda)", value=0.0, step=0.1)
    inputs.append(value)

# Foydalanuvchi ma'lumotlarini tayyorlash
user_data = [age, sex_value] + inputs

# Natija ko'rsatish
if st.button("Natijani Ko'rish"):
  
    prediction = model.predict([user_data])
    result = result_mapping.get(prediction[0], "Aniqlab bo'lmadi")
    st.success(f"**Bashorat:** {result}")
   
