# Student Grade Analyzer V7

A Python-based Student Management System that allows users to manage student records, calculate grades, generate reports, and persist data using JSON and CSV files.

## Features

* Add student records
* View all students
* Search students by name
* Update student information
* Delete student records
* Find class topper
* Calculate class average
* Display highest and lowest averages
* Sort students by name
* Save and load data using JSON
* Export and import data using CSV
* Generate student performance reports
* Input validation and error handling
* Logging support

## Project Structure

```text
Student_Grade_Analyzer_V7/
│
├── data/                 # Data files
├── models/               # Student model
├── reports/              # Generated reports
├── services/             # Business logic
├── storage/              # JSON and CSV storage operations
├── ui/                   # Console user interface
├── validators/           # Input validation
│
├── main.py               # Application entry point
└── .gitignore
```

## Architecture

This version follows a layered architecture:

### Models Layer

Contains data structures and entity definitions.

### Services Layer

Handles business logic and student-related operations.

### Storage Layer

Manages JSON and CSV file operations.

### UI Layer

Handles user interaction through the console menu.

### Validators Layer

Performs input validation and data integrity checks.

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* CSV
* File Handling
* Logging
* Modular Programming

## Learning Outcomes

This project helped practice:

* Python fundamentals
* Functions and modules
* File handling
* JSON and CSV operations
* Error handling
* Logging
* Software architecture
* Separation of concerns
* Code refactoring
* Object-Oriented Programming concepts

## How to Run

```bash
python main.py
```

## Future Improvements

* Unit testing
* Database integration (SQLite)
* Graphical User Interface (Tkinter)
* Web version using Flask
* User authentication

## Author

Hafiz Atta Ur Rahman

Learning Python through hands-on project development and incremental version upgrades.
