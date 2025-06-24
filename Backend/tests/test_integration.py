# tests/test_integration.py
import pytest
from fastapi.testclient import TestClient
from main import app
from employee import get_database

client = TestClient(app)

# Optional: point to a test DB using .env or monkeypatching
db = get_database()

def test_add_and_get_employee():
    emp = {"name": "Test User", "email": "test@user.com", "salary": 5000, "position": "Intern", "department": "Dev", "hire_date": "2023-01-01"}
    r = client.post("/employees", json=emp)
    assert r.status_code == 200

    r2 = client.get(f"/employees/{emp['email']}")
    assert r2.status_code == 200
    assert r2.json()["email"] == emp["email"]
