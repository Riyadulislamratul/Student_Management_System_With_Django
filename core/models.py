from django.db import models

# Create your models here.

class Students(models.Model):
    student_ID = models.models.IntegerField(_)
    full_name = models.TextField(max_length=100)
    department = models.TextField(max_length=100)
    gender = models.TextField(max_length=10)
    address = models.TextField(max_length=200)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.student_ID} - {self.full_name}"