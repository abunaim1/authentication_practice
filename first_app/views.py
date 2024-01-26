from django.shortcuts import render, redirect
from first_app.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form':form, 'type':'Registration'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'User Logged Successfully')
                return redirect('profile')
        else:
            messages.warning(request, 'Incorrect Username password')
            return redirect('login')
    else:
        form = AuthenticationForm(request)
        return render(request, 'register.html', {'form':form, 'type':'Login'})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Password Updated!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'register.html', {'form':form, 'type':'Password Change'})

def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Password Updated!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'register.html', {'form':form, 'type':'Password Change'})



