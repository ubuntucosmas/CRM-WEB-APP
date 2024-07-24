from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import record

# Register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'validate'})) 



# Create Record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state'] 
        