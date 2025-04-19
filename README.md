#  ToDo List Web Application

A minimal and intuitive task manager built with **Python (Flask)** and **SQLite**, designed to help users create, update, and manage daily tasks efficiently.

##  Features

-  Add new tasks with title and description  
-  Update existing tasks  
-  Delete completed tasks  
-  Automatically timestamps each entry  
-  Clean and responsive UI with Bootstrap  
-  Uses SQLite for data storage  
-  Jinja templating for dynamic content rendering

---

##  Getting Started

### Prerequisites

Make sure you have Python 3.x installed.

### Installation

1. Clone the repository or download the files.

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirement
```

4. Run the Flask application:

```bash
python app.py
```

5. Open your browser and go to:  
   **http://127.0.0.1:5000/**

---

##  Project Structure

```
├── app.py                # Main Flask application
├── toDo.db               # SQLite database file
├── seriel.py             # Auxiliary script for list operations (optional utility)
├── requirement           # List of dependencies
├── templates/
│   ├── index.html        # Main page to add & view tasks
│   ├── about.html        # About the project
│   └── update.html       # Update task form
```

---

##  About

This app is built for simplicity and usability. Whether you're a student, professional, or anyone needing a task manager — this is your go-to app. Inspired by modern UI principles and designed with learning Flask in mind.

---

##  Credits

Created using:
- Flask
- SQLAlchemy
- Bootstrap
- Jinja2 templating

---

##  License

This project is open-source and available for educational and personal use.
