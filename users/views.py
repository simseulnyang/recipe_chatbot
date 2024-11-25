from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from users.forms import SignupForm
from users.models import User


def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("")
        
        else:
            context = {"form": form}
            return render(request, "users/signup.html", context)
    
    else:
        form = SignupForm()
        context = {"form": form}
        return render(request, "users/signup.html", context)
        

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True 