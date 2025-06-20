import React, { useState, useEffect, useRef } from 'react';

// Mock API functions for demonstration
const mockAPI = {
  employees: [
    { id: 1, name: 'John Doe', email: 'john@example.com', department: 'Engineering', position: 'Developer', salary: 75000, hire_date: '2023-01-15' },
    { id: 2, name: 'Jane Smith', email: 'jane@example.com', department: 'Marketing', position: 'Manager', salary: 85000, hire_date: '2022-06-10' },
    { id: 3, name: 'Mike Johnson', email: 'mike@example.com', department: 'Sales', position: 'Representative', salary: 60000, hire_date: '2023-03-20' }
  ],
  
  getEmployees: () => Promise.resolve(mockAPI.employees),
  
  createEmployee: (employee) => {
    const newEmployee = { ...employee, id: Date.now(), hire_date: new Date().toISOString().split('T')[0] };
    mockAPI.employees.push(newEmployee);
    return Promise.resolve(newEmployee);
  },
  
  updateEmployee: (id, employee) => {
    const index = mockAPI.employees.findIndex(emp => emp.id === id);
    if (index !== -1) {
      mockAPI.employees[index] = { ...mockAPI.employees[index], ...employee };
    }
    return Promise.resolve(mockAPI.employees[index]);
  },
  
  deleteEmployee: (id) => {
    mockAPI.employees = mockAPI.employees.filter(emp => emp.id !== id);
    return Promise.resolve();
  }
};

function App() {
  const [employees, setEmployees] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    department: '',
    position: '',
    salary: ''
  });
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  // Ref for scrolling to form
  const formRef = useRef(null);

  // Fetch all employees
  const fetchEmployees = async () => {
    try {
      setLoading(true);
      const data = await mockAPI.getEmployees();
      setEmployees(data);
      setError('');
    } catch (err) {
      setError('Failed to fetch employees');
      console.error('Error fetching employees:', err);
    } finally {
      setLoading(false);
    }
  };

  // Handle form input changes
  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      const employeeData = {
        ...formData,
        salary: parseFloat(formData.salary)
      };

      if (editingId) {
        // Update employee
        await mockAPI.updateEmployee(editingId, employeeData);
        setEditingId(null);
      } else {
        // Create new employee
        await mockAPI.createEmployee(employeeData);
      }

      // Reset form and refresh list
      setFormData({
        name: '',
        email: '',
        department: '',
        position: '',
        salary: ''
      });
      
      await fetchEmployees();
      setError('');
    } catch (err) {
      setError('Failed to save employee');
      console.error('Error saving employee:', err);
    } finally {
      setLoading(false);
    }
  };

  // Handle edit button click
  const handleEdit = (employee) => {
    setFormData({
      name: employee.name,
      email: employee.email,
      department: employee.department,
      position: employee.position,
      salary: employee.salary.toString()
    });
    setEditingId(employee.id);
    
    // Scroll to form with smooth animation
    setTimeout(() => {
      formRef.current?.scrollIntoView({ 
        behavior: 'smooth', 
        block: 'start' 
      });
    }, 100);
  };

  // Handle delete
  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this employee?')) {
      try {
        setLoading(true);
        await mockAPI.deleteEmployee(id);
        await fetchEmployees();
        setError('');
      } catch (err) {
        setError('Failed to delete employee');
        console.error('Error deleting employee:', err);
      } finally {
        setLoading(false);
      }
    }
  };

  // Cancel edit
  const handleCancelEdit = () => {
    setEditingId(null);
    setFormData({
      name: '',
      email: '',
      department: '',
      position: '',
      salary: ''
    });
  };

  // Load employees on component mount
  useEffect(() => {
    fetchEmployees();
  }, []);

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f5f5f5', fontFamily: 'Arial, sans-serif' }}>
      <header style={{ 
        backgroundColor: '#2c3e50', 
        color: 'white', 
        padding: '1rem', 
        textAlign: 'center',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
      }}>
        <h1 style={{ margin: 0 }}>Employee Management System</h1>
      </header>

      <main style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem' }}>
        {/* Employee Form */}
        <section 
          ref={formRef}
          style={{
            backgroundColor: 'white',
            padding: '2rem',
            borderRadius: '8px',
            marginBottom: '2rem',
            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
            // Highlight when editing
            border: editingId ? '3px solid #3498db' : '1px solid #e0e0e0',
            position: 'relative'
          }}
        >
          {/* Edit mode indicator */}
          {editingId && (
            <div style={{
              position: 'absolute',
              top: '-12px',
              left: '20px',
              backgroundColor: '#3498db',
              color: 'white',
              padding: '4px 12px',
              borderRadius: '12px',
              fontSize: '0.85rem',
              fontWeight: 'bold'
            }}>
              ✏️ EDITING MODE
            </div>
          )}
          
          <h2 style={{ 
            color: editingId ? '#3498db' : '#2c3e50',
            marginTop: editingId ? '1rem' : '0'
          }}>
            {editingId ? '✏️ Edit Employee' : '➕ Add New Employee'}
          </h2>
          
          {editingId && (
            <div style={{
              backgroundColor: '#e3f2fd',
              border: '1px solid #2196f3',
              borderRadius: '4px',
              padding: '0.75rem',
              marginBottom: '1rem',
              fontSize: '0.9rem',
              color: '#1976d2'
            }}>
              <strong>📝 You're currently editing an employee.</strong> Make your changes below and click "Update Employee" to save.
            </div>
          )}
          
          {error && (
            <div style={{
              backgroundColor: '#ffebee',
              color: '#c62828',
              padding: '0.75rem',
              borderRadius: '4px',
              marginBottom: '1rem',
              border: '1px solid #ef5350'
            }}>
              {error}
            </div>
          )}
          
          <div onSubmit={handleSubmit}>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '1.5rem' }}>
              <input
                type="text"
                name="name"
                placeholder="Full Name"
                value={formData.name}
                onChange={handleInputChange}
                required
                style={{
                  padding: '0.75rem',
                  border: '2px solid #e0e0e0',
                  borderRadius: '4px',
                  fontSize: '1rem',
                  outline: 'none'
                }}
                onFocus={(e) => e.target.style.borderColor = '#3498db'}
                onBlur={(e) => e.target.style.borderColor = '#e0e0e0'}
              />
              
              <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleInputChange}
                required
                style={{
                  padding: '0.75rem',
                  border: '2px solid #e0e0e0',
                  borderRadius: '4px',
                  fontSize: '1rem',
                  outline: 'none'
                }}
                onFocus={(e) => e.target.style.borderColor = '#3498db'}
                onBlur={(e) => e.target.style.borderColor = '#e0e0e0'}
              />
              
              <input
                type="text"
                name="department"
                placeholder="Department"
                value={formData.department}
                onChange={handleInputChange}
                required
                style={{
                  padding: '0.75rem',
                  border: '2px solid #e0e0e0',
                  borderRadius: '4px',
                  fontSize: '1rem',
                  outline: 'none'
                }}
                onFocus={(e) => e.target.style.borderColor = '#3498db'}
                onBlur={(e) => e.target.style.borderColor = '#e0e0e0'}
              />
              
              <input
                type="text"
                name="position"
                placeholder="Position"
                value={formData.position}
                onChange={handleInputChange}
                required
                style={{
                  padding: '0.75rem',
                  border: '2px solid #e0e0e0',
                  borderRadius: '4px',
                  fontSize: '1rem',
                  outline: 'none'
                }}
                onFocus={(e) => e.target.style.borderColor = '#3498db'}
                onBlur={(e) => e.target.style.borderColor = '#e0e0e0'}
              />
              
              <input
                type="number"
                name="salary"
                placeholder="Salary"
                value={formData.salary}
                onChange={handleInputChange}
                step="0.01"
                min="0"
                required
                style={{
                  padding: '0.75rem',
                  border: '2px solid #e0e0e0',
                  borderRadius: '4px',
                  fontSize: '1rem',
                  outline: 'none'
                }}
                onFocus={(e) => e.target.style.borderColor = '#3498db'}
                onBlur={(e) => e.target.style.borderColor = '#e0e0e0'}
              />
            </div>
            
            <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
              <button 
                type="submit" 
                onClick={handleSubmit}
                disabled={loading}
                style={{
                  backgroundColor: editingId ? '#3498db' : '#27ae60',
                  color: 'white',
                  border: 'none',
                  padding: '0.75rem 1.5rem',
                  borderRadius: '4px',
                  fontSize: '1rem',
                  cursor: loading ? 'not-allowed' : 'pointer',
                  opacity: loading ? 0.6 : 1,
                  fontWeight: 'bold'
                }}
              >
                {loading ? 'Saving...' : (editingId ? '💾 Update Employee' : '➕ Add Employee')}
              </button>
              
              {editingId && (
                <button 
                  type="button" 
                  onClick={handleCancelEdit}
                  style={{
                    backgroundColor: '#95a5a6',
                    color: 'white',
                    border: 'none',
                    padding: '0.75rem 1.5rem',
                    borderRadius: '4px',
                    fontSize: '1rem',                    cursor: 'pointer',
                    fontWeight: 'bold'
                  }}
                >
                  ❌ Cancel Edit
                </button>
              )}
            </div>
          </div>
        </section>

        {/* Employee List */}
        <section>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
            <h2 style={{ color: '#2c3e50', margin: 0 }}>
              👥 Employees ({employees.length})
            </h2>
          </div>
          
          {loading && (
            <div style={{ 
              textAlign: 'center', 
              padding: '2rem',
              backgroundColor: 'white',
              borderRadius: '8px',
              color: '#7f8c8d'
            }}>
              Loading...
            </div>
          )}
          
          {employees.length === 0 && !loading ? (
            <div style={{
              textAlign: 'center',
              padding: '3rem',
              backgroundColor: 'white',
              borderRadius: '8px',
              color: '#7f8c8d'
            }}>
              <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>👥</div>
              <p>No employees found. Add your first employee above!</p>
            </div>
          ) : (
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
              gap: '1.5rem'
            }}>
              {employees.map((employee) => (
                <div 
                  key={employee.id} 
                  style={{
                    backgroundColor: 'white',
                    padding: '1.5rem',
                    borderRadius: '8px',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
                    border: editingId === employee.id ? '2px solid #3498db' : '1px solid #e0e0e0',
                    position: 'relative',
                    transform: editingId === employee.id ? 'scale(1.02)' : 'scale(1)',
                    transition: 'all 0.2s ease'
                  }}
                >
                  {editingId === employee.id && (
                    <div style={{
                      position: 'absolute',
                      top: '-8px',
                      right: '-8px',
                      backgroundColor: '#3498db',
                      color: 'white',
                      borderRadius: '50%',
                      width: '24px',
                      height: '24px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '12px',
                      fontWeight: 'bold'
                    }}>
                      ✏️
                    </div>
                  )}
                  
                  <div style={{ marginBottom: '1rem' }}>
                    <h3 style={{ margin: '0 0 0.5rem 0', color: '#2c3e50' }}>{employee.name}</h3>
                    <p style={{ margin: '0.25rem 0', color: '#7f8c8d' }}>✉️ {employee.email}</p>
                    <p style={{ margin: '0.25rem 0', color: '#7f8c8d' }}>🏢 {employee.department}</p>
                    <p style={{ margin: '0.25rem 0', color: '#7f8c8d' }}>💼 {employee.position}</p>
                    <p style={{ margin: '0.25rem 0', color: '#27ae60', fontWeight: 'bold' }}>
                      💰 ${employee.salary.toLocaleString()}
                    </p>
                    <p style={{ margin: '0.25rem 0', color: '#7f8c8d', fontSize: '0.9rem' }}>
                      📅 Hired: {new Date(employee.hire_date).toLocaleDateString()}
                    </p>
                  </div>
                  
                  <div style={{ display: 'flex', gap: '0.5rem' }}>
                    <button 
                      onClick={() => handleEdit(employee)}
                      disabled={loading}
                      style={{
                        backgroundColor: '#3498db',
                        color: 'white',
                        border: 'none',
                        padding: '0.5rem 1rem',
                        borderRadius: '4px',
                        cursor: loading ? 'not-allowed' : 'pointer',
                        fontSize: '0.9rem',
                        opacity: loading ? 0.6 : 1,
                        fontWeight: 'bold'
                      }}
                    >
                      ✏️ Edit
                    </button>
                    <button 
                      onClick={() => handleDelete(employee.id)}
                      disabled={loading}
                      style={{
                        backgroundColor: '#e74c3c',
                        color: 'white',
                        border: 'none',
                        padding: '0.5rem 1rem',
                        borderRadius: '4px',
                        cursor: loading ? 'not-allowed' : 'pointer',
                        fontSize: '0.9rem',
                        opacity: loading ? 0.6 : 1,
                        fontWeight: 'bold'
                      }}
                    >
                      🗑️ Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;