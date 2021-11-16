from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('students/', views.students),
    path('books/', views.books),   
    path('books/<int:book_id>', views.book_detail),   
    path('students/<int:student_id>', views.student_detail),
    path('cohort/', views.cohort_list),
]