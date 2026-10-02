from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=250) #required field
    is_completed = models.BooleanField(default=False) # not required field
    created_at = models.DateTimeField(auto_now_add=True) #auto-genereted
    updated_at = models.DateTimeField(auto_now=True) ##auto-genereted

    def __str__(self):
        return self.task


