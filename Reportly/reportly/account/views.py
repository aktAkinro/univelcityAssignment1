from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
def login_view(request):
    if request.method == "POST":
       userrname = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, userrname = userrname, password=password)
       print(user)

    return render(request, 'registration/login.html')