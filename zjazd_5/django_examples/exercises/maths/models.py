from django.db import models

# Create your models here.

class Math(models.Model):
    operation = models.CharField(max_length=10)
    arg_a = models.IntegerField()
    arg_b = models.IntegerField()

def __str__(self):
    return f"Math operation: {self.operation}"