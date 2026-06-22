from mongoengine import Document, StringField, DateTimeField, DateField, IntField, EmbeddedDocument
from datetime import datetime


class Task(Document):
    """Task model using MongoDB via mongoengine"""
    
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    )

    # Use ObjectId as primary key (automatically provided by mongoengine)
    sr_no = IntField(primary_key=True)
    description = StringField(max_length=300, required=True)
    owner = StringField(max_length=100, required=True)
    deadline = DateField(required=True)
    status = StringField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
        required=True
    )
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'tasks',
        'ordering': ['sr_no'],
        'indexes': ['deadline', 'status', 'owner']
    }

    def __str__(self):
        return f"{self.sr_no} - {self.description}"

    def save(self, *args, **kwargs):
        """Override save to update the updated_at timestamp"""
        self.updated_at = datetime.utcnow()
        if self.sr_no is None:
            # Auto-increment sr_no
            last_task = Task.objects().order_by('-sr_no').first()
            self.sr_no = (last_task.sr_no + 1) if last_task else 1
        return super().save(*args, **kwargs)
