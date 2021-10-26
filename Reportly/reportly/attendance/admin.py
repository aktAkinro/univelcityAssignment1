from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book) # this is one way to register

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "no_of_pages", "date"]
    list_editable = ["no_of_pages"]
    list_filter = ["date"]
    list_per_page = 2
    search_fieldss = ["title", "author","body"]




