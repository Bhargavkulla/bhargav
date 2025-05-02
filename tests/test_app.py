import sys
import os
from app.main import app
import pytest

# Add the 'app' directory to the system path so it can be imported correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_app():
    # Test if the Flask app is created successfully
    assert app is not None
