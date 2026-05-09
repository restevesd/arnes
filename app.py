# -*- coding: utf-8 -*-
"""
Punto de entrada principal para la aplicación Streamlit.

Este archivo sirve como script principal para ejecutar la aplicación
de predicción de tallas de botas para perros.

Uso:
    streamlit run app.py
"""

import sys
import os

# Asegurar que el directorio actual esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.ui.app import run_app

if __name__ == '__main__':
    run_app()
