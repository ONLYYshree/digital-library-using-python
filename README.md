DIGITAL LIBRARY WEBSITE FOR AI DEPARTMENT - SEMESTER 3

PROJECT OVERVIEW

This project is a user-centric Digital Library for the 3rd semester of the AI department, developed with Python Flask. It provides academic resources tailored to this semester, including previous year question papers, e-books, lecture notes, and a helpdesk section to assist students in checking content availability.

FEATURES

User Authentication: Includes signup, login, and logout pages for secure user access.

Academic Content Repository:

Question Papers: Collection of previous year exam papers for practice.

E-books: Digital copies of textbooks and reference materials.

Notes: Lecture notes and handouts.

Helpdesk:Users can submit requests or questions.

Admins can respond, with both submissions and responses saved for future reference.

TECH STACK

Frontend: HTML, CSS (no CSS framework used)

Backend: Python Flask

Database: SQLite (or any other supported by Flask for data persistence)

Installation

Clone the repository:

bash

git clone https://github.com/ONLYYshree/digital-library-using-python.git
cd digital-library

Install Dependencies: Ensure you have Python installed, then run:

bash

pip install -r requirements.txt

Run the Application:

bash

flask run
Access the app at http://127.0.0.1:5000.

USAGE

Home Page: Browse available academic resources.

Signup/Login: Create or access a user account.

Browse Content: Access organized content like question papers, notes, and e-books.

Helpdesk: Submit content requests or questions, and view admin responses.

FOLDER STRUCTURE

website/:main directory 


templates/: HTML files for the frontend.

static/: Static resources like CSS and images.

__init__.py: The __init__.py file in a Flask project is the entry point for the application.

auth.py:The auth.py file manages authentication-related routes and functionality for the digital library project, ensuring secure access to the academic content

models.py: Database models to store user data, content details, and helpdesk entries.

views.py: The views.py file handles general routes that users access after logging in. It defines routes for displaying content, accessing specific pages, and handling interactions such as submitting helpdesk requests.


main.py: Main application file to run the Flask app.

FUTURE SCOPE

Add more semesters’ content.

Enhance the UI with a CSS framework.

Improve the helpdesk with advanced search features.







