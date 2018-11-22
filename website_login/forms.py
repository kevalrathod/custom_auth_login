from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile




class LoginForm(forms.ModelForm):
    user_name=forms.CharField(max_length=40, help_text='required username')
    upassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Profile
        fields = ('user_name','upassword')

class SignUpForm(forms.ModelForm):
    user_name=forms.CharField(max_length=40, help_text='required username')
    upassword = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    height=forms.IntegerField(help_text='enter in cm')
    weight=forms.IntegerField(help_text='enter in KG')
    


    class Meta:
        model = Profile
        fields = ('user_name','upassword','email','height','weight')
        

