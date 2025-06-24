from fastapi.testclient import TestClient
import pytest
from unittest.mock import patch, MagicMock
from bson import ObjectId
from datetime import datetime

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
def test_root_endpoint(mock_collection):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Employee Management API"

@patch('main.employees_collection')
def test_create_employee(mock_collection):
    """Test creating a new employee"""
    # Create a proper ObjectId for the test
    employee_id = ObjectId()
    
    # Mock the response after insertion
    mock_employee_data = {
        "_id": employee_id,
        **test_employee,
        "hire_date": datetime.now()
    }
    
    # Set up the mock to handle the sequence of calls correctly
    mock_collection.find_one.side_effect = [
        None,  # First call: check for existing employee (should return None)
        mock_employee_data  # Second call: get the newly inserted employee
    ]
    mock_collection.insert_one.return_value.inserted_id = employee_id
    
    response = client.post("/employees", json=test_employee)
    assert response.status_code == 201
    assert response.json()["name"] == test_employee["name"]
    assert response.json()["email"] == test_employee["email"]

@patch('main.employees_collection')
def test_create_employee_duplicate_email(mock_collection):
    """Test creating employee with duplicate email"""
    # Mock existing employee with same email
    mock_collection.find_one.return_value = {
        "_id": ObjectId(),
        "email": test_employee["email"]
    }
    
    response = client.post("/employees", json=test_employee)
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

@patch('main.employees_collection')
def test_get_all_employees(mock_collection):
    """Test getting all employees"""
    # Mock returning a list of employees
    mock_collection.find.return_value = [
        {
            "_id": ObjectId(),
            **test_employee,
            "hire_date": datetime.now()
        }
    ]
    
    response = client.get("/employees")
    assert response.status_code == 200
    assert len(response.json()) >= 0

@patch('main.employees_collection')
def test_get_employee_by_id(mock_collection):
    """Test getting employee by ID"""
    employee_id = str(ObjectId())
    mock_collection.find_one.return_value = {
        "_id": ObjectId(employee_id),
        **test_employee,
        "hire_date": datetime.now()
    }
    
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["name"] == test_employee["name"]

@patch('main.employees_collection')
def test_get_employee_invalid_id(mock_collection):
    """Test getting employee with invalid ID"""
    response = client.get("/employees/invalid_id")
    assert response.status_code == 400
    assert "Invalid employee ID format" in response.json()["detail"]

@patch('main.employees_collection')
def test_get_employee_not_found(mock_collection):
    """Test getting non-existent employee"""
    employee_id = str(ObjectId())
    mock_collection.find_one.return_value = None
    
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 404
    assert "Employee not found" in response.json()["detail"]

@patch('main.employees_collection')
def test_update_employee(mock_collection):
    """Test updating an employee"""
    employee_id = str(ObjectId())
    original_employee = {
        "_id": ObjectId(employee_id),
        **test_employee,
        "hire_date": datetime.now()
    }
    updated_employee = {
        **original_employee,
        "salary": 55000
    }
    
    # Mock the sequence of calls for update
    mock_collection.find_one.side_effect = [
        original_employee,  # First call: check if employee exists
        updated_employee    # Second call: get updated employee
    ]
    mock_collection.update_one.return_value = None
    
    updated_data = {"salary": 55000}
    response = client.put(f"/employees/{employee_id}", json=updated_data)
    assert response.status_code == 200

@patch('main.employees_collection')
def test_update_employee_not_found(mock_collection):
    """Test updating non-existent employee"""
    employee_id = str(ObjectId())
    mock_collection.find_one.return_value = None
    
    response = client.put(f"/employees/{employee_id}", json={"salary": 55000})
    assert response.status_code == 404

@patch('main.employees_collection')
def test_delete_employee(mock_collection):
    """Test deleting an employee"""
    employee_id = str(ObjectId())
    mock_collection.find_one.return_value = {
        "_id": ObjectId(employee_id),
        **test_employee,
        "hire_date": datetime.now()
    }
    mock_collection.delete_one.return_value = None
    
    response = client.delete(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Employee deleted successfully"

@patch('main.employees_collection')
def test_delete_employee_not_found(mock_collection):
    """Test deleting non-existent employee"""
    employee_id = str(ObjectId())
    mock_collection.find_one.return_value = None
    
    response = client.delete(f"/employees/{employee_id}")
    assert response.status_code == 404