# -*- coding: utf-8 -*-
"""
Size Checker Module

Este módulo contiene funciones para verificar la compatibilidad entre
el tamaño de arnés y el tamaño de botas seleccionado.
"""

from typing import Optional, Dict, Any


def check_size_compatibility(
    selected_harness_size: float,
    selected_boot_size: float,
    estimated_boot_size: float
) -> Dict[str, Any]:
    '''
    Verifica si el tamaño de bota seleccionado es apropiado para el perro.
    
    Args:
        selected_harness_size (float): El tamaño del arnés seleccionado por el cliente.
        selected_boot_size (float): El tamaño de las botas que el cliente quiere comprar.
        estimated_boot_size (float): El tamaño de bota estimado por el modelo.
    
    Returns:
        Dict[str, Any]: Diccionario con:
            - 'status': 'success', 'warning', o 'error'
            - 'message': Mensaje para mostrar al usuario
            - 'is_valid': True si la selección es aceptable, False en caso contrario
    '''
    # Redondea al número entero más cercano porque no vendemos tallas parciales
    estimated_boot_size_rounded = int(round(estimated_boot_size))
    selected_boot_size_rounded = int(round(selected_boot_size))
    
    # Verificar si el tamaño de la bota es el apropiado
    if selected_boot_size_rounded == estimated_boot_size_rounded:
        return {
            'status': 'success',
            'message': f"¡Gran elección! Creemos que estas botas (tamaño {selected_boot_size_rounded}) "
                      f"se adaptarán bien a su perro. La talla estimada óptima es {estimated_boot_size_rounded}.",
            'is_valid': True
        }
    
    if selected_boot_size_rounded < estimated_boot_size_rounded:
        # Las botas seleccionadas podrían ser muy pequeñas 
        size_diff = estimated_boot_size_rounded - selected_boot_size_rounded
        if size_diff == 1:
            return {
                'status': 'warning',
                'message': f"Las botas que has seleccionado podrían ser un poco PEQUEÑAS para un perro "
                          f"tan grande como el suyo. Recomendamos considerar botas de tamaño {estimated_boot_size_rounded}.",
                'is_valid': True  # Advertencia pero permite continuar
            }
        else:
            return {
                'status': 'error',
                'message': f"Las botas que has seleccionado ({selected_boot_size_rounded}) podrían ser "
                          f"DEMASIADO PEQUEÑAS para un perro tan grande como el suyo. "
                          f"Recomendamos unas botas de tamaño {estimated_boot_size_rounded}.",
                'is_valid': False
            }
    
    if selected_boot_size_rounded > estimated_boot_size_rounded:
        # Las botas seleccionadas podrían ser muy grandes 
        size_diff = selected_boot_size_rounded - estimated_boot_size_rounded
        if size_diff == 1:
            return {
                'status': 'warning',
                'message': f"Las botas que has seleccionado podrían ser un poco GRANDES para un perro "
                          f"tan pequeño como el suyo. Recomendamos considerar botas de tamaño {estimated_boot_size_rounded}.",
                'is_valid': True  # Advertencia pero permite continuar
            }
        else:
            return {
                'status': 'error',
                'message': f"Las botas que has seleccionado ({selected_boot_size_rounded}) podrían ser "
                          f"DEMASIADO GRANDES para un perro tan pequeño como el suyo. "
                          f"Recomendamos unas botas de tamaño {estimated_boot_size_rounded}.",
                'is_valid': False
            }
    
    # Caso por defecto (no debería llegar aquí)
    return {
        'status': 'error',
        'message': "No se pudo determinar la compatibilidad de tallas.",
        'is_valid': False
    }


def get_size_feedback(status: str, message: str) -> str:
    '''
    Obtiene el feedback formateado según el estado.
    
    Args:
        status (str): El estado ('success', 'warning', 'error')
        message (str): El mensaje a mostrar
    
    Returns:
        str: El mensaje formateado
    '''
    return message
