from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    author = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    isbn = models.CharField(max_length=42, null=True, blank=True )
    # isb = models.CharField(max_length=42, null=True, blank=True)
    
    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    age = models.IntegerField(default=10)
    course = models.CharField(max_length=300)
    bio = models.TextField()

    def __str__(self):
        return self.first_name
