from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages

# Create your views here.
# Make sure your App URLs match your views

# This definition will render the index/home page
def index(request):
    # I was previously logging all users out when they visited the home page when testing for logged in users
    # logout(request)
    return render(request, 'BillApp/index.html')

# This definition will render the user form.
# When user presses the submit button (when the definition has a POST request), it will check to see if the username and password saved in the database matches the username they submitted in the form. If the username/password is correct, it'll log them in. If it's incorrect, send an error message and reload the page.
def login_user(request):
    # This happens when the user press the submit button
    if request.method == "POST":
        # For the user to be authenticated, the user has to be in the database AND the password in the form has to match the password of the user. If they are not authenticated, None will be returned to the variable. If they are authenticated, an instance of the User class will be returned to the variable.
        loggedInUser = authenticate(username = request.POST['username'], password = request.POST["password"])
        # If it returns anything except for None, the user was authenticated properly
        if loggedInUser is not None:
            # login is a built-in imported function. You should send request and the User table instance that was logged in. The request parameters need to match.
            login(request, loggedInUser)
            # Redirect to the route with dashboard as the nickname
            return redirect("dashboard")
        # If the authenticated user equaled None, do the code below
        else:
            # Send an error message to the user letting them know there was an error. Call the messages array in your html
            messages.error(request, "Wrong username or password")
            # Redirect to the route with login_user as the nickname
            return redirect("login_user")

            ## *** This is a different way you can send an error message and rerender the login_user page ***
            # context = {
            #     "error": "Wrong username or password",
            #     "form": UserForm(),
            # }
            # return render(request, "BillApp/login_user.html", context)

    # If the login_user page is called and didn't press the submit button, run the code below
    context = {
        "form": UserForm()
    }
    return render(request, "BillApp/login_user.html", context)

def logout_user(request):
    # If you want to log the currently logged in user, call logout. If there is not a logged in user, it will not do anything and won't hurt your system.
    logout(request)
    return redirect("index")


def new_user(request):
    # This happens when the user press the submit button, run the if statement code below
    if request.method == "POST":
        # Save user data into a form instance
        newUserForm = UserForm(request.POST)
        # If all of the user submitted data is accurate, run the code below
        if newUserForm.is_valid():
            # Create a new user to the built-in Django User table and save the user instance to the loggedInUser variable
            loggedInUser = User.objects.create_user(username= request.POST['username'], email = "", password = request.POST['password'])
            # login is a built-in imported function. You should send request and the User table instance that was logged in. The request parameters need to match.
            login(request, loggedInUser)
            return redirect("dashboard")
        # If the form was inaccurate, run the code below
        else:
            context = {
                # You can use the form attribute errors to see why the form was not valid. Call errors in your html
                "errors": newUserForm.errors,
                "form": UserForm(),
            }
            return render(request, 'BillApp/new_user.html', context)

    # If it's a GET method because request.method == 'GET'
    # If they go to create new user page and didn't press the submit button, run the code below
    else:
        context = {
            "form": UserForm()
        }
        return render(request, 'BillApp/new_user.html', context)

# This will show the dashboard html
def dashboard(request):
    return render(request, "BillApp/dashboard.html")