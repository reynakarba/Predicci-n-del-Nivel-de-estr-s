import streamlit as st
import joblib
import pandas as pd

def pagina_principal():
    st.title("Predicción del nivel de estrés mediante aprendizaje automático")
    st.text("Reyna Sarahí Carbajal Holguín " )
    st.text("391376")
    st.text("Universidad Autónoma de Chihuahua")

    st.divider()
    

    st.write(f"¡Hola! Te damos la bienvenida. En este espacio tendrás acceso a distintos modelos de predición sobre el nivel de estrés de acuerdo a unas preguntas sencillas.")
    st.write(f"Recuerda que esto no es un **{"diagnóstico"}**.")
    st.divider()

    st.write("A la izquierda, tienes un menú de opciones para manejarte dentro de la página. Puedes seleccionar la página principal o iniciar alguna predicción con el modelo de tu preferenica. ")
    st.write("Abajo te dejamos una descripción de lo que son los modelos de Machine Learning")

    st.subheader("Modelos de Predicción")
    st.write("Los modelos de machine learning son algoritmos que pueden identificar patrones o hacer predicciones sobre conjuntos de datos no vistos. A diferencia de los programas basados en reglas, estos modelos no tienen que codificarse explícitamente y pueden evolucionar con el tiempo a medida que entran nuevos datos en el sistema.")
    st.write("Los modelos de machine learning (ML) en inteligencia artificial (IA) permiten a las computadoras aprender a partir de datos y realizar predicciones o juicios sin necesidad de programación explícita. " \
    "Los modelos son la inspiración detrás de desarrollos revolucionarios en el mundo en constante cambio de la tecnología.")
    st.divider()
   



def categorize_mood(level):
    if level == "Happy":
        return 0
    elif level == "Neutral":
        return 1
    else:
        return 2

def categorize_BMI(level):
    if level == "Normal":
        return 0
    elif level == "Underweight":
        return 1
    elif level == "Overweight":
        return 2
    else:
        return 3

def Modelo1():
    st.title("Regresión Logística")
    model1 = joblib.load('C:/Users/reyna/Desktop/modelos/modelos/regresionlogistica_sinajuste.pkl')

    workload = st.slider("Nivel de Carga de Trabajo (1-10)", 1, 10, 5)
    heart_rate = st.slider("Frecuencia Cardíaca (bpm)", 40, 180, 70)
    physical_activity = st.slider("Nivel de Actividad Física (minutos por día)", 0, 180, 30)
    sleep = st.slider("Horas de Sueño", 0, 24, 7)
    mood = st.selectbox("Estado de Ánimo", ["Happy", "Neutral", "Sad"])
    bmi = st.selectbox("Categoría de BMI", ["Underweight", "Normal", "Overweight", "Obese"])
    
    input_data = pd.DataFrame({
    'Workload': [workload],
    'HeartRate': [heart_rate],
    'PhysicalActivity_Minutes': [physical_activity],
    'Sleep': [sleep],
    'Mood': [categorize_mood(mood)],
    'BMI': [categorize_BMI(bmi)]
    })

    if st.button('Predecir'):
        prediction = model1.predict(input_data)  
        st.write(f"El nivel de estrés estimado es: {prediction[0]}")

    




def Modelo2():
    st.title("Support Vector Machine")
    
    model2 = joblib.load("C:/Users/reyna/Desktop/modelos/modelo_svm.pkl")
    
    label_mapping = {
        0: "bajo",
        1: "medio",
        2: "alto"
    }

    workload = st.slider("Nivel de Carga de Trabajo (1-10)", 1, 10, 5)
    heart_rate = st.slider("Frecuencia Cardíaca (bpm)", 40, 180, 70)
    physical_activity = st.slider("Nivel de Actividad Física (minutos por día)", 0, 180, 30)
    sleep = st.slider("Horas de Sueño", 0, 24, 7)
    mood = st.selectbox("Estado de Ánimo", ["Happy", "Neutral", "Sad"])
    bmi = st.selectbox("Categoría de BMI", ["Underweight", "Normal", "Overweight", "Obese"])
    
    input_data = pd.DataFrame({
    'Workload': [workload],
    'HeartRate': [heart_rate],
    'PhysicalActivity_Minutes': [physical_activity],
    'Sleep': [sleep],
    'Mood': [categorize_mood(mood)],
    'BMI': [categorize_BMI(bmi)]
    })

    if st.button('Predecir'):
        prediction = model2.predict(input_data)  
        st.write(f"El nivel de estrés estimado es: {prediction[0]}")
    



def Modelo3():
    model3 = joblib.load('C:/Users/reyna/tree_model.pkl')
    st.title("Predicción de Nivel de Estrés segun el modelo de Random Forest") 

    workload = st.slider("Nivel de Carga de Trabajo (1-10)", 1, 10, 5)
    heart_rate = st.slider("Frecuencia Cardíaca (bpm)", 40, 180, 70)
    physical_activity = st.slider("Nivel de Actividad Física (minutos por día)", 0, 180, 30)
    sleep = st.slider("Horas de Sueño", 0, 24, 7)
    mood = st.selectbox("Estado de Ánimo", ["Happy", "Neutral", "Sad"])
    bmi = st.selectbox("Categoría de BMI", ["Underweight", "Normal", "Overweight", "Obese"])
    
    input_data = pd.DataFrame({
    'Workload': [workload],
    'HeartRate': [heart_rate],
    'PhysicalActivity_Minutes': [physical_activity],
    'Sleep': [sleep],
    'Mood': [categorize_mood(mood)],
    'BMI': [categorize_BMI(bmi)]
    })

    if st.button('Predecir'):
        prediction = model3.predict(input_data)  
        st.write(f"El nivel de estrés estimado es: {prediction[0]}")

def Modelo4():
    model4 = joblib.load('C:/Users/reyna/Desktop/modelos/modelos/modelo5_ajustado.pkl')
    st.title("Predicción de Nivel de Estrés según el ensamble de Adaboost") 

    workload = st.slider("Nivel de Carga de Trabajo (1-10)", 1, 10, 5)
    heart_rate = st.slider("Frecuencia Cardíaca (bpm)", 40, 180, 70)
    physical_activity = st.slider("Nivel de Actividad Física (minutos por día)", 0, 180, 30)
    sleep = st.slider("Horas de Sueño", 0, 24, 7)
    mood = st.selectbox("Estado de Ánimo", ["Happy", "Neutral", "Sad"])
    bmi = st.selectbox("Categoría de BMI", ["Underweight", "Normal", "Overweight", "Obese"])
    
    input_data = pd.DataFrame({
    'Workload': [workload],
    'HeartRate': [heart_rate],
    'PhysicalActivity_Minutes': [physical_activity],
    'Sleep': [sleep],
    'Mood': [categorize_mood(mood)],
    'BMI': [categorize_BMI(bmi)]
    })

    if st.button('Predecir'):
        prediction = model4.predict(input_data)  
        st.write(f"El nivel de estrés estimado es: {prediction[0]}")
    
    








st.sidebar.title("Navegacion")
pagina = st.sidebar.selectbox("Selecciona un modelo", ["Página Principal",
                                                       "Regresion Logistica"
                                                       ,"Support Vector Machine",
                                                       "Random Forest",
                                                       "Ensamble Adaboost"
                                                       ])


if pagina == "Regresion Logistica":
    Modelo1()
elif pagina == "Support Vector Machine":
    Modelo2()
elif pagina == "Random Forest":
    Modelo3()
elif pagina == "Ensamble Adaboost":
    Modelo4()
elif pagina == "Página Principal":
    pagina_principal()

