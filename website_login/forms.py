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
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    user_name=forms.CharField(max_length=40, help_text='required username')
    upassword = forms.CharField(widget=forms.PasswordInput)
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # height=forms.IntegerField(help_text='enter in cm')
    # weight=forms.IntegerField(help_text='enter in KG')
    # birth_date=forms.DateField(help_text='required format MM-DD-YY')


    class Meta:
        model = Profile
        # fields = ('user_name','upassword','email','height','weight','email','birth_date')
        fields = ('user_name','upassword')

