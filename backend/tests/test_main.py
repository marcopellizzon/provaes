import os
import sys
from fastapi.testclient import TestClient

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app


"""
Execute this test by running on the terminal (from the app/) the command:
pytest --cov=app --cov-report=html tests/
 """

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200

def test_total_waste():
    response = client.get("/total_waste/Comune1/2020")
    assert response.status_code == 200
    # Add more assertions based on expected response

def test_total_waste_all_years():
    response = client.get("/total_waste_all_years/Comune1")
    assert response.status_code == 200
    # Additional assertions

def test_find_municipalities_by_waste():
    response = client.get("/find_municipalities_by_waste?waste_amount=1000")
    assert response.status_code == 200
    # More assertions based on expected output

def test_invalid_input():
    response = client.get("/total_waste/InvalidComune/2020")
    assert response.status_code == 404
    # Or any other expected status code
