
# DJANGO TODO-APP (Without Django Rest Framework)

This is a web application built with Django that allows users to create and manage tasks. The application provides a simple and intuitive interface using the UiKit framework for the frontend.

## Features
- User registration and authentication

- Task creation, editing

- Assigning tasks to specific users

- Marking tasks as completed or in progress

- Sorting and filtering tasks

- Responsive design with UiKit CSS framework

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ulysses316/django-todo.git
```
2. Create a virtual environment and activate it:
```bash
python  -m  venv  env
source  env/bin/activate  # For macOS/Linux
.\env\Scripts\activate # For Windows
```
3. Install python dependencies
```bash
pip  install  -r  requirements.txt
```
4. Install Frontend dependencies:
```bash
cd  static
npm  install
```
5. Envars

Create an .env file and add envars to connect to the database in postgresql

6. Apply the database migrations:
```bash
python  manage.py  makemigrations
python  manage.py  migrate
```
7. Run server
```bash
python  manage.py  runserver
```
