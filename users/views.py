from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms import SignupForm, LoginForm
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
        

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/start/")
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                return redirect("/start/")
            
            else:
                print("로그인에 실패했습니다.")
                
        
        context = {"form": form}
        return render(request, "users/login.html", context)
    
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)
    
    
def logout_view(request):
    logout(request)
    return redirect("/users/login/")