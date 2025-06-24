from fastapi.testclient import TestClient
import pytest
from unittest.mock import patch, MagicMock
from bson import ObjectId

# Import after setting environment variable
from main import app

client = TestClient(app)

test_employee = {
    "name": "Roshan Singh",
    "email": "roshan@example.com",
    "salary": 50000,
    "position": "Engineer",
    "department": "AI"
}

@patch('main.employees_collection')
def test_create_employee(mock_collection):
    # Mock the database operations
    mock_collection.find_one.return_value = None  # No existing employee
    mock_collection.insert_one.return_value.inserted_id = ObjectId()
    mock_collection.find_one.return_value = {
        "_id": ObjectId(),
        **test_employee,
        "hire_date": "2024-01-01"
    }
    
    response = client.post("/employees", json=test_employee)
    assert response.status_code == 201
    assert response.json()["name"] == test_employee["name"]

@patch('main.employees_collection')
def test_get_all_employees(mock_collection):
    # Mock returning a list of employees
    mock_collection.find.return_value = [
        {
            "_id": ObjectId(),
            **test_employee,
            "hire_date": "2024-01-01"
        }
    ]
    
    response = client.get("/employees")
    assert response.status_code == 200
    assert len(response.json()) >= 0

@patch('main.employees_collection')
def test_get_employee_by_id(mock_collection):
    employee_id = str(ObjectId())
    mock_collection.find_one.return_value = {
        "_id": ObjectId(employee_id),
        **test_employee,
        "hire_date": "2024-01-01"
    }
    
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["name"] == test_employee["name"]

@patch('main.employees_collection')
def test_update_employee(mock_collection):
    employee_id = str(ObjectId())
    mock_collection.find_one.return_value = {
        "_id": ObjectId(employee_id),
        **test_employee,
        "hire_date": "2024-01-01"
    }
    mock_collection.update_one.return_value = None
    
    updated_data = {"salary": 55000}
    response = client.put(f"/employees/{employee_id}", json=updated_data)
    assert response.status_code == 200

@patch('main.employees_collection')
def test_delete_employee(mock_collection):
    employee_id = str(ObjectId())
    mock_collection.find_one.return_value = {
        "_id": ObjectId(employee_id),
        **test_employee,
        "hire_date": "2024-01-01"
    }
    mock_collection.delete_one.return_value = None
    
    response = client.delete(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Employee deleted successfully"