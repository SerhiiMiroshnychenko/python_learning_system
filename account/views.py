from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm, RegistrationForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'


def sing_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(request, username=username, password=password)
            if user := authenticate(request, **form.cleaned_data):
                login(request, user)
                print(user.username)
                return redirect('home')
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def sing_out(request):
    logout(request)
    return redirect('home')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


