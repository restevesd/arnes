# Documentación del Proyecto

## Estructura del Proyecto

```
/workspace/
├── app.py                      # Punto de entrada principal
├── arnes.py                    # Archivo original (mantenido por compatibilidad)
├── src/                        # Código fuente principal
│   ├── __init__.py            # Paquete principal
│   ├── models/                # Módulo de modelos de ML
│   │   ├── __init__.py
│   │   └── model_loader.py    # Carga y predicción del modelo
│   ├── utils/                 # Utilidades y validaciones
│   │   ├── __init__.py
│   │   ├── validators.py      # Validadores de entrada
│   │   └── size_checker.py    # Lógica de verificación de tallas
│   └── ui/                    # Interfaz de usuario
│       ├── __init__.py
│       └── app.py             # Aplicación Streamlit
├── avalanche_dog_boot_model.pkl  # Modelo preentrenado
├── requirements.txt           # Dependencias de Python
├── README.md                  # Documentación principal
└── .gitignore                 # Archivos ignorados por Git
```

## Módulos

### src.models
Contiene la lógica para cargar y utilizar el modelo de machine learning.

**Funciones principales:**
- `load_model()`: Carga el modelo desde un archivo pickle
- `predict_boot_size()`: Realiza predicciones usando el modelo

### src.utils
Contiene funciones utilitarias para validación y verificación.

**Módulos:**
- `validators`: Valida las entradas del usuario (tamaño de arnés y botas)
- `size_checker`: Compara el tamaño seleccionado con el tamaño estimado

### src.ui
Contiene la interfaz de usuario de Streamlit.

**Funciones principales:**
- `run_app()`: Ejecuta la aplicación completa
- `display_feedback()`: Muestra mensajes al usuario

## Uso

### Ejecutar la aplicación

```bash
streamlit run app.py
```

### Importar módulos

```python
from src.models import load_model, predict_boot_size
from src.utils import validate_harness_size, validate_boot_size
from src.utils import check_size_compatibility
```

## Pruebas

Para verificar que la instalación es correcta:

```bash
python -c "from src.models import load_model; print('Importación exitosa')"
```

## Migración desde la versión anterior

El archivo `arnes.py` se mantiene por compatibilidad, pero se recomienda usar
la nueva estructura modular. La funcionalidad es idéntica.
