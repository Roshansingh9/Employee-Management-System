# Employee Management System

## 🌐 Live Demo
**[View Live Application](https://keploy-assignment-2.vercel.app/)**

## 📖 Project Description
A full-stack web application for managing employee records with complete CRUD (Create, Read, Update, Delete) functionality. The application provides an intuitive interface for HR departments and managers to efficiently handle employee data, including personal information, job details, and salary management.

## 🛠️ Tech Stack

### Frontend
- **React.js** - JavaScript library for building user interfaces
- **Axios** - HTTP client for API requests
- **CSS3** - Styling and responsive design
- **Vercel** - Frontend deployment platform

### Backend
- **FastAPI 0.104.1** - Modern Python web framework for building APIs
- **MongoDB** - NoSQL database for data storage
- **PyMongo 4.6.0** - Python driver for MongoDB
- **Pydantic** - Data validation and settings management
- **Uvicorn 0.24.0** - ASGI server for FastAPI
- **python-dotenv 1.0.0** - Environment variable management
- **Render** - Backend deployment platform

### Testing Stack
- **pytest 7.4.3** - Main testing framework
- **pytest-cov 4.1.0** - Code coverage reporting
- **pytest-asyncio 0.21.1** - Async testing support
- **httpx 0.25.0** - HTTP client for API testing
- **unittest.mock** - Mocking and patching (Python standard library)

## 🚀 API Integration Details

### Integrated API: Employee Management REST API
The application integrates a custom-built REST API with the following endpoints:

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/` | API health check | API information |
| POST | `/employees` | Create new employee | Created employee data |
| GET | `/employees` | Get all employees | Array of employees |
| GET | `/employees/{id}` | Get specific employee | Single employee data |
| PUT | `/employees/{id}` | Update employee | Updated employee data |
| DELETE | `/employees/{id}` | Delete employee | Success message |

### Employee Data Model
```json
{
  "id": "string",
  "name": "string",
  "email": "string (unique)",
  "department": "string",
  "position": "string",
  "salary": "number",
  "hire_date": "datetime (auto-generated)"
}
```

## ✨ Features
- **Employee Registration** - Add new employees with comprehensive details
- **Employee Listing** - View all employees in a clean, organized grid layout
- **Real-time Updates** - Instant reflection of changes across the application
- **Employee Editing** - Update existing employee information seamlessly
- **Employee Deletion** - Remove employee records with confirmation prompts
- **Input Validation** - Client-side and server-side data validation
- **Email Uniqueness** - Prevents duplicate email addresses in the system
- **Responsive Design** - Optimized for desktop and mobile devices
- **Error Handling** - Comprehensive error messages and user feedback
- **Loading States** - Visual indicators during API operations

## ⚠️ **Note on Backend Hosting**
**The backend is hosted on Render's free tier. Due to cold start limitations, the first API request may take 1-2 minutes to respond. Subsequent requests will be much faster.**

## 🚀 Getting Started

### Prerequisites
- **Node.js** (v14 or higher)
- **Python** (v3.8 or higher)
- **MongoDB** (local installation or MongoDB Atlas account)
- **Git**

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/Roshansingh9/Keploy_Assignment-2
cd employee-management-system
```

#### 2. Backend Setup
```bash
# Navigate to backend directory
cd Backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```

#### 3. Frontend Setup
```bash
# Navigate to frontend directory (from root)
cd Frontend

# Install dependencies
npm install


```

## 🏃‍♂️ Running the Application

### Start Backend Server
```bash
cd Backend
python main.py

```

### Start Frontend Development Server
```bash
cd Frontend
npm start

```

## 🧪 Running Tests

The backend includes comprehensive testing with high coverage. Here's how to run the tests:

### Prerequisites for Testing
```bash
cd Backend
pip install -r requirements.txt  # Installs all testing dependencies
```

### Run All Tests
```bash
cd Backend
pytest
```

### Run Tests with Coverage Report
```bash
cd Backend
pytest --cov=main --cov-report=term-missing
```

### Run Tests with HTML Coverage Report
```bash
cd Backend
pytest --cov=main --cov-report=html
# Open htmlcov/index.html in browser to view detailed coverage
```

### Run Specific Test Files
```bash
# Unit tests only
pytest tests/test_unit.py

# API endpoint tests only
pytest tests/test_api.py

# Integration tests only
pytest tests/test_integration.py
```

### Run Tests with Verbose Output
```bash
pytest -v
```

## 🧪 Testing Frameworks & Tools Used

### Primary Testing Framework: pytest
- **pytest 7.4.3** - Main testing framework chosen for its simplicity and powerful features
- **pytest-cov 4.1.0** - Code coverage measurement and reporting
- **pytest-asyncio 0.21.1** - Support for testing async FastAPI endpoints
- **httpx 0.25.0** - HTTP client for testing API endpoints (replaces requests in async context)

### Additional Testing Tools
- **unittest.mock** - Python's built-in mocking library for isolating tests
- **FastAPI TestClient** - Built-in test client for FastAPI applications
- **MongoDB Mocking** - Database operations are mocked for isolated testing

### Testing Approach
- **Unit Tests** (`test_unit.py`) - Test individual functions and helper methods
- **API Tests** (`test_api.py`) - Test all FastAPI endpoints with various scenarios
- **Integration Tests** (`test_integration.py`) - Test complete CRUD workflows
- **Mocking Strategy** - Database operations are mocked to ensure fast, reliable tests

## 📊 Test Coverage Report

The application achieves **98% test coverage** across all major components:

### Coverage Summary

![Test Coverage Screenshot](Backend/testing_screenshots/coverage.png)


### What's Covered
- ✅ **All API Endpoints** - POST, GET, PUT, DELETE operations
- ✅ **Data Validation** - Pydantic model validation testing
- ✅ **Error Handling** - HTTP exceptions and edge cases
- ✅ **Database Operations** - CRUD operations with MongoDB
- ✅ **Business Logic** - Employee creation, updates, deletions
- ✅ **Input Validation** - Email uniqueness, required fields
- ✅ **Helper Functions** - Data transformation utilities

### Test Structure
```
Backend/tests/
├── __init__.py              # Package initialization
├── conftest.py             # Test configuration and fixtures
├── test_api.py             # API endpoint tests (12 test cases)
├── test_integration.py     # Integration tests (2 test cases)
└── test_unit.py            # Unit tests (2 test cases)
```

### Key Test Scenarios Covered

#### API Endpoint Tests (`test_api.py`)
- Root endpoint functionality
- Employee creation with valid data
- Duplicate email prevention
- Retrieve all employees
- Retrieve employee by ID
- Invalid ID format handling
- Employee not found scenarios
- Employee updates
- Employee deletion
- Various error conditions

#### Integration Tests (`test_integration.py`)
- Complete employee lifecycle (Create → Read → Update → Delete)
- Data validation across multiple operations
- End-to-end workflow testing

#### Unit Tests (`test_unit.py`)
- Helper function testing
- Data transformation utilities
- ObjectId string conversion

## 📁 Project Structure
```
employee-management-system/
├── Frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Application styles
│   │   └── index.js        # Entry point
│   ├── package.json
│   └── README.md
├── Backend/
│   ├── main.py             # FastAPI application with all endpoints
│   ├── models.py           # Pydantic models for data validation
│   ├── database.py         # MongoDB connection and configuration
│   ├── requirements.txt    # Python dependencies including test tools
│   ├── pytest.ini          # Pytest configuration file
│   ├── .env               # Environment variables (not committed)
│   ├── .gitignore         # Git ignore rules
│   └── tests/             # Test directory
│       ├── __init__.py    # Test package initialization
│       ├── conftest.py    # Test fixtures and configuration
│       ├── test_api.py    # API endpoint tests
│       ├── test_integration.py  # Integration tests
│       └── test_unit.py   # Unit tests
└── README.md              # This documentation
```

## 🔧 Environment Configuration

### Backend Environment Variables
Create a `.env` file in the `Backend` directory:
```env
MONGO_URL=mongodb://localhost:27017/employee_db
# For MongoDB Atlas:
# MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/employee_db?retryWrites=true&w=majority
```

### Test Environment
The test configuration is handled in `pytest.ini`:
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
addopts = --cov=main --cov-report=term-missing
env = 
    MONGO_URL = mongodb://localhost:27017/test_db
```

## 📧 Contact
**Developer**: Roshan Kumar Singh  
- **Email**: roshan.kr.singh9857@gmail.com  
- [**LinkedIn**](https://www.linkedin.com/in/roshan-kumar-singh-60b68a253/)  
- [**Portfolio**](https://roshansingh.live)
- [**GitHub Repository**](https://github.com/Roshansingh9/Keploy_Assignment-2)

### 🐛 Bug Reports
If you encounter any bugs or issues, please [create an issue](https://github.com/Roshansingh9/Keploy_Assignment-2/issues) with:
- Detailed description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

### 💡 Feature Requests
Have an idea for a new feature? We'd love to hear it! Please [open an issue](https://github.com/Roshansingh9/Keploy_Assignment-2/issues) with the tag "enhancement" and describe your suggestion.

---
