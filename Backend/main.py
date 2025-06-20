from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from typing import List

from database import get_employees_collection
from models import Employee, EmployeeUpdate, EmployeeResponse

app = FastAPI(
    title="Employee Management API",
    description="A simple API for managing employees",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get collection
employees_collection = get_employees_collection()

# Helper function to convert ObjectId to string
def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "email": employee["email"],
        "department": employee["department"],
        "position": employee["position"],
        "salary": employee["salary"],
        "hire_date": employee["hire_date"]
    }

# API Endpoints

@app.get("/")
def root():
    return {"message": "Employee Management API", "version": "1.0.0"}

@app.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee):
    """Create a new employee"""
    employee_dict = employee.dict()
    
    # Check if email already exists
    existing_employee = employees_collection.find_one({"email": employee.email})
    if existing_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee with this email already exists"
        )
    
    result = employees_collection.insert_one(employee_dict)
    new_employee = employees_collection.find_one({"_id": result.inserted_id})
    
    return employee_helper(new_employee)

@app.get("/employees", response_model=List[EmployeeResponse])
def get_all_employees():
    """Get all employees"""
    employees = []
    
    for employee in employees_collection.find():
        employees.append(employee_helper(employee))
    
    return employees

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: str):
    """Get a specific employee by ID"""
    if not ObjectId.is_valid(employee_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid employee ID format"
        )
    
    employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    
    return employee_helper(employee)

@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: str, employee_update: EmployeeUpdate):
    """Update an employee"""
    if not ObjectId.is_valid(employee_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid employee ID format"
        )
    
    # Check if employee exists
    existing_employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    if not existing_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    
    # Prepare update data
    update_data = {k: v for k, v in employee_update.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No data provided for update"
        )
    
    # Check email uniqueness if email is being updated
    if "email" in update_data:
        email_exists = employees_collection.find_one({
            "email": update_data["email"],
            "_id": {"$ne": ObjectId(employee_id)}
        })
        if email_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Employee with this email already exists"
            )
    
    # Update employee
    employees_collection.update_one(
        {"_id": ObjectId(employee_id)},
        {"$set": update_data}
    )
    
    # Return updated employee
    updated_employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    return employee_helper(updated_employee)

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: str):
    """Delete an employee"""
    if not ObjectId.is_valid(employee_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid employee ID format"
        )
    
    # Check if employee exists
    employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    
    # Delete employee
    employees_collection.delete_one({"_id": ObjectId(employee_id)})
    
    return {"message": "Employee deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)