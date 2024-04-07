# Flasking

## Team Members
- Nathan Schmidt

## Description of Project
The project "Flasking" has been developed to create a web server that allows users to securely store information. Users can sign in to the server with unique credentials and store their data, providing a trusted platform for information storage through a self-hosted web server.

## Introduction
This project enables authorized users to securely store information on a web server from anywhere. It's crucial to ensure the server's security to maintain the integrity and confidentiality of stored data.

### Purpose
"Flasking" targets tech enthusiasts in the tech industry, offering a platform for companies and individuals to securely store and access data remotely.

### Scope
The project focuses on essential features such as registration, secure login, data storage, retrieval, and basic security measures. It supports text-based data entry specifically for notes at this time.

## Technologies Used
- Python3
- VSCode
- GitHub
- HTML/CSS/JavaScript
- JSON
- SQLite
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Talisman

## Must Have Requirements
- Allow users to register with unique usernames and secure passwords.
- Implement secure login with salted and hashed passwords.
- Enforce user access control for viewing and modifying their data.
- Enable users to add, edit, and delete text-based information securely.
- Provide users with the ability to view and download their stored information.
- Implement encryption at rest and in transit to protect sensitive data.
- Offer a user-friendly interface for registration, login, and data management.
- Implement logging mechanisms for user activity and server events.
- Establish a regular backup procedure for data recovery.

## Stretch Requirements
- Implement password recovery functionality.
- Provide data encryption for individual entries.
- Implement activity logs for better auditing and security monitoring.

## Weekly Schedule

| Requirement                    | Description                                                                        | Acceptance Criteria                              | Hours  | Due Date   |
|--------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------|--------|------------|
| User Registration and Login    | Implement user registration and secure login.                                      | Users can register and log in securely.          | 10     | Completed  |
| User Access Control            | Restrict user access to their own data.                                            | Users can only view and edit their data.         | 10     | Completed  |
| Data Storage and Retrieval     | Develop functionalities for adding, editing, and deleting text-based information.  | Users can manage their data securely.            | 10     | Completed  |
| User Interface Design          | Design a user-friendly interface.                                                  | Interface is intuitive and visually appealing.   | 10     | Completed  |
| Data Security and Encryption   | Implement encryption for data security.                                            | Data is encrypted at rest and in transit.        | 10     | Completed  |
| Server Configuration & Logging | Configure the server and implement logging mechanisms.                             | Server runs smoothly with logging enabled.       | 10     | Completed  |
| Documentation and Testing      | Document setup, configuration, and perform testing.                                | Comprehensive documentation and tested features. | 10     | Completed  |

## Design Overview of the Product

### Workflow
1. User Registration
2. Password Processing
3. Login
4. Authentication
5. Data Management

### Resources
- **Programming Language:** Python 3
- **Web Framework:** Flask
- **Development Environment:** VSCode
- **Version Control:** GitHub
- **Database:** SQLite

### Data at Rest
Stored securely in an encrypted SQLite database.

### Data on the Wire
Transmitted over HTTP (Flask-Talisman) for secure communication.

### Data State
Access restricted based on user authentication and authorization.

### HMI/HCI/GUI
- User interface designed using HTML, CSS, and Javascript.
- Focus on user-friendliness and intuitive navigation.

## Verification

### Demo
#### User Registration
- Users can register with a unique username and strong password.
- Password strength and uniqueness are validated.

#### Login
- Secure authentication process.
- Access restricted to authorized users only.

#### Data Management
- Add, edit, and delete text-based information securely.
- Intuitive user interface for data management.

#### Data Security
- Data encrypted at rest and in transit.

### Testing
| Feature                   | Must Have Requirement                                                                                      | Stretch Requirement                                   | Acceptance Testing Criteria                                                                                    |
|---------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| User Management           | Registration form validates password strength and uniqueness. Hashed and salted passwords stored securely. | Users can recover forgotten passwords.    (Incomplete)| Users can register with secure credentials. Successful login and access control. Password reset functionality. |
| Data Storage & Retrieval  | Data stored securely. Users can view, edit, delete, and download their data.                               | Data encryption for individual entries.   (Incomplete)| Secure storage and retrieval of data. Data displayed accurately.                                               |
| Security & Access Control | Data encrypted at rest and in transit.                                                                     | Implement activity logs.                    (Complete)| Encryption at rest and in transit. Access control based on user authentication.                                |
| User Interface (UI)       | User-friendly interface.                                                                                   | -                                                     | Visually appealing and intuitive UI. All functionalities accessible.                                           |
| System Administration     | Implement logging mechanisms.                                                                              | -                                                     | Logs capture user actions and server events. Logs accessible for monitoring and troubleshooting.               |

## Deployment
### Instructions:
1. Navigate to your local machine and code editor then do the following:
- git clone https://github.com/schminat000/flasking.git
2. Go to the project directory and enter the following to install the requirements:
- pip install -r requirements.txt
3. After installation, refresh your code editor.
4. Run the code via command line:
- python main.py
- This will create an instance folder within the project folder with the database inside, as well as the database_backups folder. It will also create a logs folder and begin filling information in an app.log file.
5. Run the code again.
6. The server is now running! Go to the page it gives you by control-clicking the address it gives you in the terminal and enjoy your personal note web server!
- To close the server, type CTRL + C in the terminal.

## Known Issues:
- It will log "Server is shutting down..." twice.