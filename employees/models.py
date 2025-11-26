from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_new = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.eid})"
