from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import signup, CustomLoginView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]