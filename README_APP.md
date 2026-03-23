# 🛌 Sleep Disorder Prediction App

Aplicación web desarrollada con **Streamlit** para predecir trastornos del sueño a partir de variables de estilo de vida y salud.

---

## 🚀 Demo

👉 (Añadir aquí el link de Render cuando lo tengamos)

---

## 🧠 Descripción del proyecto

Este proyecto utiliza un modelo de Machine Learning para clasificar si una persona presenta:

- None (sin trastorno)
- Insomnia
- Sleep Apnea

El modelo ha sido entrenado a partir del dataset:

Sleep Health and Lifestyle Dataset (Kaggle)

---

## ⚙️ Tecnologías utilizadas

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

---

## 🧩 Pipeline del proyecto

1. Análisis exploratorio (EDA)
2. Preprocesado de datos
   - Eliminación de variables irrelevantes
   - Transformación de Blood Pressure
   - Encoding de variables categóricas
3. Entrenamiento de modelos:
   - Logistic Regression
   - Random Forest
   - Gradient Boosting
4. Evaluación de modelos
5. Selección del mejor modelo (Gradient Boosting)
6. Desarrollo de aplicación web con Streamlit
7. Despliegue en Render

---

## 📊 Resultados

Modelo final: **Gradient Boosting**

- Accuracy: 0.96
- Buen equilibrio entre clases
- Buen recall en clases críticas (Sleep Apnea)

---

## 🖥️ Uso local

```bash
pip install -r requirements.txt
streamlit run src/app.py