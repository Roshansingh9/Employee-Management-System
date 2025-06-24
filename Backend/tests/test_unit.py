import pytest
from unittest.mock import MagicMock, patch
from bson import ObjectId

# Import after environment setup
from main import employee_helper

def test_employee_helper():
    """Test the employee helper function"""
    mock_employee = {
        "_id": ObjectId(),
        "name": "Test User",
        "email": "test@example.com",
        "department": "IT",
        "position": "Developer",
        "salary": 50000,
        "hire_date": "2024-01-01"
    }
    
    result = employee_helper(mock_employee)
    
    assert result["name"] == "Test User"
    assert result["email"] == "test@example.com"
    assert "id" in result
    assert isinstance(result["id"], str)

@patch('main.employees_collection')
def test_create_employee_duplicate_email(mock_collection):
    """Test creating employee with duplicate email"""
    from fastapi.testclient import TestClient
    from main import app
    
    client = TestClient(app)
    
    # Mock existing employee with same email
    mock_collection.find_one.return_value = {
        "_id": ObjectId(),
        "email": "test@example.com"
    }
    
    test_emp = {
        "name": "Test User",
        "email": "test@example.com",
        "salary": 50000,
        "position": "Developer",
        "department": "IT"
    }
    
    response = client.post("/employees", json=test_emp)
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]