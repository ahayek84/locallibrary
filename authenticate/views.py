from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, UpdateProfileForm,UpdateUserForm
from .models import User

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

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        pform = UpdateProfileForm(request.POST)
        if form.is_valid():
            a = form.save()
            b = pform.save(commit=False)
            b.user_id = a.id
            b.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,('you have successfuly register it'))
            return redirect('home')

    else:
        form = SignUpForm()
        pform = UpdateProfileForm()

    context = {'form':form,
               'pform': pform}
    return render(request, 'authenticate/register.html', context)

def update_profile(request):
    if request.method == 'POST':
        # update user info
        form = UpdateUserForm(request.POST, instance=request.user)
        pform = UpdateProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid() and pform.is_valid():
            form.save()
            pform.save()
            messages.success(request,('you have successfuly updated your profile'))
            return redirect('home')
    else:
        # show user info
        form = UpdateUserForm(instance=request.user)
        pform = UpdateProfileForm(instance=request.user.profile)
    context = {'form':form,
               'pform': pform}
    return render(request, 'authenticate/update_profile.html', context)