from django.shortcuts import render, redirect, get_object_or_404
# from .models import User 
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomAuthenticationForm, ProfileForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:signin')
    else:   
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signin.html', context)

def logout(request):
    auth_logout(request)
    return redirect('/')

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user 
            profile.save()


            if user.profile_set.all().count() > 1:
                user.profile_set.all()[0].delete()
                
            return redirect('accounts:detail', pk)
    else:
        profile_form = ProfileForm()
    
    if user.profile_set.all().count() == 0:
        profile_image = None
    else:
        profile_image = user.profile_set.all()[0]
    context = {
        'user' : user, 
        'profile_form' : profile_form,
        'profile_image' : profile_image,
    }
    return render(request, 'accounts/detail.html', context)

def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)

    return redirect('/')