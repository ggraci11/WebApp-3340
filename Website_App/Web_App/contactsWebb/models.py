from django.db import models
from django.contrib.auth.models import User

# UserProfile to store user role (assigner or receiver)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    
    ROLE_CHOICES = (
        ('assigner', 'Assigner'),
        ('receiver', 'Receiver'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

# Task model with assigner and receiver
class Task(models.Model):
    assigner = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
