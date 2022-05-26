from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
            # why authenticate() when we just created the user?
            # user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect(reverse('homepage:home'))
    else:
        form = SignupForm()
    return render(request, "users/signup.html", {'form': form})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        data_form = UserDataForm(request.POST, request.FILES, instance=request.user)
        profile_form = ProfileForm(request.POST)
        if data_form.is_valid() and profile_form.is_valid():
            data_form.save()
            user.profile.birthday = profile_form.cleaned_data["birthday"]
            user.save()
            return redirect(reverse('users:profile'))
    else:
        data_form = UserDataForm(initial={"email": user.email, "first_name": user.first_name,
                                          "last_name": user.last_name, "remove_photo": False})
        profile_form = ProfileForm(initial={"birthday": user.profile.birthday})
    context = {
        "data_form": data_form,
        "profile_form": profile_form
    }
    return render(request, "users/profile.html", context)


def user_detail(request, user_id):
    user = get_user_model().objects.get(pk=user_id)

    publication_set = user.publication_set.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(publication_set, 5)
    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        publications = paginator.page(1)
    except EmptyPage:
        publications = paginator.page(paginator.num_pages)
    context = {
        'user': user,
        'current_user': request.user,
        'publications': publications,
    }
    return render(request, "users/user_detail.html", context)
