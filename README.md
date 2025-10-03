# Flask User Management System

A lightweight and efficient web application for managing user profiles built with Flask and MySQL. This system provides complete CRUD (Create, Read, Delete) operations for user management through an intuitive web interface.

## 🌟 Overview

The Flask User Management System is a streamlined web application that allows administrators to:
- Add new users through a simple form
- View all users in an organized list
- Access individual user profile pages
- Remove users from the system
- Manage user data with a clean, responsive interface

## 🛠️ Tech Stack

- **Backend**: Python with Flask framework
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Templating**: Jinja2

## 🗃️ Database Design

### Users Table

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique user identifier |
| user_name | VARCHAR(50) | NOT NULL | User's full name |
| email | VARCHAR(100) | NOT NULL | Email address |
| city | VARCHAR(50) | | City of residence |
| hobby | VARCHAR(50) | | User's hobby/interests |

## 📋 Prerequisites

Before installation, ensure you have the following installed:

- Python 3.8+
- MySQL Server 5.7+
- pip (Python package manager)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-user-management.git
cd flask-user-management
2. Create Virtual Environment (Recommended)
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
pip install flask mysql-connector-python
Or create a requirements.txt file and install:

bash
pip install -r requirements.txt
Example requirements.txt:

text
Flask==2.3.3
mysql-connector-python==8.1.0
4. Database Setup
Create MySQL Database and User
sql
CREATE DATABASE user_management;
CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON user_management.* TO 'flask_user'@'localhost';
FLUSH PRIVILEGES;
Create Users Table
sql
USE user_management;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    hobby VARCHAR(50)
);
5. Configuration

Make corresponding change in order to connect MySQL in the server.py

conn = mysql.connector.connect(
   host = "hostname",
   user = 'username',
   password = 'password',
   database = 'databasename'
)
－－－－－－－－－－－－－－－
Create a config.py file or set environment variables:

python
# config.py
MYSQL_HOST = 'localhost'
MYSQL_USER = 'flask_user'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'user_management'
SECRET_KEY = 'your-secret-key-here'
🏃‍♂️ Running the Application
Set environment variables (optional):

bash
export FLASK_APP=app.py
export FLASK_ENV=development
Run the application:

bash
python app.py
Access the application:
Open your web browser and navigate to:

text
http://localhost:5000
📄 App Pages & Routes
1. Home Page (/)
Purpose: Introduction and navigation hub

Welcome message

Navigation buttons to all major sections

Clean, responsive design using Bootstrap

Content:

Welcome header and description

"Add User" button → /add

"View Users" button → /users

2. Add User Form Page (/add)
Methods: GET (display form), POST (process submission)

Purpose: Add new users to the database

Form Fields:

Name (text input, required)

Email (email input, required)

City (text input)

Hobby (text input)

Flow:

User fills out the form

Form validation occurs

Data inserted into users table

Redirect to /users upon success

3. User List Page (/users)
Purpose: Display all users in a responsive table format

Content:

Bootstrap-styled table showing:

Name

Email

City

Hobby

"View Profile" button → /user/<id>

"Delete" button → /delete/<id>

4. User Profile Page (/user/<id>)
Purpose: Display detailed information for a specific user

Content:

Complete user profile information

User ID, Name, Email, City, Hobby

Navigation back to user list

5. Delete User Functionality (/delete/<id>)
Purpose: Remove user from the database

Flow:

User clicks delete button

Confirmation (optional - can be implemented with JavaScript)

User record deleted from users table

Redirect to /users with success message

💾 Example Application Structure
text
flask-user-management/
├── app.py
├── config.py
├── requirements.txt
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── templates/
    ├── base.html
    ├── index.html
    ├── add_user.html
    ├── users.html
    └── user_profile.html
🎯 Key Features
Responsive Design: Bootstrap-powered interface works on all devices

Form Validation: Client and server-side validation

CRUD Operations: Complete Create, Read, Delete functionality

Clean UI: Professional and user-friendly interface

MySQL Integration: Robust database operations

RESTful Routes: Logical and predictable URL structure

🔧 API Endpoints
Method	Route	Description
GET	/	Home page
GET, POST	/add	Add new user
GET	/users	List all users
GET	/user/<id>	Show user profile
GET, POST	/delete/<id>	Delete user
🤝 Contribution
This project was developed with contributions and assistance from:

Kevin Leung (kevinleung96) - Lead Development & Architecture

GitHub - Version control and collaboration platform

Google - Research, troubleshooting, and best practices

ChatGPT - Code optimization and development guidance

Gemini - Technical consultation and problem-solving

How to Contribute
Fork the repository

Create a feature branch: git checkout -b feature/NewFeature

Commit your changes: git commit -am 'Add NewFeature'

Push to the branch: git push origin feature/NewFeature

Submit a Pull Request

🐛 Troubleshooting
Common Issues
MySQL Connection Error

Verify MySQL service is running

Check database credentials in config

Ensure user has proper permissions

Module Not Found Errors

Ensure virtual environment is activated

Run pip install -r requirements.txt

Port Already in Use

Change port in app.py: app.run(port=5001)

Kill existing process: pkill -f flask

📞 Support
For support, please contact the development team or create an issue in the GitHub repository.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.