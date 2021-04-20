from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import *
from django.contrib.auth import authenticate, login,logout

from django.contrib import messages 

#restrict user to check main page 
from django.contrib.auth.decorators import login_required

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #only get the username
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect('login:login')

    context ={ 'form': form }
    return render(request, 'login/register.html',context)

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('blogs:blogs')
        else:
            messages.info(request,'Username Or password is incorrect')
            return render(request, 'login/login.html')
    context ={}
    return render(request, 'login/login.html',context)

def logoutUser(request):
    return redirect('login:login')
