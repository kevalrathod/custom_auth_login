from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string


from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from .models import Profile
from django.http import HttpResponseRedirect


def home(request):
    return render(request,'profiles/home.html')

def signup(request):
    if request.method=='POST':  
        form=SignUpForm(request.POST)
        if form.is_valid():
            user_name=request.POST['user_name']
            upassword = request.POST['upassword']
            new_user = Profile(user_name=user_name,upassword=upassword)
            new_user.save()
            print('mark1')
            return HttpResponseRedirect("/login/")
    else:
        form=SignUpForm()
    return render(request,'profiles/signup.html',{'form':form})

def login(request):
    form=LoginForm(request.POST)
    if request.method=='POST':
        user_name=request.POST['user_name']
        upassword = request.POST['upassword']
        print(request.POST)
        try:
            user = Profile.objects.get(user_name=user_name,upassword=upassword)
            if(user):
                print('USEr found in DB')
                return HttpResponseRedirect("/home/")
        except Exception as e:
            print('profile does not exists')
    else:
        form =LoginForm()
    return render(request, 'profiles/login.html',{'form':form})


def logout(request):
    pass