# Task Management System

A Django-based task management application with admin-only CRUD operations.

## Features

- Display tasks with Serial Number, Description, Deadline, and Status
- Admin-only create, update, and delete operations
- Status tracking (Pending/Done)
- User authentication
- Responsive UI

## Project Structure

```
task/
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
├── db.sqlite3            # Database (auto-created)
├── task_manager/         # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                # Tasks application
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── forms.py
│   ├── urls.py
│   └── apps.py
└── templates/
    └── tasks/
        ├── task_list.html
        └── task_form.html
```

## Setup Instructions

### 1. Activate Virtual Environment
```bash
cd c:\srushti\task
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create Database
```bash
python manage.py migrate
```

### 4. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to enter:
- Username (e.g., admin)
- Email
- Password

### 5. Run Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/tasks/`

## Usage

### Public Access
- Visit `http://127.0.0.1:8000/tasks/` to view all tasks (read-only)

### Admin Access
- Click "Admin Login" button or go to `http://127.0.0.1:8000/admin/`
- Login with your superuser credentials
- Create, update, and delete tasks

### Admin Panel Features
- Create new tasks
- Edit task details (description, owner, deadline, status)
- Change task status to "Done" or "Pending"
- Delete tasks
- Bulk operations via Django admin

## Features Implemented

✅ Task Display with Serial Number, Description, Deadline, Status
✅ Admin-only CRUD operations
✅ User Authentication
✅ Role-based Access Control (admin/staff only)
✅ Responsive Design
✅ Form validation
✅ Database migrations

## API Endpoints

| Endpoint | Method | Permission | Description |
|----------|--------|-----------|-------------|
| `/tasks/` | GET | Public | View all tasks |
| `/tasks/create/` | GET, POST | Admin | Create new task |
| `/tasks/<id>/update/` | GET, POST | Admin | Update task |
| `/tasks/<id>/delete/` | POST | Admin | Delete task |
| `/admin/` | GET, POST | Superuser | Admin dashboard |

## Notes

- Only superusers can create, update, or delete tasks
- Public users can view tasks but cannot make modifications
- Tasks are ordered by creation date (newest first)
- Use Django admin panel for advanced management

## Future Enhancements

- MongoDB integration
- Task categories/tags
- Priority levels
- User-specific task assignment
- Email notifications for deadlines
- Task filtering and search
