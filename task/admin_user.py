from mongoengine import Document, StringField, BooleanField, DateTimeField
from datetime import datetime
import hashlib


class AdminUser(Document):
    """Custom Admin User model using MongoDB"""
    
    username = StringField(required=True, unique=True, max_length=150)
    email = StringField(required=True, max_length=254)
    password_hash = StringField(required=True)  # Hashed password
    is_active = BooleanField(default=True)
    is_superuser = BooleanField(default=True)
    is_staff = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'admin_users',
        'indexes': ['username', 'email']
    }
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        """Verify password"""
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()
    
    def __str__(self):
        return self.username
