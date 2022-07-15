from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterStudent(UserCreationForm):
	email = forms.EmailField(label = "email",max_length= 100, required = True)
	first_name = forms.CharField(label = "first_name",max_length=100,required=True)
	last_name = forms.CharField(label="last_name",max_length=100,required=True)
	
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","password1","password2"]

