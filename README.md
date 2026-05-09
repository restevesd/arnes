# Dog Harness and Boot Size Predictor

A Streamlit web application that helps customers select the appropriate boot size for their dogs based on harness size measurements.

## Overview

This application uses a pre-trained machine learning model to predict the optimal boot size for a dog based on its harness size. The tool helps ensure customers select properly-fitting boots for their pets by comparing the selected boot size against the model's prediction.

## Features

- Interactive slider for selecting harness size
- Input field for entering boot size
- Real-time validation of boot size appropriateness
- Visual feedback with success/error messages
- Automatic size recommendation

## How It Works

1. The user inputs their dog's harness size using the slider
2. The user enters the boot size they're considering purchasing
3. The application loads a pre-trained model and predicts the optimal boot size
4. The application compares the selected size with the predicted size
5. Feedback is provided to help the user make an appropriate selection

## Requirements

- Python 3.8+
- Streamlit
- joblib
- statsmodels
- pandas

## Installation

1. Clone or download this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Recommended (New Structure)

Run the application using the new modular structure:

```bash
streamlit run app.py
```

### Legacy Mode

You can still run the original monolithic version:

```bash
streamlit run arnes.py
```

### Using the Application

1. Use the slider to select your dog's harness size (in cm)
2. Enter the boot size you're considering in the text input
3. Click "Check" to get feedback on your selection

## Project Structure

```
├── app.py                      # Main entry point for the Streamlit app
├── arnes.py                    # Legacy monolithic application (maintained for compatibility)
├── avalanche_dog_boot_model.pkl # Pre-trained model file
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── docs/                       # Documentation
│   └── README.md               # Additional documentation
└── src/                        # Source code modules
    ├── __init__.py             # Package initialization
    ├── models/                 # Machine learning logic
    │   ├── __init__.py
    │   └── predictor.py        # Model prediction functions
    ├── utils/                  # Utility functions and validators
    │   ├── __init__.py
    │   └── validators.py       # Input validation and business logic
    └── ui/                     # User interface components
        ├── __init__.py
        └── components.py       # Streamlit UI components
```

## Language

The application is in Spanish, with the title "Compra de Arneses y Botas para perros" (Dog Harness and Boot Purchase).

## Model Information

The application uses a pre-trained model stored in `avalanche_dog_boot_model.pkl` to predict appropriate boot sizes. The model was trained to understand the relationship between harness sizes and optimal boot sizes for dogs.

## Architecture

This project has been restructured following best practices:

- **Separation of Concerns**: Code is organized into specialized modules (models, utils, ui)
- **Type Safety**: Full type hints throughout the codebase
- **Documentation**: Comprehensive docstrings for all functions and classes
- **Error Handling**: Structured error handling with custom exceptions
- **Maintainability**: Modular design makes the code easier to test and extend

## Development

To contribute or extend the application:

1. Add new features in the appropriate module under `src/`
2. Update tests as needed
3. Ensure type hints are added for all new code
4. Update documentation in `docs/`

## License

[Add your license information here]
