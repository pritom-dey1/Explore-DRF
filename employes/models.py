from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name