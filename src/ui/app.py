# -*- coding: utf-8 -*-
"""
Streamlit Application Module

Este módulo contiene la aplicación principal de Streamlit para la tienda
de arneses y botas para perros.
"""

import streamlit as st
from typing import Optional, Dict, Any

# Importar módulos del paquete src
import sys
import os

# Asegurar que el directorio padre esté en el path para importar src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.model_loader import load_model, predict_boot_size
from src.utils.validators import validate_harness_size, validate_boot_size
from src.utils.size_checker import check_size_compatibility


@st.cache_resource
def get_cached_model() -> Optional[Any]:
    '''
    Esta función carga un modelo preentrenado y lo mantiene en caché
    para mejorar el rendimiento.
    
    Returns:
        Optional[Any]: El modelo cargado o None si ocurre un error.
    '''
    return load_model()


def load_model_and_predict(harness_size: float) -> Optional[float]:
    '''
    Esta función carga un modelo preentrenado. Utiliza el modelo
    con el tamaño del arnés del perro del cliente para predecir el 
    tamaño de botas que se ajustarán a ese perro.

    Args:
        harness_size (float): El tamaño del arnés, en cm 
    
    Returns:
        Optional[float]: El tamaño de bota predicho o None si ocurre un error.
    '''
    # Cargamos el modelo desde el archivo (usando caché)
    loaded_model = get_cached_model()
    
    if loaded_model is None:
        return None

    # Usar la función de predicción del módulo model_loader
    return predict_boot_size(loaded_model, harness_size)


def display_feedback(result: Dict[str, Any]) -> None:
    '''
    Muestra el feedback al usuario según el resultado de la verificación.
    
    Args:
        result (Dict[str, Any]): Diccionario con status, message e is_valid
    '''
    status = result['status']
    message = result['message']
    
    if status == 'success':
        st.success(message)
    elif status == 'warning':
        st.warning(message)
    elif status == 'error':
        st.error(message)


def run_app() -> None:
    '''
    Función principal que ejecuta la aplicación Streamlit.
    '''
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
        
        arnes = col1.slider(
            label='Tamaño del arnés (cm):', 
            min_value=1, 
            max_value=100, 
            value=30, 
            help="Mida la circunferencia del pecho de su perro"
        )
        botas = col2.text_input(
            label='Tamaño de la Bota:', 
            help="Ingrese el tamaño de las botas que desea comprar"
        )
        submit = st.form_submit_button(label='Check', type='primary')
        
        if submit:
            # Validar entrada de botas
            is_valid_boot, boot_size_value, boot_error = validate_boot_size(botas)
            
            if not is_valid_boot:
                st.error(boot_error)
            else:
                # Validar tamaño del arnés
                is_valid_harness, harness_error = validate_harness_size(arnes)
                
                if not is_valid_harness:
                    st.error(harness_error)
                else:
                    # Estimar la talla de la bota
                    estimated_boot_size = load_model_and_predict(arnes)

                    if estimated_boot_size is None:
                        st.error("No se pudo realizar la predicción. Por favor, inténtelo de nuevo más tarde.")
                    else:
                        # Verificar compatibilidad de tallas
                        result = check_size_compatibility(
                            selected_harness_size=arnes,
                            selected_boot_size=boot_size_value,
                            estimated_boot_size=estimated_boot_size
                        )
                        
                        # Mostrar feedback al usuario
                        display_feedback(result)


# Punto de entrada principal cuando se ejecuta como script
if __name__ == '__main__':
    run_app()
