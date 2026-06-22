from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import Http404
from .models import Task
from .forms import TaskForm
from .admin_user import AdminUser
import hashlib


def get_admin_from_session(request):
    """Get admin user from session"""
    admin_id = request.session.get('admin_id')
    if admin_id:
        try:
            admin = AdminUser.objects.get(id=admin_id)
            return admin
        except:
            return None
    return None


def is_admin_logged_in(request):
    """Check if user is admin"""
    return get_admin_from_session(request) is not None


@require_http_methods(["GET", "POST"])
def admin_login(request):
    """Admin login view"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        try:
            admin = AdminUser.objects.get(username=username)
            if admin.check_password(password):
                request.session['admin_id'] = str(admin.id)
                request.session.set_expiry(86400)  # 24 hours
                return redirect('task_list')
            else:
                error = "Invalid password"
        except AdminUser.DoesNotExist:
            error = "User not found"
        except Exception as e:
            error = f"Error: {str(e)}"
        
        return render(request, 'tasks/login.html', {'error': error})
    
    # Redirect to task list if already logged in
    if is_admin_logged_in(request):
        return redirect('task_list')
    
    return render(request, 'tasks/login.html')


@require_http_methods(["GET"])
def admin_logout(request):
    """Admin logout view"""
    if 'admin_id' in request.session:
        del request.session['admin_id']
    return redirect('task_list')


@require_http_methods(["GET"])
def task_list(request):
    """Display all tasks"""
    try:
        tasks = Task.objects().order_by('sr_no')
    except Exception as e:
        tasks = []
    
    admin = get_admin_from_session(request)
    context = {
        'tasks': tasks,
        'is_admin': admin is not None,
        'admin': admin
    }
    return render(request, 'tasks/task_list.html', context)


@require_http_methods(["GET", "POST"])
def create_task(request):
    """Create a new task (Admin only)"""
    admin = get_admin_from_session(request)
    if not admin:
        return redirect('admin_login')
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save_task()
                return redirect('task_list')
            except Exception as e:
                form.add_error(None, f"Error saving task: {str(e)}")
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create', 'admin': admin})


@require_http_methods(["GET", "POST"])
def update_task(request, pk):
    """Update a task (Admin only)"""
    admin = get_admin_from_session(request)
    if not admin:
        return redirect('admin_login')
    
    try:
        task = Task.objects.get(sr_no=pk)
    except Task.DoesNotExist:
        raise Http404("Task not found")
    except Exception as e:
        raise Http404(f"Error retrieving task: {str(e)}")
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save_task(task)
                return redirect('task_list')
            except Exception as e:
                form.add_error(None, f"Error updating task: {str(e)}")
    else:
        form = TaskForm(initial={
            'description': task.description,
            'owner': task.owner,
            'deadline': task.deadline,
            'status': task.status,
        })
    
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Update', 'task': task, 'admin': admin})


@require_http_methods(["POST"])
def delete_task(request, pk):
    """Delete a task (Admin only) and auto-renumber remaining tasks"""
    admin = get_admin_from_session(request)
    if not admin:
        return redirect('admin_login')
    
    try:
        task = Task.objects.get(sr_no=pk)
        task.delete()
        
        # Auto-renumber all remaining tasks (1, 2, 3, ... with no gaps)
        remaining_tasks = Task.objects().order_by('sr_no')
        for index, remaining_task in enumerate(remaining_tasks, start=1):
            remaining_task.sr_no = index
            remaining_task.save()
    except Task.DoesNotExist:
        raise Http404("Task not found")
    except Exception as e:
        print(f"Error deleting task: {str(e)}")
    
    return redirect('task_list')
