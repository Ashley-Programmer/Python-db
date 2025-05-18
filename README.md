# User Registration & Management System

A desktop application built with Python and CustomTkinter for user registration, login, and management with MySQL database integration.

![Application Screenshot](https://via.placeholder.com/600x400?text=Registration+System+Screenshot)

## Features

- **User Registration:** Create new user accounts with username, email, and password
- **User Authentication:** Secure login system for registered users
- **User Management:** View and manage registered user information
- **Modern UI:** Clean and responsive interface using CustomTkinter
- **Data Validation:** Form validation for all user inputs
- **Database Integration:** MySQL backend for data persistence

## Requirements

- Python3
- MySQL Server
- Required Python packages:
  - `customtkinter`
  - `mysql-connector-python`
  - `tkinter` (included in standard Python installation)

## Installation

1. **Clone or download the repository**

2. **Install required Python packages:**
   ```bash
   pip install customtkinter mysql-connector-python
   ```

3. **Set up MySQL database:**
   - Create a database named `python_register`
   - Create a table named `users_db` with the following structure:
   ```sql
   CREATE TABLE users_db (
     id INT AUTO_INCREMENT PRIMARY KEY,
     username VARCHAR(255) NOT NULL,
     email VARCHAR(255) NOT NULL UNIQUE,
     password VARCHAR(255) NOT NULL
   );
   ```

4. **Configure database connection:**
   - By default, the application connects to:
     - Host: localhost
     - User: root
     - Password: (empty)
     - Database: python_register
   - If your configuration differs, update the `connect_db()` function in the code.

## Usage

1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Sign Up:**
   - The application opens with the sign-up window by default
   - Enter username, email, password (minimum 8 characters), and confirm password
   - Click "SIGN UP" to register

3. **Login:**
   - Navigate to login page by clicking "Login here"
   - Enter your registered email and password
   - Click "LOGIN" to access your account

4. **Manage Users:**
   - After logging in, you can view user data by clicking "Show/Pop up User Data"
   - The system displays all registered users with their ID, name, and email

## Application Structure

### Database Functions
- `connect_db()`: Establishes connection to MySQL database
- `register_user()`: Inserts new user data into the database
- `login_user()`: Authenticates user against database records
- `load_data_from_db()`: Retrieves all user records
- `display_user_data()`: Shows user information in a messagebox

### Form Validation
- `validate_form()`: Validates registration form inputs
- `validate_form2()`: Validates login form inputs

### UI Functions
- `signup_page()`: Displays the registration form
- `login_page()`: Displays the login form
- `manage_user_page()`: Displays the user management interface
- `register_and_redirect()`: Handles registration and redirection to login
- `login_and_redirect()`: Handles login and redirection to management

## Security Considerations

⚠️ **Important Notes:**
- This application stores passwords as plaintext, which is not secure for production
- For a production environment, implement proper password hashing (e.g., bcrypt)
- Consider adding additional security measures:
  - Input sanitization to prevent SQL injection
  - Session management
  - Password strength requirements

## Customization

- UI elements can be customized by modifying the CustomTkinter widget properties
- Database schema can be extended to store additional user information
- Form validation rules can be adjusted in the validation functions

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

Ashley Koketso Motsie 

---

*This README is for the User Registration & Management System, a Python desktop application using CustomTkinter and MySQL.*
