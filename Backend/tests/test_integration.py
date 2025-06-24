import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from bson import ObjectId
from datetime import datetime

from main import app

client = TestClient(app)

@patch('main.employees_collection')
def test_full_employee_lifecycle(mock_collection):
    """Test complete CRUD operations"""
    employee_id = ObjectId()
    
    test_employee = {
        "name": "Integration Test User",
        "email": "integration@test.com",
        "salary": 60000,
        "position": "Tester",
        "department": "QA"
    }
    
    employee_data = {
        "_id": employee_id,
        **test_employee,
        "hire_date": datetime.now()
    }
    
    # Test Create Employee
    mock_collection.find_one.return_value = None  # No existing employee
    mock_collection.insert_one.return_value.inserted_id = employee_id
    mock_collection.find_one.return_value = employee_data
    
    response = client.post("/employees", json=test_employee)
    assert response.status_code == 201
    created_employee = response.json()
    
    # Test Get Employee
    response = client.get(f"/employees/{str(employee_id)}")
    assert response.status_code == 200
    assert response.json()["name"] == test_employee["name"]
    
    # Test Update Employee
    mock_collection.update_one.return_value = None
    updated_employee_data = {**employee_data, "salary": 65000}
    mock_collection.find_one.return_value = updated_employee_data
    
    response = client.put(f"/employees/{str(employee_id)}", json={"salary": 65000})
    assert response.status_code == 200
    
    # Test Get All Employees
    mock_collection.find.return_value = [updated_employee_data]
    response = client.get("/employees")
    assert response.status_code == 200
    assert len(response.json()) > 0
    
    # Test Delete Employee
    mock_collection.delete_one.return_value = None
    response = client.delete(f"/employees/{str(employee_id)}")
    assert response.status_code == 200
    assert response.json()["message"] == "Employee deleted successfully"

@patch('main.employees_collection')
def test_employee_validation(mock_collection):
    """Test employee data validation"""
    # Test missing required fields
    invalid_employee = {
        "name": "Test User"
        # Missing email, department, position, salary
    }
    
    response = client.post("/employees", json=invalid_employee)
    assert response.status_code == 422  # Validation error
    
    # Test invalid salary type
    invalid_employee2 = {
        "name": "Test User",
        "email": "test@example.com",
        "department": "IT",
        "position": "Developer",
        "salary": "not_a_number"
    }
    
    response = client.post("/employees", json=invalid_employee2)
    assert response.status_code == 422  # Validation error