import pytest
from unittest.mock import MagicMock
from bson import ObjectId
from datetime import datetime

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
        "hire_date": datetime.now()
    }
    
    result = employee_helper(mock_employee)
    
    assert result["name"] == "Test User"
    assert result["email"] == "test@example.com"
    assert result["department"] == "IT"
    assert result["position"] == "Developer"
    assert result["salary"] == 50000
    assert "id" in result
    assert isinstance(result["id"], str)
    assert "hire_date" in result

def test_employee_helper_with_string_id():
    """Test employee helper with string ObjectId"""
    object_id = ObjectId()
    mock_employee = {
        "_id": object_id,
        "name": "Test User 2",
        "email": "test2@example.com",
        "department": "HR",
        "position": "Manager",
        "salary": 60000,
        "hire_date": datetime.now()
    }
    
    result = employee_helper(mock_employee)
    assert result["id"] == str(object_id)
