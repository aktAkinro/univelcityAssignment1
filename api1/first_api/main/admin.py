from django.contrib import admin
from .models import Book, Student

# Register your models here.
# admin.site.register([Book, Student])
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