from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, ReportForm, CustomAuthenticationForm
# from .models import Report, Contact


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    # print(request.user.is_authenticated)
    # if request.user.is_authenticated:
    #     return render(request, 'profile.html', {'user': request.user})
    # else:
    return render(request, 'login.html')



def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def report(request):
    if request.method == "POST":
        form = ReportForm(request.POST, initial={'email': request.user.email})
        if form.is_valid():
            instance = form.save(commit=False)
            email = request.user.email
            instance.email = email
            instance.save()
            messages.success(request, f'Your report has been accepted.')
            return redirect('profile')
    else:
        form = ReportForm()

    context = {'form': form}
    return render(request, 'report-problem.html', context)

def reply(request):
    return render(request, 'reply.html')