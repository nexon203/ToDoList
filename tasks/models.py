from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    status = models.BooleanField(default=False)
    due = models.DateField()
    priority = models.CharField(max_length=10, null=False)
    category = models.CharField(max_length=20, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return f"{self.title} of {self.user.username}"


