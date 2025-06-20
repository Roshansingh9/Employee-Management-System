from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Employee(BaseModel):
    name: str
    email: str
    department: str
    position: str
    salary: float
    hire_date: Optional[datetime] = Field(default_factory=datetime.now)

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None

class EmployeeResponse(BaseModel):
    id: str
    name: str
    email: str
    department: str
    position: str
    salary: float
    hire_date: datetime