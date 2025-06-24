# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

test_employee = {
    "name": "Roshan Singh",
    "email": "roshan@example.com",
    "salary": 50000,
    "position": "Engineer",
    "department": "AI",
    "hire_date": "2024-01-01"
}

def test_create_employee():
    r = client.post("/employees", json=test_employee)
    assert r.status_code == 200
    assert r.json()["msg"] == "Employee added successfully"

def test_get_employee():
    r = client.get(f"/employees/{test_employee['email']}")
    assert r.status_code == 200
    assert r.json()["email"] == test_employee["email"]

def test_update_employee():
    r = client.put(f"/employees/{test_employee['email']}", json={"salary": 55000})
    assert r.status_code == 200
    assert r.json()["msg"] == "Employee updated successfully"

def test_delete_employee():
    r = client.delete(f"/employees/{test_employee['email']}")
    assert r.status_code == 200
    assert r.json()["msg"] == "Employee deleted successfully"
