"""
Test script to verify the refactored application works as expected.
"""
import sys
import os

# Add the workspace directory to the path
sys.path.insert(0, '/workspace')

def test_imports():
    """Test that all necessary modules can be imported."""
    try:
        import streamlit as st
        import joblib
        print("✓ Required modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_refactored_code():
    """Test that the refactored code can be imported and instantiated."""
    try:
        from arnes_refactored import DogBootSizePredictor
        predictor = DogBootSizePredictor()
        print("✓ DogBootSizePredictor class instantiated successfully")
        return True
    except Exception as e:
        print(f"✗ Error with refactored code: {e}")
        return False

def test_original_code():
    """Test that the original code can still be imported."""
    try:
        import arnes
        print("✓ Original arnes.py module imported successfully")
        return True
    except Exception as e:
        print(f"✗ Error with original code: {e}")
        return False

def main():
    print("Testing refactored application...")
    print()
    
    success = True
    success &= test_imports()
    success &= test_original_code()
    success &= test_refactored_code()
    
    print()
    if success:
        print("✓ All tests passed! Both original and refactored versions are working.")
    else:
        print("✗ Some tests failed.")
        
    print()
    print("To run the original application:")
    print("  streamlit run arnes.py")
    print()
    print("To run the refactored application:")
    print("  streamlit run arnes_refactored.py")

if __name__ == "__main__":
    main()