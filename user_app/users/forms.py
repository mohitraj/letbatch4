from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser




class SignUpForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['email','native_name','phone_no']
