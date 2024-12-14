# Flask Notes App

A simple web application built with Flask that allows users to sign up, log in, and create multiple notes. Users can securely manage their notes, with features for signing up, logging in, and creating/editing/deleting notes.

## Features

- **User Authentication:**
  - User sign-up
  - User login/logout
  - Session-based authentication

- **Notes Management:**
  - Create, update, and delete notes
  - View a list of all created notes

## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/e5m41l/Flask-Web-App
cd Flask-Web-App
```

### 2. Set up a Virtual Environment (optional but recommended)

For better project dependency management, it's a good idea to create a virtual environment.

```bash
python -m venv venv
```

### 3. Install Dependencies

Make sure you have all the necessary libraries installed:

```bash
pip install -r requirements.txt
```

### 4. Set up Database (if applicable)

If you're using a database (e.g., SQLite, PostgreSQL), make sure to set up your database. If you're using SQLite, the application might create it automatically when you run it.

For example, you can run the following to create the tables:

```bash
python
from app import db
db.create_all()
```

### 5. Run the Application

Once the dependencies are installed and the database is set up, you can run the app locally.

```bash
python app.py
```

The app should now be running at `http://127.0.0.1:5000/`.

## Usage

1. **Sign Up**: Navigate to `/signup` to create a new account.
2. **Login**: After signing up, log in at `/login` to access your notes.
3. **Create Notes**: After logging in, navigate to `/notes` to view, create, edit, or delete your notes.
4. **Logout**: Use the logout option from the navigation bar to end your session.

## File Structure

```
/your-project-folder
├── app.py                  # Main application file
├── models.py               # Database models (User, Note)
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── login.html          # Login page
│   ├── signup.html         # Sign-up page
│   └── notes.html          # Edit note page
├── static/                 # CSS, JS, images
│   └── index.js
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

## Technologies Used

- **Flask** – Web framework for building the application.
- **Flask-SQLAlchemy** – ORM for handling database interactions.
- **Flask-Login** – User session management for login/logout functionality.
- **Jinja2** – Template engine used in Flask for rendering HTML.
- **SQLite** (or other DB) – Database for storing user and note data.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
