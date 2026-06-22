from django.contrib import admin

# Mongoengine models don't work directly with Django admin
# CRUD operations are handled through the custom views instead
# For MongoDB management, use MongoDB Compass or mongosh command line

# Alternatively, you can register models here if you want to use django-admin-mongoengine
# but for simplicity, we're using custom views for CRUD operations
