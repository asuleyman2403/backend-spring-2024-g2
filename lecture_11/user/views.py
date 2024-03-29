from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login
from .models import Profile
from .forms import ProfileForm


def login_page_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            login(request, user)
            if user is not None:
                return redirect('/')
            else:
                form.add_error(field='username', error='Invalid password or login')
                return render(request, 'user/login.html', {'form': form})
        else:
            return render(request, 'user/login.html', {'form': form})


def register_page_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(owner_id=user.id)
            profile.save()
            auth_data = auth.authenticate(request, email=user.email, password=form.data.get('password'))
            if auth_data is not None:
                login(request, auth_data)
                return redirect('')
        return render(request, 'user/register.html', {'form': form})


def handle_logout(request):
    auth.logout(request)
    return redirect('/auth/login')


def settings_page_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(owner_id=request.user.id)
        if request.method == 'GET':
            form = ProfileForm(data={'bio': profile.bio}, files={'avatar': profile.avatar, 'resume': profile.resume})
            return render(request, 'user/settings.html', {'form': form, 'profile': profile})
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile.bio = form.data.get('bio', '')
                if form.files.get('avatar'):
                    profile.avatar = form.files.get('avatar')
                if form.files.get('resume'):
                    profile.resume = form.files.get('resume')
                profile.save()
            return render(request, 'user/settings.html', {'form': form, 'profile': profile})
    else:
        return redirect('/auth/login')
