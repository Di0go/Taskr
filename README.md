# Taskr  

Taskr is a simple collaborative task management web application inspired by Kanban boards (like Trello), but lighter and more focused on the essentials.  

---

## Features  

- Users
- Projects  
- States (customizable columns)  
- Tasks (create, edit, move, delete)  
- Collaboration (add/remove members, assign tasks)  
- Navigation (sidebar with projects)  

**Future:**  
- Labels  
- Notifications  
- Permissions  

---

## Setup & Usage  

### 1. Clone the repository  

```
git clone https://github.com/Di0go/Taskr
cd taskr  
```

### 2. Create a virtual environment  
```
python -m venv venv  
source venv/bin/activate   # macOS/Linux  
venv\Scripts\activate      # Windows  
```

### 3. Install dependencies  
```
pip install -r requirements.txt  
```

### 4. Set up the django secret key and environment variables
Copy the example environment file and edit it:  
```
cp .env.example .env
```

Generating a secret key
```
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Then open `.env` and set your values:  
```
DJANGO_SECRET_KEY=YOUR-SECRET-KEY
```

### 5. Apply migrations  
After setting up your environment:  
```
python manage.py migrate
```

### 6. Create super user  
After applying the migration files:
```
python manage.py createsuperuser
```

### 7. Run the server
```
python manage.py runserver
```

💡 Remember to run this command every time migrations have been added!

If you modify models, create new migrations with:  
```
python manage.py makemigrations
```

Commit migration files so others can apply them.

---

## Collaboration Guidelines  

- Never commit `.env` or `db.sqlite3`  
- Always commit migration files (`migrations/*.py`)  
- Run `python manage.py migrate` after every pull (just to be safe)
- Each developer should have their own `.env` file and local database  
- Never leak the secret key

---

## Tech Stack  

- **Backend**: Django (Python)  
- **Database**: SQLite (via Django ORM)  
- **Frontend**: Django Templates + Bootstrap  
- **Auth**: Django built-in User system  
- **Testing**: Django unittest + GitHub Actions  

---

## Architecture  

```
taskr/ # Main project directory
│
├── taskr/ # Global configs, main urls
├── users/ # User management
├── projects/ # Projects creation & management
├── states/ # Customizable project columns
├── tasks/ # Task creation & management
└── collaboration/ # Project members & assignments
```

---

## Data Models (simplified)

```
Users
└── User (Django built-in)
└── avatar 

Projects
└── Project
├── name
├── owner (FK → User)
└── members (ManyToMany → User)

States
└── State
├── name
├── order
└── project (FK → Project)

Tasks
└── Task
├── name
├── description
├── state (FK → State)
└── assigned_to (FK → User, optional)
```

---

## Project Context  

This project was developed as part of a university course on Agile Software Development Methodologies.  
The goal is to apply **eXtreme Programming (XP)** principles in practice, from planning to implementation, using an agile approach.  

**Taskr** serves as a practical example of developing a collaborative web application, allowing students to experience iterative development, test-driven development, modular architecture, and user-focused features. 

---
