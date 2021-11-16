from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

def get_cohort():
    date = timezone.now()
    cohort = datetime.strftime(date, "%B-%Y")
    return cohort





class Student(models.Model):
    first_name = models.CharField(max_length=300)
    cohort = models.CharField(max_length=300, default=get_cohort())
    date_joined = models.DateTimeField(auto_now_add=True, null = True)


    def __str__(self):
        return self.first_name

    @property
    def book(self):
        return self.books.all().values("title")

class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    author = models.CharField(max_length=300)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="books")
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


    @property
    def student_name(self):
        return self.student.first_name

    
    
    

