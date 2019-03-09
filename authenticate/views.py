from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'authenticate/home.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('you have successfuly logged it'))
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('login failed'))
            return redirect('login')
    else:
        return render(request,'authenticate/login.html',{},)

def logout_user(request):
    if request.user.is_authenticated :
        logout(request)
        messages.success(request, ('logged out'))
        return redirect('home')
    else:
        return redirect('home')
