from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'BillApp/index.html')

def login_user(request):
    return render(request, "BillApp/login_user.html")

def logout_user(request):
    return render(request, "BillApp/index.html")

def new_user(request):
    return render(request, 'BillApp/new_user.html')

def dashboard(request):
    return render(request, "BillApp/dashboard.html")