from django.db import models

# Create your models here.
class Course(models.Model):
    course=models.CharField(max_length=120,unique=True)
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.course

class Batch(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch=models.CharField(max_length=120,unique=True)
    active_status=models.BooleanField(default=True)