from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = get_user_model().objects.create_user(password=raw_password, username=username, email=email)
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('')
        # TODO add reverse redirect
    else:
        form = SignupForm()
    return render(request, "users/signup.html", {'form': form})


@login_required
def profile(request):
    return HttpResponse('Profile')
