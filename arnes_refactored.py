# -*- coding: utf-8 -*-
"""
Dog Harness and Boot Size Predictor - Refactored Version

This application helps customers select the appropriate boot size for their dogs
based on harness size measurements using a pre-trained ML model.
"""

import streamlit as st
import joblib
import os
from typing import Optional, Tuple, Union


class DogBootSizePredictor:
    """
    A class to handle dog boot size predictions based on harness size.
    """
    
    def __init__(self, model_filename: str = 'avalanche_dog_boot_model.pkl'):
        """
        Initialize the predictor with the model file path.
        
        Args:
            model_filename: Path to the pre-trained model file
        """
        self.model_filename = model_filename
        self._model = None
    
    @st.cache_resource
    def _load_model(self):
        """
        Load the pre-trained model and cache it for better performance.
        
        Returns:
            The loaded model or None if loading fails
        """
        try:
            loaded_model = joblib.load(self.model_filename)
            return loaded_model
        except FileNotFoundError:
            st.error(f"¡Archivo del modelo '{self.model_filename}' no encontrado!")
            return None
        except Exception as e:
            st.error(f"Error al cargar el modelo: {e}")
            return None
    
    def predict_boot_size(self, harness_size: float) -> Optional[float]:
        """
        Predict the optimal boot size based on harness size.
        
        Args:
            harness_size: The harness size in cm
            
        Returns:
            Predicted boot size or None if prediction fails
        """
        if self._model is None:
            self._model = self._load_model()
        
        if self._model is None:
            return None
        
        # Prepare input data for the model
        inputs = {'harness_size': [harness_size]}
        
        try:
            predicted_boot_size = self._model.predict(inputs)[0]
            return predicted_boot_size
        except Exception as e:
            st.error(f"Error al realizar la predicción: {e}")
            return None
    
    def validate_inputs(self, harness_size: float, boot_size_input: str) -> Tuple[bool, Optional[str]]:
        """
        Validate the user inputs.
        
        Args:
            harness_size: The harness size in cm
            boot_size_input: The boot size as string input from user
            
        Returns:
            A tuple of (is_valid, error_message)
        """
        # Validate harness size
        if harness_size <= 0 or harness_size > 100:
            return False, "Por favor, ingrese un tamaño de arnés válido (mayor a 0 y menor o igual a 100 cm)."
        
        # Validate boot size
        try:
            boot_size = float(boot_size_input)
            if boot_size <= 0:
                return False, "Por favor, ingrese un tamaño de bota válido (mayor a 0)."
        except ValueError:
            return False, "Por favor, ingrese un tamaño de bota válido (número)."
        
        return True, None
    
    def check_size_appropriateness(self, harness_size: float, boot_size_input: str) -> None:
        """
        Check if the selected boot size is appropriate for the harness size.
        
        Args:
            harness_size: The harness size in cm
            boot_size_input: The boot size as string input from user
        """
        # Validate inputs first
        is_valid, error_message = self.validate_inputs(harness_size, boot_size_input)
        if not is_valid:
            st.error(error_message)
            return
        
        boot_size = float(boot_size_input)
        
        # Get the estimated boot size
        estimated_boot_size = self.predict_boot_size(harness_size)
        if estimated_boot_size is None:
            st.error("No se pudo realizar la predicción. Por favor, inténtelo de nuevo más tarde.")
            return
        
        # Round to nearest integer as we don't sell partial sizes
        estimated_boot_size = int(round(estimated_boot_size))
        selected_boot_size = int(round(boot_size))
        
        # Check if the boot size is appropriate
        self._display_size_feedback(selected_boot_size, estimated_boot_size)
    
    def _display_size_feedback(self, selected_boot_size: int, estimated_boot_size: int) -> None:
        """
        Display feedback about the boot size appropriateness.
        
        Args:
            selected_boot_size: The boot size selected by the user
            estimated_boot_size: The estimated optimal boot size
        """
        if selected_boot_size == estimated_boot_size:
            # The boots are probably OK
            st.success(f"¡Gran elección! Creemos que estas botas (tamaño {selected_boot_size}) se adaptarán bien a su perro. La talla estimada óptima es {estimated_boot_size}.")
            return

        if selected_boot_size < estimated_boot_size:
            # The selected boots might be too small
            size_diff = estimated_boot_size - selected_boot_size
            if size_diff == 1:
                st.warning(f"Las botas que has seleccionado podrían ser un poco PEQUEÑAS para un perro tan grande como el suyo. Recomendamos considerar botas de tamaño {estimated_boot_size}.")
            else:
                st.error(f"Las botas que has seleccionado ({selected_boot_size}) podrían ser DEMASIADO PEQUEÑAS para un perro tan grande como el suyo. Recomendamos unas botas de tamaño {estimated_boot_size}.")
            return

        if selected_boot_size > estimated_boot_size:
            # The selected boots might be too large
            size_diff = selected_boot_size - estimated_boot_size
            if size_diff == 1:
                st.warning(f"Las botas que has seleccionado podrían ser un poco GRANDES para un perro tan pequeño como el suyo. Recomendamos considerar botas de tamaño {estimated_boot_size}.")
            else:
                st.error(f"Las botas que has seleccionado ({selected_boot_size}) podrían ser DEMASIADO GRANDES para un perro tan pequeño como el suyo. Recomendamos unas botas de tamaño {estimated_boot_size}.")


def setup_page():
    """Set up the Streamlit page configuration and title."""
    st.set_page_config(
        page_title="Compra de Arneses y Botas para perros",
        page_icon="🐾",
        layout="centered"
    )
    
    st.title('Compra de Arneses y Botas para perros')
    st.header("Tienda RED")
    st.subheader("Ingrese los datos de su perro")


def display_help_section():
    """Display the help section with instructions on how to measure harness size."""
    with st.expander("¿Cómo medir el tamaño del arnés?"):
        st.write("""
        - Mida la circunferencia del pecho del perro, detrás de las patas delanteras
        - Asegúrese de que la cinta métrica esté ajustada pero no apretada
        - La medida debe estar en centímetros
        """)


def create_input_form(predictor: DogBootSizePredictor):
    """Create the input form for harness and boot size."""
    with st.form(key='dog-boot-pred-form'):
        col1, col2 = st.columns(2)
        
        harness_size = col1.slider(
            label='Tamaño del arnés (cm):',
            min_value=1,
            max_value=100,
            value=30,
            help="Mida la circunferencia del pecho de su perro"
        )
        
        boot_size = col2.text_input(
            label='Tamaño de la Bota:',
            help="Ingrese el tamaño de las botas que desea comprar"
        )
        
        submit = st.form_submit_button(label='Check', type='primary')
        
        if submit:
            if boot_size.strip() == "":
                st.error("Por favor, ingrese un tamaño de bota.")
            else:
                predictor.check_size_appropriateness(harness_size, boot_size)


def main():
    """Main function to run the Streamlit application."""
    setup_page()
    display_help_section()
    predictor = DogBootSizePredictor()
    create_input_form(predictor)


if __name__ == "__main__":
    main()