# College Management System 

Welcome to the College Management System developed using Python/Django!

## Project Overview

This project is a fully functional web application aimed at managing various aspects of college administration, including student information, staff management, courses, attendance, and more.


### Features

- **Admin User(HOD) Can:**
  - See overall summary charts of students' performances, staff performances, courses, subjects, leave, etc.
  - Manage staff (Add, Update, Delete)
  - Manage students (Add, Update, Delete)
  - Manage courses (Add, Update, Delete)
  - Manage subjects (Add, Update, Delete)
  - Manage sessions (Add, Update, Delete)
  - View student attendance
  - Review and reply to student/staff feedback
  - Review (approve/reject) student/staff leave requests

- **Staff/Teachers Can:**
  - See overall summary charts related to their students, subjects, leave status, etc.
  - Take/update student attendance
  - Add/update results
  - Apply for leave
  - Send feedback to the Head of Department (HOD)

- **Students Can:**
  - See overall summary charts related to their attendance, subjects, leave status, etc.
  - View attendance
  - View results
  - Apply for leave
  - Send feedback to the HOD

## Installation Steps

### Pre-Requisites

1. Install Git Version Control [Git](https://git-scm.com/)
2. Install the latest Python version [Python](https://www.python.org/downloads/)
3. Install Pip (Python Package Manager) [Pip](https://pip.pypa.io/en/stable/installing/)

### Installation Steps

1. **Set up a Virtual Environment:**

   #### Install Virtual Environment:
   
   Before you start, make sure you have `virtualenv` installed. If not, you can install it using pip
   ```bash
   pip install virtualenv
   ```
   #### Create Virtual Environment
    ```bash
     python -m venv venv
   ```
   #### Activate Virtual Environment
    ```bash
     source venv/scripts/activate
    ```
2.  **Clone this project:**
    ```bash
    git clone https://github.com/Akhil08893/College-management-System.git
    ```
    #### Then, Enter the project
    ```bash
     cd student_management_system
     ```
3. **Install Requirements from 'requirements.txt'**
    ```bash
     pip3 install -r requirements.txt
    ```
4. **Now Run Server**
    ```bash
     python manage.py runserver
    ```
5. **Login Credentials**
    #### Create Super User (HOD) :
    ```bash
      python manage.py createsuperuser
     ```
     
