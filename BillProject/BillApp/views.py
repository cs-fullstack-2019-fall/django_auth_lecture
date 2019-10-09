from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, 'BillApp/index.html')

def login_user(request):
    return render(request, "BillApp/login_user.html")

def logout_user(request):
    return render(request, "BillApp/index.html")

def new_user(request):
    if request.method == "POST":
        User.objects.create_user(username= request.POST['username'], email = "", password = request.POST['password'])
    context = {
        "form": UserForm()
    }
    return render(request, 'BillApp/new_user.html', context)

def dashboard(request):
    return render(request, "BillApp/dashboard.html")