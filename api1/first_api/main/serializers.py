from django.db.models import fields
from rest_framework import serializers
from .models import Student, Book

class StudentSerializer(serializers.ModelSerializer):
    book = serializers.ReadOnlyField()

    
    class Meta:
        model = Student
        fields = ['id','first_name', 'cohort','date_joined','book']
        # fields = '__all__'

class Bookserializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField()

    class Meta:
        model = Book
        fields = ["id","title","no_of_pages","author","student","student_name","body","date"]
        