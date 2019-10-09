from django.urls import path
from . import views
# Don't forget to add all the routes you need for your views.
# Check this page if you're getting a reverse match error
# Check for case sensitivity when you get errors
# Create all views for all paths

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('new_user/', views.new_user, name="new_user"),
]