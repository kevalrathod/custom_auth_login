from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .forms import SignUpForm


@login_required
def home(request):
	return render(request,'profiles/home.html')

def signup(request):
	if request.method=='POST':	
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.refresh_from_db()
			user.profile.height=form.cleaned_data.get('height')
			user.profile.weight=form.cleaned_data.get('weight')
			# username=form.cleaned_data('username')
			user.save()
			raw_password=form.cleaned_data.get('password1')
			user=authenticate(username=user.username,password=raw_password)
			login(request,user)
			return redirect('home')
	else:
		form=SignUpForm()
	return render(request,'profiles/signup.html',{'form':form})