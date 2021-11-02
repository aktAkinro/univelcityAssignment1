from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=300)
    cohort = models.CharField(max_length=300)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    author = models.CharField(max_length=300)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="books")
    # student = models.OneToOneField(Student, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    isbn = models.CharField(max_length=42, null=True, blank=True )
    # isb = models.CharField(max_length=42, null=True, blank=True)
    
    def __str__(self):
        return self.title

