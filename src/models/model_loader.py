# -*- coding: utf-8 -*-
"""
Model Loader Module

Este módulo se encarga de cargar y gestionar el modelo de machine learning
para predecir el tamaño de botas para perros.
"""

import joblib
import os
from typing import Optional, Dict, Any

# Ruta del archivo del modelo
MODEL_FILENAME = 'avalanche_dog_boot_model.pkl'


def load_model(model_path: str = MODEL_FILENAME) -> Optional[Any]:
    '''
    Carga un modelo preentrenado desde un archivo.
    
    Args:
        model_path (str): Ruta al archivo del modelo. Por defecto es 
                         'avalanche_dog_boot_model.pkl'
    
    Returns:
        Optional[Any]: El modelo cargado o None si ocurre un error.
    
    Raises:
        FileNotFoundError: Si el archivo del modelo no existe.
        Exception: Si ocurre cualquier otro error durante la carga.
    '''
    try:
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Archivo del modelo '{model_path}' no encontrado")
        
        loaded_model = joblib.load(model_path)
        return loaded_model
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None


def predict_boot_size(model: Any, harness_size: float) -> Optional[float]:
    '''
    Utiliza el modelo para predecir el tamaño de bota basado en el tamaño del arnés.
    
    Args:
        model (Any): El modelo de machine learning cargado.
        harness_size (float): El tamaño del arnés en centímetros.
    
    Returns:
        Optional[float]: El tamaño de bota predicho o None si ocurre un error.
    
    Raises:
        Exception: Si ocurre un error durante la predicción.
    '''
    try:
        # Preparar los datos de entrada para el modelo
        inputs: Dict[str, list] = {'harness_size': [harness_size]}
        
        # Usamos el modelo para hacer predicciones
        predicted_boot_size = model.predict(inputs)[0]
        return float(predicted_boot_size)
    
    except Exception as e:
        print(f"Error al realizar la predicción: {e}")
        return None
