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

Each app contains:  

```
app_name/
├── models.py # Data models
├── views.py # Presentation & logic
├── urls.py # Endpoints
├── templates/ # HTML templates
├── static/ # CSS, JS, Images
└── tests.py # Unit tests
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
