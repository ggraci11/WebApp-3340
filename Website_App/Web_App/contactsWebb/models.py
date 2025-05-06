from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Optional description
    due_date = models.DateField(null=True, blank=True)  # Optional due date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
