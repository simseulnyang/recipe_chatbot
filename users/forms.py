from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class SignupForm(forms.Form):
    email = forms.EmailField()
    nickname = forms.CharField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            self.add_error("password2", "비밀번호와 비밀번호 확인란의 값이 다릅니다.")
            
    def save(self):
        email=self.cleaned_data["email"]
        nickname=self.cleaned_data["nickname"]
        password1=self.cleaned_data["password1"]
        
        user = User.objects.create_user(
            email=email,
            nickname=nickname,
            password=password1
        )
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")