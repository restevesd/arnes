# -*- coding: utf-8 -*-
"""
Validators Module

Este módulo contiene funciones para validar las entradas del usuario.
"""

from typing import Tuple, Optional


def validate_harness_size(harness_size: float) -> Tuple[bool, Optional[str]]:
    '''
    Valida que el tamaño del arnés esté en un rango razonable.
    
    Args:
        harness_size (float): El tamaño del arnés en centímetros.
    
    Returns:
        Tuple[bool, Optional[str]]: 
            - True y None si es válido
            - False y mensaje de error si no es válido
    '''
    if harness_size <= 0 or harness_size > 100:
        return False, "Por favor, ingrese un tamaño de arnés válido (mayor a 0 y menor o igual a 100 cm)."
    
    return True, None


def validate_boot_size(boot_size_input: str) -> Tuple[bool, Optional[float], Optional[str]]:
    '''
    Valida que el tamaño de las botas sea un número válido.
    
    Args:
        boot_size_input (str): El tamaño de las botas como string.
    
    Returns:
        Tuple[bool, Optional[float], Optional[str]]:
            - True, valor_float, None si es válido
            - False, None, mensaje de error si no es válido
    '''
    if not boot_size_input or boot_size_input.strip() == "":
        return False, None, "Por favor, ingrese un tamaño de bota."
    
    try:
        boot_size = float(boot_size_input.strip())
        if boot_size <= 0:
            return False, None, "Por favor, ingrese un tamaño de bota válido (mayor a 0)."
        return True, boot_size, None
    except ValueError:
        return False, None, "Por favor, ingrese un tamaño de bota válido (número)."
