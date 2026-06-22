from django.core.management.base import BaseCommand
from tasks.admin_user import AdminUser


class Command(BaseCommand):
    help = 'Create an admin user for MongoDB'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Admin username')
        parser.add_argument('--email', type=str, help='Admin email')
        parser.add_argument('--password', type=str, help='Admin password')

    def handle(self, *args, **options):
        username = options.get('username') or input('Enter username: ')
        email = options.get('email') or input('Enter email: ')
        password = options.get('password') or input('Enter password: ')

        try:
            # Check if user already exists
            existing = AdminUser.objects(username=username).first()
            if existing:
                self.stdout.write(self.style.ERROR(f'❌ User "{username}" already exists!'))
                return

            # Create new admin user
            admin = AdminUser(
                username=username,
                email=email
            )
            admin.set_password(password)
            admin.save()

            self.stdout.write(self.style.SUCCESS(f'✅ Admin user "{username}" created successfully!'))
            self.stdout.write(f'   Email: {email}')
            self.stdout.write(f'\n🔐 You can now login at http://127.0.0.1:8000/tasks/login/')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error creating admin user: {str(e)}'))
