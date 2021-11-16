from copy import error
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import Bookserializer, StudentSerializer
from .models import Book, Student

# Create your views here.

@api_view(['GET', 'POST'])
def students(request):

    if request.method =='GET':
        all_students = Student.objects.order_by('-date_joined')

        serializer = StudentSerializer(all_students, many=True)

        data = {
            "message":"success",
            "data" : serializer.data
        } 
        return Response(data, status=status.HTTP_200_OK)


    elif request.method == 'POST':

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                "message" : "success",
                "data" : serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        else:
            error = {
                'message' : 'failed',
                'error' : serializer.errors
            }

            return Response(error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def books(request):

    if request.method =='GET':
        all_books = Book.objects.order_by('-date')

        serializer = Bookserializer(all_books, many=True)

        data = {
            "message":"success",
            "data" : serializer.data
        } 
        return Response(data, status=status.HTTP_200_OK)


    elif request.method == 'POST':

        serializer = Bookserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                "message" : "success",
                "data" : serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        else:
            error = {
                'message' : 'failed',
                'error' : serializer.errors
            }

            return Response(error, status=status.HTTP_400_BAD_REQUEST)

# to view just one book, PUT is same as update. since it is just one item we would be able to get it, update and delete it
@api_view (['GET','PUT','DELETE'])
def book_detail(request,book_id):

    """
    Takes in a book id and returns the http response depending on the http method.
    
    Args:
    book_id: Integer
    
    Allowed methods:
    GET - Get the details of single book
    PUT - Allows the book detail to be edited
    DELETE - THis logic delets the book record from the data base
    """

    try:
        book = Book.objects.get(id= book_id)
    except Book.DoesNotExist:
        error = {
            'message':'failed',
            'errors': f"Book with id {book_id} does not exist"
        }

        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Bookserializer(book)
        data = {
            "message":"success",
            "data" : serializer.data
        } 

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = Bookserializer(book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                "message" : "success",
                "data" : serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        
        else:
            error = {
                'message' : 'failed',
                'error' : serializer.errors
            }

            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()

        return Response({"message":"success"}, status=status.HTTP_204_NO_CONTENT)




@api_view (['GET','PUT','DELETE'])
def student_detail(request,student_id):

    """
    Takes in a student id and returns the http response depending on the http method.
    
    Args:
    student_id: Integer
    
    Allowed methods:
    GET - Get the details of single student
    PUT - Allows the student detail to be edited
    DELETE - THis logic delets the student record from the data base
    """

    try:
        student = Student.objects.get(id= student_id)
    except Student.DoesNotExist:
        error = {
            'message':'failed',
            'errors': f"Student with id {student_id} does not exist"
        }

        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        data = {
            "message":"success",
            "data" : serializer.data
        } 

        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data, partial=True) # partial = true allows you edit individual 

        if serializer.is_valid():
            serializer.save()
            data = {
                "message" : "success",
                "data" : serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        
        else:
            error = {
                'message' : 'failed',
                'error' : serializer.errors
            }

            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()

        return Response({"message":"success"}, status=status.HTTP_204_NO_CONTENT)



# we want to write A code to get all students in a particular cohort

@api_view(["GET"])
def cohort_list(request):
    if request.method == 'GET':
        cohorts = Student.objects.values_list("cohort", flat=True).distinct() # flat= true gives us a list rather than a list of tupple

        data = {cohort:Student.objects.filter(cohort=cohort).values() for cohort in cohorts} # if value() is left it shows every detail, if i use value("first_name") it shows just name

        return Response({}, status=status.HTTP_204_NO_CONTENT)
