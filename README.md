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

- Python 3.6+
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

1. Run the Streamlit application:
```bash
streamlit run arnes.py
```

2. Use the slider to select your dog's harness size (in cm)
3. Enter the boot size you're considering in the text input
4. Click "Check" to get feedback on your selection

## File Structure

- `arnes.py`: Original Streamlit application code
- `arnes_refactored.py`: Refactored version with improved structure and maintainability
- `avalanche_dog_boot_model.pkl`: Pre-trained model file (required for predictions)
- `requirements.txt`: Python dependencies
- `README.md`: This file
- `REFACTORING_CHANGES.md`: Documentation of refactoring improvements
- `IMPROVEMENTS_SUMMARY.md`: Summary of improvements made to the original code

## Language

The application is in Spanish, with the title "Compra de Arneses y Botas para perros" (Dog Harness and Boot Purchase).

## Model Information

The application uses a pre-trained model stored in `avalanche_dog_boot_model.pkl` to predict appropriate boot sizes. The model was trained to understand the relationship between harness sizes and optimal boot sizes for dogs.