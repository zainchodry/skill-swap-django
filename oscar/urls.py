from django.urls import path
from . views import *
from django.contrib.auth import views as auth_view
from . forms import *

urlpatterns = [
    path('home', home_view, name='home'),
    path('offer/new/', create_offer, name='create_offer'),
    path('request/new/', create_request, name='create_request'),
    path('', Signup.as_view(), name='register'),
    path('/login', auth_view.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name='login'),
    path('logout', logout, name='logout')


]

