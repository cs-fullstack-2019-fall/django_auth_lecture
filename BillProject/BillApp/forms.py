from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import BillModel

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class BillForm(ModelForm):
    class Meta:
        model = BillModel
        fields = ['name']