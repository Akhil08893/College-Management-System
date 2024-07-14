# College Management System 

Welcome to the College Management System developed using Python/Django!

## Project Overview

This project is a fully functional web application aimed at managing various aspects of college administration, including student information, staff management, courses, attendance, and more.

## Technologies used
  ### Django (Backend Framework)
  Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is known for its "batteries-included" philosophy, offering a 
    wide range of built-in features and tools that facilitate common web development tasks, such as authentication, URL routing, and database schema migrations
  ### MySQL (Database)
  MySQL is a widely-used open-source relational database management system (RDBMS). Known for its reliability, robustness, and ease of use.MySQL serves as the backbone for storing and managing a large volume of structured data efficiently.It handles student records, course information, faculty details, timetables, grades, and other essential data.
### Bootstrap (Frontend Framework)
Bootstrap is a popular front-end framework for developing responsive and mobile-first web applications. It provides a collection of pre-designed HTML, CSS, and JavaScript components that streamline the process of creating modern, visually appealing user interfaces.

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
3. **Now Run Server**
    ```bash
     python manage.py runserver
    ```
    Then go to the browser and enter the url http://127.0.0.1:8000/
4. **Login Credentials**
    #### Create Super User (HOD) :
    ```bash
      python manage.py createsuperuser
     ```
    You can access the django admin page at http://127.0.0.1:8000/admin and login with username 'admin' and the  password created above

## Screenshots
### Home page
![alt text](https://imgur.com/YU9qJQw.png)

### HOD pages
![alt text](https://imgur.com/sHhbD2d.png)

![alt text](https://imgur.com/IBNNRLD.png)

![alt text](https://imgur.com/B1DrMH0.png)

![alt text](https://imgur.com/sWE3QSp.png)

![alt text](https://imgur.com/QbGaslF.png)

![alt text](https://imgur.com/hhUPLPG.png)


### Staff Pages

![alt text](https://imgur.com/qySVrQO.png)

![alt text](https://imgur.com/5yoeil7.png)

![alt text](https://imgur.com/Z0SFuDZ.png)

![alt text](https://imgur.com/rRVHRaO.png)

![alt text](https://imgur.com/HaH4ciJ.png)

![alt text](https://imgur.com/gbwqMvU.png)

### Student Pages

![alt text](https://imgur.com/3gNXfjW.png)

![alt text](https://imgur.com/YieV4Ve.png)

![alt text](https://imgur.com/wvJP2fT.png)

### Admin Page

![alt text](https://imgur.com/0iXYmIh.png)

























