# tests/test_app.py
import pytest
from app import app  # Updated import to directly refer to app.py

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, world!"
