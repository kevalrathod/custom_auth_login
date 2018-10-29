from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect


@login_required
def home(request):
	return render(request,'profiles/home.html')

def signup(request):
	if request.method=='POST':	
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data('username')
			password=form.cleaned_data('password1')
			user=authenticate(username=username,password=password1)
			login(request,user)
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'profiles/signup.html',{'form':form})