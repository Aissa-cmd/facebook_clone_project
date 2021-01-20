from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import is_authenticated
from .forms import CreateUser, CreateAccount


@login_required
def index(request):
    return render(request, 'app/index.html')


@is_authenticated
def login_view(request):
    user_form = CreateUser()
    account_form = CreateAccount()
    context = {
        'user_form' : user_form,
        'account_form' : account_form,
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        next_page = request.GET.get('next')
        if user is not None:
            login(request, user)
            if next_page is not None:
                return redirect(next_page)
            else:
                return redirect('index')
        else:
            messages.info(request,
                          'Please enter a correct email address and password. Note that both fields maybe case-sensitive.')
            return redirect('login')
    return render(request, 'app/login.html', context)


def logout_view(request):
    return


def profile_view(request):
    return render(request, 'app/profile.html')
