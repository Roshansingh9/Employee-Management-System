# tests/test_unit.py

from unittest.mock import MagicMock
from main import add_employee, get_employees, get_employee, update_employee, delete_employee

import pytest

@pytest.fixture
def mock_db():
    return MagicMock()

def test_add_employee(mock_db):
    mock_collection = mock_db["employee"]
    mock_collection.insert_one.return_value.inserted_id = "123"

    response = add_employee(mock_db, {"name": "Roshan", "email": "r@a.com"})
    assert response["msg"] == "Employee added successfully"
