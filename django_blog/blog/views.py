# blog/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileUpdateForm

class UserLoginView(LoginView):
    template_name = 'blog/login.html'

class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, log the user in after registration
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})
