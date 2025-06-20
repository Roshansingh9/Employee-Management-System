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
- **FastAPI** - Modern Python web framework for building APIs
- **MongoDB** - NoSQL database for data storage
- **PyMongo** - Python driver for MongoDB
- **Pydantic** - Data validation and settings management
- **Render** - Backend deployment platform

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

# Create .env file and add your MongoDB connection string
echo "MONGO_URL=your_mongodb_connection_string" > .env
```

#### 3. Frontend Setup
```bash
# Navigate to frontend directory (from root)
cd Frontend

# Install dependencies
npm install

# Create .env file with backend URL
echo "REACT_APP_API_URL=http://localhost:8000" > .env
```

### Running the Application

#### Start Backend Server
```bash
cd Backend
python main.py
# Server will run on http://localhost:8000
```

#### Start Frontend Development Server
```bash
cd Frontend
npm start
# Application will open on http://localhost:3000
```

## 📚 API Documentation

### Base URL
- **Production**: `https://keploy-assignment-2.onrender.com`
- **Local Development**: `http://localhost:8000`

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API health check |
| POST | `/employees` | Create new employee |
| GET | `/employees` | Get all employees |
| GET | `/employees/{id}` | Get specific employee |
| PUT | `/employees/{id}` | Update employee |
| DELETE | `/employees/{id}` | Delete employee |

### Employee Data Model
```json
{
  "id": "string",
  "name": "string",
  "email": "string",
  "department": "string",
  "position": "string",
  "salary": "number",
  "hire_date": "datetime"
}
```

## 📁 Folder Structure
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
│   ├── main.py             # FastAPI application
│   ├── models.py           # Pydantic models
│   ├── database.py         # MongoDB connection
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables
└── README.md              # Project documentation
```

## 🤝 Contributing

We welcome contributions to improve the Employee Management System! Here's how you can help:

### How to Contribute
1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m "Add: your feature description"
   ```
5. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**

### Contribution Guidelines
- Follow existing code style and conventions
- Add appropriate comments and documentation
- Test your changes thoroughly
- Update README.md if necessary
- Ensure all existing tests pass

### Areas for Contribution
- UI/UX improvements
- Additional employee fields
- Search and filtering functionality
- Data export features
- Unit and integration tests
- Performance optimizations


## 📧 Contact
**Developer**: Roshan Kumar Singh  
- **Email**: roshan.kr.singh9857@gmail.com  
- [**LinkedIn**](https://www.linkedin.com/in/roshan-kumar-singh-60b68a253/)  
- [**Portfolio**](https://roshansingh.live)




### 🐛 Bug Reports
If you encounter any bugs or issues, please [create an issue](https://github.com/Roshansingh9/Keploy_Assignment-2/issues) with:
- Detailed description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

### 💡 Feature Requests
Have an idea for a new feature? We'd love to hear it! Please [open an issue](https://github.com/Roshansingh9/Keploy_Assignment-2/issues) with the tag "enhancement" and describe your suggestion.
