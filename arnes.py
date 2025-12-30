# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 00:33:13 2021

@author: info
"""

import streamlit as st
import joblib
import os

model_filename = 'avalanche_dog_boot_model.pkl'

@st.cache_resource
def load_model():
    '''
    Esta función carga un modelo preentrenado y lo mantiene en caché
    para mejorar el rendimiento.
    '''
    try:
        loaded_model = joblib.load(model_filename)
        return loaded_model
    except FileNotFoundError:
        st.error(f"¡Archivo del modelo '{model_filename}' no encontrado!")
        return None
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None

def load_model_and_predict(harness_size):
    '''
    Esta función carga un modelo preentrenado. Utiliza el modelo
    con el tamaño del arnés del perro del cliente para predecir el 
    tamaño de botas que se ajustarán a ese perro.

    harness_size: El tamaño del arnés, en cm 
    '''
    
    # Cargamos el modelo desde el archivo (usando caché)
    loaded_model = load_model()
    
    if loaded_model is None:
        return None

    # Preparar los datos de entrada para el modelo
    inputs = { 'harness_size' : [harness_size] }

    try:
        # Usamos el modelo para hacer predicciones
        predicted_boot_size = loaded_model.predict(inputs)[0] #devuelve una serie, usamos el [0] para que me de el valor de la celda con el resultado
        return predicted_boot_size
    except Exception as e:
        st.error(f"Error al realizar la predicción: {e}")
        return None

def check_size_of_boots(selected_harness_size, selected_boot_size):
    '''
    Calcula si el cliente ha elegido un par de botas para perros que 
    son de una talla razonable.
    
    Esto funciona estimando el tamaño real de la bota del perro 
    del perro a partir de su talla de arnés.

    Esto devuelve un mensaje para el cliente que debe mostrarse antes de que
    de completar el pago. 

    selected_harness_size: El tamaño del arnés que el cliente quiere comprar
    selected_boot_size: El tamaño de las botas que el cliente quiere comprar
    '''

    # Validar que el tamaño del arnés esté en un rango razonable
    if selected_harness_size <= 0 or selected_harness_size > 100:
        return st.error("Por favor, ingrese un tamaño de arnés válido (mayor a 0 y menor o igual a 100 cm).")

    # Validar que el tamaño de las botas sea un número válido
    try:
        selected_boot_size = float(selected_boot_size)
        if selected_boot_size <= 0:
            return st.error("Por favor, ingrese un tamaño de bota válido (mayor a 0).")
    except ValueError:
        return st.error("Por favor, ingrese un tamaño de bota válido (número).")

    # Estimar la talla de la bota del perro del cliente
    estimated_boot_size = load_model_and_predict(selected_harness_size)

    if estimated_boot_size is None:
        return st.error("No se pudo realizar la predicción. Por favor, inténtelo de nuevo más tarde.")

    # Redondea al número entero más cercano porque no vendemos tallas parciales
    estimated_boot_size = int(round(estimated_boot_size))
    selected_boot_size = int(round(selected_boot_size))

    # Verificar si el tamaño de la bota es el apropiado
    if selected_boot_size == estimated_boot_size:
        # Las botas probablemente están OK
        return st.success(f"¡Gran elección! Creemos que estas botas (tamaño {selected_boot_size}) se adaptarán bien a su perro. La talla estimada óptima es {estimated_boot_size}.")

    if selected_boot_size < estimated_boot_size:
        # Las botas seleccionadas podrían ser muy pequeñas 
        size_diff = estimated_boot_size - selected_boot_size
        if size_diff == 1:
            return st.warning(f"Las botas que has seleccionado podrían ser un poco PEQUEÑAS para un perro tan grande como el suyo. Recomendamos considerar botas de tamaño {estimated_boot_size}.")
        else:
            return st.error(f"Las botas que has seleccionado ({selected_boot_size}) podrían ser DEMASIADO PEQUEÑAS para un perro tan grande como el suyo. Recomendamos unas botas de tamaño {estimated_boot_size}.")

    if selected_boot_size > estimated_boot_size:
        # Las botas selecionadas podrian ser muy grandes 
        size_diff = selected_boot_size - estimated_boot_size
        if size_diff == 1:
            return st.warning(f"Las botas que has seleccionado podrían ser un poco GRANDES para un perro tan pequeño como el suyo. Recomendamos considerar botas de tamaño {estimated_boot_size}.")
        else:
            return st.error(f"Las botas que has seleccionado ({selected_boot_size}) podrían ser DEMASIADO GRANDES para un perro tan pequeño como el suyo. Recomendamos unas botas de tamaño {estimated_boot_size}.")

 
st.title('Compra de Arneses y Botas para perros')
st.header("Tienda RED")
st.subheader("Ingrese los datos de su perro")

# Información adicional para el usuario
with st.expander("¿Cómo medir el tamaño del arnés?"):
    st.write("""
    - Mida la circunferencia del pecho del perro, detrás de las patas delanteras
    - Asegúrese de que la cinta métrica esté ajustada pero no apretada
    - La medida debe estar en centímetros
    """)

with st.form(key='dog-boot-pred-form'):
    col1, col2 = st.columns(2)
    
    arnes = col1.slider(label='Tamaño del arnés (cm):', min_value=1, max_value=100, value=30, help="Mida la circunferencia del pecho de su perro")
    botas = col2.text_input(label='Tamaño de la Bota:', help="Ingrese el tamaño de las botas que desea comprar")
    submit = st.form_submit_button(label='Check', type='primary')
    
    if submit:
        if botas.strip() == "":
            st.error("Por favor, ingrese un tamaño de bota.")
        else:
            check_size_of_boots(selected_harness_size=arnes, selected_boot_size=botas)