from django.db import models
from .models import *

# Create your models here. 

class Student(models.Model): 
    age = models.IntegerField(verbose_name="Age")
    fullname = models.CharField(verbose_name="Full Name", max_length=50, null=True, blank=True)
    registered_date = models.DateField(verbose_name="Registered Date", auto_now_add=True)
    updated_date = models.DateField(verbose_name="Updated Date", auto_now=True)

    class Meta: 
        verbose_name = "Student"
    def __str__(self):
        return self.fullname
    
    def calculate_z_score(self): 
        mean_age = Student.objects.all().aggregate(models.Avg('age'))['age_avg'] 
        std_dev_age = Student.objects.all().aggregate(models.StdDev('age'))['age_stddev']
        z_score = (self.age - mean_age) / std_dev_age 
        return z_score
