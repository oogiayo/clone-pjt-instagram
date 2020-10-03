from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods


# User Authentication -------------------------------
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url or 'posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('posts:index')
    
    return redirect('accounts:login')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile', user)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def delete(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method=='POST':
        request.user.delete()
        return redirect('posts:index')
    
    return render(request, 'accounts/delete.html')
    

@login_required
@require_http_methods(['GET', 'POST'])
def password_update(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            auth_login(request, request.user)
            return redirect('accounts:update')
    else:       
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password_update.html', context)


# User Profile ----------------------------------
@login_required
@require_http_methods(['GET', 'POST'])
def profile(request, username):
    person = get_object_or_404(User, username=username)
    context ={
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, username):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    person = get_object_or_404(User, username=username)
    me = request.user
    if person!=me:
        if person.followers.filter(pk=me.pk).exists():
            person.followers.remove(me)
        else:
            person.followers.add(me)
    return redirect('accounts:profile', username)

