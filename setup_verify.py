#!/usr/bin/env python
"""
Quick setup script for Task Manager with MongoDB
Run this after installing dependencies to verify everything is working
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
import django
django.setup()

from tasks.models import Task

def test_mongodb_connection():
    """Test MongoDB connection"""
    print("\n" + "="*60)
    print("🔍 Testing MongoDB Connection...")
    print("="*60)
    
    try:
        # Try to query the database
        task_count = Task.objects().count()
        print(f"✅ MongoDB connection successful!")
        print(f"📊 Current tasks in database: {task_count}")
        return True
    except Exception as e:
        print(f"❌ MongoDB connection failed!")
        print(f"Error: {str(e)}")
        print("\n📝 Troubleshooting steps:")
        print("1. Ensure MongoDB is running (mongosh or MongoDB Compass)")
        print("2. Check connection settings in task_manager/settings.py")
        print("3. Verify MongoDB port (default: 27017)")
        return False

def create_sample_task():
    """Create a sample task"""
    print("\n" + "="*60)
    print("➕ Creating Sample Task...")
    print("="*60)
    
    try:
        from datetime import datetime, timedelta
        
        # Check if sample task already exists
        existing = Task.objects(description="Sample Task").first()
        if existing:
            print("ℹ️  Sample task already exists!")
            return True
        
        # Create sample task
        sample_task = Task(
            description="Sample: Complete project report",
            owner="Admin",
            deadline=datetime.now().date() + timedelta(days=7),
            status="Pending"
        )
        sample_task.save()
        
        print(f"✅ Sample task created!")
        print(f"   Serial: #{sample_task.sr_no}")
        print(f"   Description: {sample_task.description}")
        print(f"   Deadline: {sample_task.deadline}")
        return True
    except Exception as e:
        print(f"❌ Error creating sample task: {str(e)}")
        return False

def display_all_tasks():
    """Display all tasks"""
    print("\n" + "="*60)
    print("📋 All Tasks in Database")
    print("="*60)
    
    try:
        tasks = Task.objects().order_by('-created_at')
        
        if not tasks:
            print("No tasks found. Create one to get started!")
            return True
        
        for task in tasks:
            status_emoji = "✓" if task.status == "Done" else "⏱"
            print(f"\n  #{task.sr_no} - {task.description}")
            print(f"     Owner: {task.owner}")
            print(f"     Deadline: {task.deadline}")
            print(f"     Status: {status_emoji} {task.status}")
        
        print(f"\n📊 Total tasks: {len(tasks)}")
        return True
    except Exception as e:
        print(f"❌ Error displaying tasks: {str(e)}")
        return False

def main():
    """Run setup verification"""
    print("\n" + "🚀 "*20)
    print("Task Manager - MongoDB Setup Verification")
    print("🚀 "*20)
    
    # Test MongoDB connection
    if not test_mongodb_connection():
        print("\n⚠️  Setup incomplete. Fix MongoDB connection and try again.")
        sys.exit(1)
    
    # Display existing tasks
    display_all_tasks()
    
    print("\n" + "="*60)
    print("✅ Setup Verification Complete!")
    print("="*60)
    print("\n🎯 Next steps:")
    print("1. Run: python manage.py createsuperuser (if not done)")
    print("2. Run: python manage.py runserver")
    print("3. Visit: http://127.0.0.1:8000/tasks/")
    print("4. Login with admin credentials")
    print("5. Create, update, or delete tasks!")
    print("\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
