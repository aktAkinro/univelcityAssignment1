from django.contrib import admin
from .models import Book, Student

# Register your models here.
# admin.site.register(Book) # this is one way to register

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "id", "no_of_pages", "date"]
    list_editable = ["no_of_pages"]
    list_filter = ["date"]
    list_per_page = 2
    search_fieldss = ["title", "author","body"]

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    display = ["First_name","id", "Last_name"]
    editable = ["First_name"]
    filter = ["First_name"]
    
    



    

# @admin.register(student)
# class studentAdmin(admin.ModelAdmin):
#     list_display = ["First_name","Last_name"]
#     list_editable = ["First_name","Last_name"]




