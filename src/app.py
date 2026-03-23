import streamlit as st
import pandas as pd
import joblib

# ============================================
# 1. CONFIGURACIÓN GENERAL
# ============================================

st.set_page_config(
    page_title="Sleep Disorder Predictor",
    page_icon="🛌",
    layout="centered"
)

# ============================================
# 2. CARGA DEL MODELO
# ============================================

@st.cache_resource
def load_model():
    return joblib.load("models/sleep_model.pkl")

model = load_model()

# ============================================
# 3. CABECERA
# ============================================

st.title("🛌 Predicción de Trastornos del Sueño")
st.markdown(
    """
    Esta aplicación estima si una persona presenta:
    - **None**
    - **Insomnia**
    - **Sleep Apnea**

    a partir de variables de estilo de vida, sueño y salud.
    """
)

st.divider()

# ============================================
# 4. FORMULARIO DE ENTRADA
# ============================================

st.subheader("Introduce los datos del paciente")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 18, 80, 30)
    occupation = st.selectbox(
        "Occupation",
        [
            "Accountant", "Doctor", "Engineer", "Lawyer", "Manager",
            "Nurse", "Sales Representative", "Salesperson",
            "Scientist", "Software Engineer", "Teacher"
        ]
    )
    bmi = st.selectbox("BMI Category", ["Normal", "Overweight", "Obese"])
    sleep_duration = st.slider("Sleep Duration", 4.0, 10.0, 6.5, 0.1)
    quality_sleep = st.slider("Quality of Sleep", 1, 10, 5)

with col2:
    physical_activity = st.slider("Physical Activity Level", 10, 100, 50)
    stress = st.slider("Stress Level", 1, 10, 5)
    heart_rate = st.slider("Heart Rate", 50, 120, 70)
    steps = st.slider("Daily Steps", 1000, 20000, 6000, 500)
    systolic = st.slider("Systolic BP", 90, 180, 120)
    diastolic = st.slider("Diastolic BP", 60, 120, 80)

st.divider()

# ============================================
# 5. PREDICCIÓN
# ============================================

if st.button("Predecir", use_container_width=True):

    input_data = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Occupation": occupation,
        "Sleep Duration": sleep_duration,
        "Quality of Sleep": quality_sleep,
        "Physical Activity Level": physical_activity,
        "Stress Level": stress,
        "BMI Category": bmi,
        "Heart Rate": heart_rate,
        "Daily Steps": steps,
        "Systolic_BP": systolic,
        "Diastolic_BP": diastolic
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Datos introducidos")
    st.dataframe(input_data, use_container_width=True)

    st.subheader("Resultado de la predicción")

    if prediction == "None":
        st.success(f"Predicción: {prediction}")
        st.info("El modelo no detecta un trastorno del sueño en este perfil.")
    elif prediction == "Insomnia":
        st.warning(f"Predicción: {prediction}")
        st.info("El modelo detecta un patrón más cercano a insomnio.")
    elif prediction == "Sleep Apnea":
        st.error(f"Predicción: {prediction}")
        st.info("El modelo detecta un patrón más cercano a apnea del sueño.")