import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from bson import ObjectId

from main import app

client = TestClient(app)

@patch('main.employees_collection')
def test_full_employee_lifecycle(mock_collection):
    """Test complete CRUD operations"""
    employee_id = str(ObjectId())
    
    # Mock create
    mock_collection.find_one.return_value = None  # No existing employee
    mock_collection.insert_one.return_value.inserted_id = ObjectId(employee_id)
    
    test_employee = {
        "name": "Integration Test User",
        "email": "integration@test.com",
        "salary": 60000,
        "position": "Tester",
        "department": "QA"
    }
    
    # Mock the employee data for subsequent operations
    employee_data = {
        "_id": ObjectId(employee_id),
        **test_employee,
        "hire_date": "2024-01-01"
    }
    
    # Create employee
    mock_collection.find_one.return_value = employee_data
    response = client.post("/employees", json=test_employee)
    assert response.status_code == 201
    
    # Get employee
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["name"] == test_employee["name"]
    
    # Update employee
    mock_collection.update_one.return_value = None
    response = client.put(f"/employees/{employee_id}", json={"salary": 65000})
    assert response.status_code == 200
    
    # Delete employee
    mock_collection.delete_one.return_value = None
    response = client.delete(f"/employees/{employee_id}")
    assert response.status_code == 200