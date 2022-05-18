from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SignupForm, UserDataForm, ProfileForm


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
            return redirect(reverse('homepage:home'))
    else:
        form = SignupForm()
    return render(request, "users/signup.html", {'form': form})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        data_form = UserDataForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST)
        if data_form.is_valid() and profile_form.is_valid():
            user.first_name = data_form.cleaned_data.get('first_name')
            user.last_name = data_form.cleaned_data.get('last_name')
            user.email = data_form.cleaned_data.get('email')
            user.email = data_form.cleaned_data.get('image')
            user.profile.birthday = profile_form.cleaned_data["birthday"]
            user.save()
    else:
        data_form = UserDataForm(initial={"email": user.email, "first_name": user.first_name,
                                          "last_name": user.last_name})
        profile_form = ProfileForm(initial={"birthday": user.profile.birthday})
    context = {
        "data_form": data_form,
        "profile_form": profile_form
    }
    return render(request, "users/profile.html", context)
