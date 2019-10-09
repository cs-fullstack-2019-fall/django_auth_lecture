from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
def index(request):
    logout(request)
    return render(request, 'BillApp/index.html')

def login_user(request):
    return render(request, "BillApp/login_user.html")

def logout_user(request):
    return render(request, "BillApp/index.html")

def new_user(request):
    if request.method == "POST":
        newUserForm = UserForm(request.POST)
        if newUserForm.is_valid():

            User.objects.create_user(username= request.POST['username'], email = "", password = request.POST['password'])

            loggedInUser = authenticate(username = request.POST['username'], password = request.POST['password'])
            login(request, loggedInUser)
            return redirect("dashboard")
        else:    # Form is invalid
            context = {
                "errors": newUserForm.errors,
                "form": UserForm(),
            }
            return render(request, 'BillApp/new_user.html', context)
    else:   # If it's a GET method because request.method == 'GET'
        context = {
            "form": UserForm()
        }
        return render(request, 'BillApp/new_user.html', context)

def dashboard(request):
    return render(request, "BillApp/dashboard.html")