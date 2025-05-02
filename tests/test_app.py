import sys
import os

# Add the 'app' directory (inside 'micro') to the system path so it can be imported correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.main import app
 
def test_app():
    # Test if the Flask app is created successfully
    assert app is not None
