from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import is_authenticated
from .forms import UserRegisterForm, CreateAccount


@login_required
def index(request):
    return render(request, 'app/index.html')


@is_authenticated
def login_view(request):
    user_form = UserRegisterForm()
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


def create_new_user(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        account_form = CreateAccount(request.POST)
        account_form.instance.user = user_form.instance
        if user_form.is_valid() and account_form.is_valid():
            new_user_email = user_form.cleaned_data.get('email')
            user_form.save()
            account_form.save()
            messages.success(request, f'account has been created successfully for {new_user_email}')
            return redirect('login')
        else:
            messages.info(request, 'There was a problem creating your account, please try again and make sure you enter the right information.')   
    return redirect('login')


def logout_view(request):
    return


@login_required
def profile_view(request):
    return render(request, 'app/profile.html')
