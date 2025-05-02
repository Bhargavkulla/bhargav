# tests/test_app.py
import pytest
from app.app import app  # Ensure that the correct app is imported from the right location

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, world!"
