from django.shortcuts import render
from .models import Customer, Accounts
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'banking_app_templates/index.html', context)

@login_required
def user_account(request, pk):
    return render(request, 'banking_app_templates/accounts.html', context)

def signup(request):
    context = {}
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_name = request.POST['user']
        email = request.POST['user']
        if password == confirm_password:
            if User.objects.create_user(user_name, email, password):
                return render(request, 'banking_app_templates/index.html', context)
            else:
                context = {
                        'error' : 'Could not create user account - please try again.'
                        }
            else:
                context = {
                        'error' : 'Passwords did not match - please try again'
                        }
    return render(request, 'registration/signup.html', context)
