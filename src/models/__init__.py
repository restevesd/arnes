"""
Models subpackage - Contiene el cargador del modelo de machine learning.
"""

from .model_loader import load_model, predict_boot_size

__all__ = ['load_model', 'predict_boot_size']
