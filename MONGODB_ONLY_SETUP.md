# MongoDB-Only Task Management Setup

This is now a **100% MongoDB-based** Django application with custom authentication.

## ✅ Quick Setup (3 Steps)

### **Step 1: Start MongoDB**
Open a **NEW PowerShell window** and run:
```bash
mongod
```
Wait for: `Waiting for connections on port 27017`

### **Step 2: Create Admin User**
In your project folder, run:
```bash
python manage.py create_admin
```

Follow prompts:
```
Enter username: admin
Enter email: admin@example.com
Enter password: admin123
```

### **Step 3: Start Django Server**
```bash
python manage.py runserver
```

You'll see:
```
Starting development server at http://127.0.0.1:8000/
```

## 🌐 Access Your Application

### **View Tasks** (Public)
http://127.0.0.1:8000/tasks/

### **Admin Login**
http://127.0.0.1:8000/tasks/login/

### **After Login - CRUD Operations**
- ➕ **Add New Task** - Click "+ Add New Task"
- ✏️ **Edit Task** - Click "Edit" on any task
- 🗑️ **Delete Task** - Click "Delete" on any task

---

## 🎯 What's New - MongoDB Only

✅ **No SQLite** - Everything stored in MongoDB
✅ **Custom Authentication** - AdminUser model in MongoDB
✅ **MongoDB Collections:**
   - `admin_users` - Admin accounts
   - `tasks` - Task data
   - `sessions` - Session data (if needed)

✅ **Session Storage** - Django sessions stored in MongoDB
✅ **No Django Auth** - Custom authentication system

---

## 📊 MongoDB Data Structure

### admin_users collection
```json
{
  "_id": ObjectId,
  "username": "admin",
  "email": "admin@example.com",
  "password_hash": "sha256hash...",
  "is_active": true,
  "is_superuser": true,
  "is_staff": true,
  "created_at": ISODate
}
```

### tasks collection
```json
{
  "_id": ObjectId,
  "sr_no": 1,
  "description": "Task description",
  "owner": "Owner name",
  "deadline": ISODate,
  "status": "Pending",
  "created_at": ISODate,
  "updated_at": ISODate
}
```

---

## 🔧 Management Commands

### Create Admin User
```bash
python manage.py create_admin
python manage.py create_admin --username admin --email admin@ex.com --password pass123
```

---

## 📝 MongoDB Commands (mongosh)

### View all tasks
```javascript
use task_manager_db
db.tasks.find()
```

### View admin users
```javascript
db.admin_users.find()
```

### Find pending tasks
```javascript
db.tasks.find({ status: "Pending" })
```

### Delete all tasks
```javascript
db.tasks.deleteMany({})
```

---

## 🐛 Troubleshooting

### **MongoDB not running**
```bash
# Windows - Start MongoDB service
net start MongoDB
# Or check Services (services.msc)
```

### **Port 27017 error**
```bash
# Check if in use
netstat -ano | findstr :27017

# Kill process on Windows
taskkill /PID <PID> /F
```

### **Connection refused**
Ensure MongoDB is running and accessible at `localhost:27017`

### **Login not working**
- Clear browser cache/cookies
- Check MongoDB is running
- Verify admin user exists: `db.admin_users.find()`

---

## ✨ Features

- Single page for task management
- Admin-only CRUD operations
- Responsive design
- MongoDB storage (100%)
- Custom authentication
- Session management
- Task filtering (Pending/Done)

---

## 🚀 Deployment Ready

To deploy:
1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Add your domain to `ALLOWED_HOSTS`
4. Update MongoDB connection to production URL
5. Use production WSGI server (Gunicorn, etc.)

